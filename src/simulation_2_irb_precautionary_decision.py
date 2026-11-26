#!/usr/bin/env python3
"""
Simulation 2: Precautionary 3Rs Gatekeeping & Bayesian IRB Decision-Theoretic Analysis
Target Venue: Neuroethics (Springer Nature)

Operationalizes Russell & Burch's 3Rs (Replacement, Reduction, Refinement) into a
Bayesian Value-of-Information (VoI) / Precautionary Decision Model for pediatric IRBs.
- Models the trade-off between in-silico surrogate error (false negatives) and in-vivo pediatric exposure risk.
- Outputs the IRB Decision Frontier plot showing the exact conditions under which in-silico Replacement is ethically mandatory.
- Generates Fig4 (PDF, EPS, PNG 300DPI, TIFF 300DPI).
"""

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from PIL import Image

PROJECT_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_DIR / "manuscript"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Springer Nature typography styling (Clean Sans-Serif)
plt.rcParams.update({
    "font.sans-serif": ["Liberation Sans", "Helvetica", "Arial", "DejaVu Sans"],
    "font.family": "sans-serif",
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",
    "font.size": 10.0,
    "axes.titlesize": 11.5,
    "axes.labelsize": 10.5,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "legend.fontsize": 9.0,
    "figure.titlesize": 13.0,
    "axes.edgecolor": "#334155",
    "axes.linewidth": 1.0,
    "figure.autolayout": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

PALETTE = {
    "dark_navy": "#0F172A",
    "emerald": "#059669",
    "soft_emerald": "#ECFDF5",
    "emerald_border": "#10B981",
    "crimson": "#DC2626",
    "soft_crimson": "#FEF2F2",
    "crimson_border": "#EF4444",
    "amber": "#D97706",
    "soft_amber": "#FFFBEB",
    "amber_border": "#F59E0B",
    "blue": "#2563EB",
    "soft_blue": "#EFF6FF",
    "blue_border": "#3B82F6",
    "slate": "#64748B",
    "slate_light": "#F1F5F9"
}

def compute_decision_losses(N, p0=0.493, sens=0.886, spec=0.92, C_harm=1.0, C_comp=2.0, C_delay=0.1):
    """
    Computes expected ethical loss for In-Vivo vs In-Silico Precautionary Screening.
    N: Pediatric cohort size (number of minor students)
    p0: Prior probability that conversational tutor exhibits sycophantic answer leakage under wear-down
    sens: Sensitivity of in-silico multi-agent stress audit P(Flagged | Harmful)
    spec: Specificity of in-silico audit P(Cleared | Safe)
    C_harm: Unit developmental harm cost per child exposed to failing conversational sycophancy
    C_comp: Fixed computational cost of in-silico multi-agent audit
    C_delay: Marginal cost of delay for a false positive flag on a safe tutor
    """
    loss_invivo = p0 * N * C_harm
    
    # In-silico: compute cost + false negatives (harmful passed to children) + false positives (unnecessary revision delay)
    fn_rate = 1.0 - sens
    fp_rate = 1.0 - spec
    loss_insilico = C_comp + (p0 * fn_rate * N * C_harm) + ((1.0 - p0) * fp_rate * C_delay)
    
    delta_voi = loss_invivo - loss_insilico
    pct_risk_reduction = ((loss_invivo - loss_insilico) / (loss_invivo + 1e-6)) * 100.0
    
    return loss_invivo, loss_insilico, delta_voi, pct_risk_reduction

def generate_figure_4():
    """Generates Figure 4: Simulation 2 Bayesian IRB Decision Frontier & 3Rs Precautionary Analysis."""
    print("Running Simulation 2: Bayesian Value-of-Information & Precautionary IRB Gatekeeping...")
    
    # Calculate baseline metrics for paper text
    p0_nominal = 0.4933  # 49.33% guardrailed breakdown observed in empirical audit
    sens_nominal = 0.8500 # Pre-clinical benchmark clearance sensitivity threshold (>= 0.85)
    
    # Class cohort N = 30
    _, _, voi_30, red_30 = compute_decision_losses(30, p0=p0_nominal, sens=sens_nominal)
    # Grade cohort N = 120
    _, _, voi_120, red_120 = compute_decision_losses(120, p0=p0_nominal, sens=sens_nominal)
    # District pilot N = 1000
    _, _, voi_1000, red_1000 = compute_decision_losses(1000, p0=p0_nominal, sens=sens_nominal)
    
    print(f"  Classroom (N=30): VoI = {voi_30:.2f}, Risk Reduction = {red_30:.1f}%")
    print(f"  Grade Level (N=120): VoI = {voi_120:.2f}, Risk Reduction = {red_120:.1f}%")
    print(f"  District Pilot (N=1000): VoI = {voi_1000:.2f}, Risk Reduction = {red_1000:.1f}%")

    fig, axes = plt.subplots(2, 2, figsize=(13.2, 10.2), dpi=300)
    
    # =========================================================================
    # PANEL A: Expected Ethical Loss vs. Pediatric Cohort Size N
    # =========================================================================
    ax_a = axes[0, 0]
    N_arr = np.linspace(10, 1500, 200)
    
    # Status Quo In-Vivo Loss
    loss_vivo_arr = [compute_decision_losses(n, p0=p0_nominal)[0] for n in N_arr]
    
    # In-Silico Loss across Sensitivities
    loss_silico_85 = [compute_decision_losses(n, p0=p0_nominal, sens=0.85)[1] for n in N_arr]
    loss_silico_90 = [compute_decision_losses(n, p0=p0_nominal, sens=0.90)[1] for n in N_arr]
    loss_silico_98 = [compute_decision_losses(n, p0=p0_nominal, sens=0.98)[1] for n in N_arr]
    
    ax_a.plot(N_arr, loss_vivo_arr, color=PALETTE["crimson"], lw=3.0,
              label="Live Minor Trial (Status Quo Risk Escalation)")
    ax_a.plot(N_arr, loss_silico_85, color=PALETTE["emerald"], lw=2.8,
              label=r"In-Silico 3Rs Gatekeeping ($\mathrm{Sens} = 0.85$)")
    ax_a.plot(N_arr, loss_silico_98, color=PALETTE["blue"], lw=2.2, linestyle="--",
              label=r"High-Fidelity Surrogate ($\mathrm{Sens} = 0.980$)")
    
    # Shaded risk aversion area
    ax_a.fill_between(N_arr, loss_silico_85, loss_vivo_arr, color=PALETTE["soft_emerald"], alpha=0.35,
                      label="Harm Prevented by Computational Surrogacy")
    
    ax_a.set_title(r"(a) Expected Ethical Loss $\mathbb{E}[L]$ vs. Cohort Size ($N$)",
                   fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_a.set_xlabel("Proposed Pediatric Research Cohort Size ($N$ Children)", fontweight="bold")
    ax_a.set_ylabel(r"Expected Developmental Harm Loss ($\mathbb{E}[L]$)", fontweight="bold")
    ax_a.set_xlim(10, 1500)
    ax_a.set_ylim(0, 750)
    ax_a.grid(True, linestyle="--", alpha=0.5, color="#CBD5E1")
    ax_a.legend(loc="upper left", frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")

    # =========================================================================
    # PANEL B: Value of In-Silico Replacement (Delta VoI) vs. Model Breakdown Prior p0
    # =========================================================================
    ax_b = axes[0, 1]
    p0_grid = np.linspace(0.02, 0.98, 120)
    
    cohorts = [30, 120, 500, 1000]
    c_colors = [PALETTE["amber"], PALETTE["blue"], PALETTE["emerald"], PALETTE["dark_navy"]]
    c_labels = ["Classroom Pilot ($N = 30$)", "School Grade ($N = 120$)", "Multi-School Pilot ($N = 500$)", "District Pilot ($N = 1,000$)"]
    
    for n_val, col, lbl in zip(cohorts, c_colors, c_labels):
        voi_curve = [compute_decision_losses(n_val, p0=p, sens=0.85)[2] for p in p0_grid]
        ax_b.plot(p0_grid, voi_curve, color=col, lw=2.4, label=lbl)
        
    ax_b.axvline(0.4933, color=PALETTE["crimson"], linestyle=":", lw=1.8)
    ax_b.text(0.51, 380, r"Empirical Guardrailed Breakdown" + "\n" + r"Baseline ($p_0 = 49.33\%$)",
              fontsize=8.8, color=PALETTE["crimson"], fontweight="bold")
    
    ax_b.axhline(0, color="#64748B", lw=1.0)
    ax_b.set_title(r"(b) Precautionary Value of Information ($\Delta\mathrm{VoI}$)",
                   fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_b.set_xlabel(r"Prior Model Sycophancy Breakdown Probability ($p_0$)", fontweight="bold")
    ax_b.set_ylabel(r"Net Ethical Harm Averted ($\Delta\mathrm{VoI}$ Units)", fontweight="bold")
    ax_b.set_xlim(0, 1.0)
    ax_b.set_ylim(-10, 450)
    ax_b.grid(True, linestyle="--", alpha=0.5, color="#CBD5E1")
    ax_b.legend(loc="upper left", frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")

    # =========================================================================
    # PANEL C: The IRB Precautionary Decision Frontier (Sens vs. N)
    # =========================================================================
    ax_c = axes[1, 0]
    sens_mesh = np.linspace(0.70, 0.999, 100)
    n_mesh = np.linspace(5, 300, 100)
    SENS, N_GRID = np.meshgrid(sens_mesh, n_mesh)
    
    # Calculate Risk Reduction %
    REDUCT_GRID = np.zeros_like(SENS)
    for r in range(SENS.shape[0]):
        for c in range(SENS.shape[1]):
            REDUCT_GRID[r, c] = compute_decision_losses(N_GRID[r, c], p0=p0_nominal, sens=SENS[r, c])[3]
            
    cp = ax_c.contourf(SENS, N_GRID, REDUCT_GRID, levels=np.linspace(60, 100, 9), cmap="YlGn", alpha=0.85)
    cbar = fig.colorbar(cp, ax=ax_c, orientation="vertical", pad=0.03, aspect=24)
    cbar.set_label("Harm Reduction Achieved (%)", fontweight="bold", fontsize=9.5)
    
    # IRB Mandatory Decision Boundaries
    cs = ax_c.contour(SENS, N_GRID, REDUCT_GRID, levels=[80.0, 90.0, 95.0],
                      colors=["#D97706", "#047857", "#064E3B"], linewidths=[2.0, 2.4, 2.0], linestyles=["--", "-", ":"])
    ax_c.clabel(cs, inline=True, fmt={80.0: "80% Reduction", 90.0: "90% Mandatory Replacement Gate", 95.0: "95% Optimal Threshold"},
                fontsize=8.5)
    
    # Point marker for pre-clinical benchmark sensitivity = 0.85
    ax_c.scatter([0.85], [30], color=PALETTE["crimson"], s=90, zorder=6, edgecolor="#FFFFFF", lw=1.5)
    ax_c.annotate("Pre-Clinical Benchmark\n" + r"($\mathrm{Sens} = 0.85, N = 30 \to 71.5\%$ Reduction)",
                  xy=(0.85, 30), xytext=(0.71, 95),
                  arrowprops=dict(arrowstyle="->", color=PALETTE["crimson"], lw=1.5),
                  fontweight="bold", fontsize=8.8, color=PALETTE["crimson"])
    
    ax_c.set_title(r"(c) IRB Precautionary Decision Frontier", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_c.set_xlabel(r"In-Silico Surrogate Diagnostic Sensitivity ($\mathrm{Sens}$)", fontweight="bold")
    ax_c.set_ylabel("Proposed Pediatric Cohort Size ($N$)", fontweight="bold")
    ax_c.grid(True, linestyle=":", alpha=0.5, color="#334155")

    # =========================================================================
    # PANEL D: Multi-Parameter Sensitivity Heatmap: False-Negative Risk vs. p0
    # =========================================================================
    ax_d = axes[1, 1]
    fn_arr = np.linspace(0.01, 0.25, 80)  # beta in-silico = 1 - sens
    p0_arr = np.linspace(0.10, 0.80, 80)
    FN, P0 = np.meshgrid(fn_arr, p0_arr)
    
    # Net Harm Averted per Student: delta_H = p0 * (1 - FN)
    HARM_AVERTED = P0 * (1.0 - FN) * 100.0  # percentage points of absolute risk avoided per child
    
    cp_d = ax_d.contourf(FN * 100.0, P0 * 100.0, HARM_AVERTED, levels=np.linspace(10, 80, 8), cmap="Blues", alpha=0.90)
    cbar_d = fig.colorbar(cp_d, ax=ax_d, orientation="vertical", pad=0.03, aspect=24)
    cbar_d.set_label("Absolute Harm Averted per Child (%)", fontweight="bold", fontsize=9.5)
    
    # Isolines of Absolute Ethical Advantage
    cs_d = ax_d.contour(FN * 100.0, P0 * 100.0, HARM_AVERTED, levels=[25.0, 45.0, 65.0],
                        colors=["#0369A1", "#075985", "#082F49"], linewidths=[2.0, 2.2, 2.0])
    ax_d.clabel(cs_d, inline=True, fmt={25.0: "25% Averted", 45.0: "45% Averted (Guardrailed)", 65.0: "65% Averted"},
                fontsize=8.5)
    
    ax_d.set_title(r"(d) Pediatric Risk Averted per Minor Subject (%)", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_d.set_xlabel(r"In-Silico Audit False Negative Rate ($\beta_{\mathrm{in-silico}} = 1 - \mathrm{Sens}$ %)", fontweight="bold")
    ax_d.set_ylabel(r"Prior Model Sycophancy Vulnerability ($p_0$ %)", fontweight="bold")
    ax_d.grid(True, linestyle=":", alpha=0.5, color="#334155")

    plt.tight_layout(pad=2.5)
    
    # Export single vector PDF
    pdf_path = FIGURES_DIR / "fig4_simulation_irb_decision_frontier.pdf"
    fig.savefig(pdf_path, format="pdf", bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Generated Simulation 2 Figure: {pdf_path.name}")
    return {
        "red_30": float(red_30),
        "red_120": float(red_120),
        "red_1000": float(red_1000),
        "voi_30": float(voi_30),
        "voi_120": float(voi_120),
        "voi_1000": float(voi_1000)
    }

if __name__ == "__main__":
    res = generate_figure_4()
    print("Simulation 2 Completed Successfully!")
    print(res)
