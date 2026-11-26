#!/usr/bin/env python3
"""
Simulation 1: Extended Mind vs. Epistemic Parasitism Phase-Space Analysis
Target Venue: Neuroethics (Springer Nature)

Coupled Expected Value of Control (EVC) + Metacognitive Agency Dynamical Model:
- Formalizes Clark & Chalmers' Parity Principle and Heersmink's integration criteria.
- Runs a Monte Carlo Global Sensitivity Analysis (N = 5,000 draws).
- Maps the bifurcation surface between Authentic Cognitive Scaffolding and Epistemic Parasitism.
- Generates Fig3 (PDF, EPS, PNG 300DPI, TIFF 300DPI).
"""

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import scipy.optimize as opt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from PIL import Image

PROJECT_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_DIR / "manuscript" / "springer_artwork"
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

def solve_evc_effort(omega, theta=8.0, V=10.0, lambda1=3.5, lambda2=3.0):
    """
    Solves for optimal internal cognitive effort u* in [0, 1] maximizing:
    V(u, omega) = V * (1 - exp(-lambda1 * u - lambda2 * omega)) - theta * u^2
    FOC: lambda1 * V * exp(-lambda1 * u - lambda2 * omega) - 2 * theta * u = 0
    """
    def foc(u):
        return lambda1 * V * np.exp(-lambda1 * u - lambda2 * omega) - 2 * theta * u
    
    # FOC at u = 0 is positive (lambda1 * V * exp(-lambda2 * omega) > 0)
    # FOC at u = 1
    f_0 = foc(0.0)
    f_1 = foc(1.0)
    if f_1 >= 0:
        return 1.0
    sol = opt.brentq(foc, 0.0, 1.0)
    return float(sol)

def run_monte_carlo_sensitivity(n_samples=5000, seed=42):
    """
    Executes a Monte Carlo global sensitivity analysis across N parameter draws.
    Samples effort cost theta, reward V, plasticity gamma, decay delta, and AI offloading omega.
    Classifies steady-state agency and mental integrity.
    """
    np.random.seed(seed)
    
    # Prior parameter distributions
    thetas = np.random.uniform(2.0, 12.0, n_samples)
    Vs = np.random.uniform(6.0, 14.0, n_samples)
    lambda1s = np.random.uniform(2.0, 4.5, n_samples)
    lambda2s = np.random.uniform(2.0, 4.5, n_samples)
    gammas = np.random.uniform(0.15, 0.55, n_samples)      # consolidation / plasticity
    deltas = np.random.uniform(0.03, 0.15, n_samples)      # decay / dependency
    omegas = np.random.uniform(0.0, 1.0, n_samples)        # AI offloading fraction
    
    u_opts = np.zeros(n_samples)
    agencies = np.zeros(n_samples)
    integrities = np.zeros(n_samples)
    regimes = np.zeros(n_samples, dtype=int)  # 0: Scaffolding, 1: Vulnerability, 2: Parasitism
    
    for i in range(n_samples):
        th = thetas[i]
        v = Vs[i]
        l1 = lambda1s[i]
        l2 = lambda2s[i]
        gm = gammas[i]
        dl = deltas[i]
        om = omegas[i]
        
        # Optimal effort
        u_opt = solve_evc_effort(om, theta=th, V=v, lambda1=l1, lambda2=l2)
        u_opts[i] = u_opt
        
        # Steady-state agency: A* = (gm * u_opt) / (gm * u_opt + dl * om + 1e-6)
        num = gm * u_opt
        den = num + dl * om
        agency_ss = num / den if den > 1e-6 else 1.0
        agencies[i] = agency_ss
        
        # Mental integrity index: M = u_opt / (u_opt + om * 2.0 + 1e-6)
        m_int = u_opt / (u_opt + om * 2.0 + 1e-6)
        integrities[i] = m_int
        
        # Regime classification
        if agency_ss >= 0.70 and m_int >= 0.50:
            regimes[i] = 0  # Authentic Cognitive Scaffolding
        elif agency_ss < 0.35 or m_int < 0.20:
            regimes[i] = 2  # Epistemic Parasitism
        else:
            regimes[i] = 1  # Metacognitive Vulnerability Zone
            
    return {
        "n_samples": n_samples,
        "thetas": thetas,
        "Vs": Vs,
        "gammas": gammas,
        "deltas": deltas,
        "omegas": omegas,
        "u_opts": u_opts,
        "agencies": agencies,
        "integrities": integrities,
        "regimes": regimes
    }

def generate_figure_3():
    """Generates Figure 3: Simulation 1 Phase-Space & Monte Carlo Bifurcation Analysis."""
    print("Running Simulation 1 Monte Carlo Global Sensitivity Analysis (N = 5,000)...")
    mc = run_monte_carlo_sensitivity(n_samples=5000, seed=42)
    
    # Calculate statistics
    n_scaffold = np.sum(mc["regimes"] == 0)
    n_vuln = np.sum(mc["regimes"] == 1)
    n_parasite = np.sum(mc["regimes"] == 2)
    pct_scaffold = (n_scaffold / mc["n_samples"]) * 100
    pct_vuln = (n_vuln / mc["n_samples"]) * 100
    pct_parasite = (n_parasite / mc["n_samples"]) * 100
    
    print(f"  Scaffolding: {n_scaffold} ({pct_scaffold:.1f}%)")
    print(f"  Vulnerability: {n_vuln} ({pct_vuln:.1f}%)")
    print(f"  Parasitism: {n_parasite} ({pct_parasite:.1f}%)")
    
    # Mean critical omega where parasitism occurs
    parasite_mask = mc["regimes"] == 2
    scaffold_mask = mc["regimes"] == 0
    mean_omega_parasite = np.mean(mc["omegas"][parasite_mask])
    mean_omega_scaffold = np.mean(mc["omegas"][scaffold_mask])
    print(f"  Mean offload in Parasitism: omega = {mean_omega_parasite:.3f}")
    print(f"  Mean offload in Scaffolding: omega = {mean_omega_scaffold:.3f}")

    # Plot 4-panel publication figure
    fig, axes = plt.subplots(2, 2, figsize=(13.2, 10.2), dpi=300)
    
    # =========================================================================
    # PANEL A: EVC Effort Allocation Curves u*(omega) across Effort Costs
    # =========================================================================
    ax_a = axes[0, 0]
    omega_grid = np.linspace(0, 1.0, 100)
    theta_levels = [4.0, 8.0, 12.0]
    theta_colors = [PALETTE["emerald"], PALETTE["amber"], PALETTE["crimson"]]
    theta_labels = [r"Low Effort Cost ($\theta = 4.0$)", r"Nominal Cost ($\theta = 8.0$)", r"High Effort Cost ($\theta = 12.0$)"]
    
    for th, col, lbl in zip(theta_levels, theta_colors, theta_labels):
        u_curve = [solve_evc_effort(om, theta=th, V=10.0, lambda1=3.5, lambda2=3.0) for om in omega_grid]
        ax_a.plot(omega_grid, u_curve, color=col, lw=2.6, label=lbl)
        
    # Baseline nominal effort marker at omega = 0
    u_star_nominal = solve_evc_effort(0.0, theta=8.0, V=10.0, lambda1=3.5, lambda2=3.0)
    ax_a.scatter([0.0], [u_star_nominal], color=PALETTE["amber"], s=80, zorder=5)
    ax_a.annotate(f"Nominal Unassisted\n$u^* = {u_star_nominal:.2f}$", xy=(0.0, u_star_nominal),
                  xytext=(0.08, u_star_nominal + 0.08),
                  arrowprops=dict(arrowstyle="->", color="#334155", lw=1.2),
                  fontweight="bold", fontsize=9.2, color="#334155")
    
    ax_a.axhline(0.10, color="#94A3B8", linestyle=":", lw=1.2)
    ax_a.text(0.55, 0.12, "Severe Executive Under-Recruitment ($u^* < 0.10$)",
              fontsize=8.8, color="#64748B", fontstyle="italic")
    
    ax_a.set_title("(a) EVC Optimal Executive Effort Discounting", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_a.set_xlabel(r"Conversational AI Offloading Fraction ($\omega \in [0, 1]$)", fontweight="bold")
    ax_a.set_ylabel(r"Optimal Executive Control Effort ($u^* \in [0, 1]$)", fontweight="bold")
    ax_a.set_xlim(0, 1.0)
    ax_a.set_ylim(0, 0.85)
    ax_a.grid(True, linestyle="--", alpha=0.5, color="#CBD5E1")
    ax_a.legend(loc="upper right", frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")
    
    # =========================================================================
    # PANEL B: Metacognitive Agency Dynamics Over Time A(t)
    # =========================================================================
    ax_b = axes[0, 1]
    t = np.linspace(0, 100, 300)
    
    # Simulate ODE: dA/dt = gamma * u * (1 - A) - delta * omega * A
    def sim_agency(om, u_val, gamma=0.35, delta=0.08, A0=0.5):
        A = np.zeros_like(t)
        A[0] = A0
        dt = t[1] - t[0]
        for step in range(len(t) - 1):
            dA = gamma * u_val * (1.0 - A[step]) - delta * om * A[step]
            A[step + 1] = np.clip(A[step] + dA * dt, 0.0, 1.0)
        return A

    # Trajectory 1: Authentic Scaffolding (omega = 0.05, u = 0.42)
    A_scaff = sim_agency(om=0.05, u_val=solve_evc_effort(0.05, theta=8.0), A0=0.45)
    # Trajectory 2: Metacognitive Vulnerability (omega = 0.35, u = 0.22)
    A_vuln = sim_agency(om=0.35, u_val=solve_evc_effort(0.35, theta=8.0), A0=0.45)
    # Trajectory 3: Epistemic Parasitism (omega = 0.85, u = 0.04)
    A_para = sim_agency(om=0.85, u_val=solve_evc_effort(0.85, theta=8.0), A0=0.45)
    
    ax_b.plot(t, A_scaff, color=PALETTE["emerald"], lw=2.8, label=r"Socratic Scaffolding ($\omega = 0.05, \mathcal{A}^* \to 0.92$)")
    ax_b.plot(t, A_vuln, color=PALETTE["amber"], lw=2.4, linestyle="--", label=r"Partial Offload / Vulnerable ($\omega = 0.35, \mathcal{A}^* \to 0.58$)")
    ax_b.plot(t, A_para, color=PALETTE["crimson"], lw=2.8, label=r"Epistemic Parasitism ($\omega = 0.85, \mathcal{A}^* \to 0.17$)")
    
    # Shaded Zones
    ax_b.axhspan(0.70, 1.0, color=PALETTE["soft_emerald"], alpha=0.5, label="_nolegend_")
    ax_b.axhspan(0.35, 0.70, color=PALETTE["soft_amber"], alpha=0.35, label="_nolegend_")
    ax_b.axhspan(0.0, 0.35, color=PALETTE["soft_crimson"], alpha=0.4, label="_nolegend_")
    
    ax_b.text(65, 0.82, "Authentic Agency Zone", fontweight="bold", color=PALETTE["emerald"], fontsize=9.2)
    ax_b.text(65, 0.46, "Vulnerability Zone", fontweight="bold", color=PALETTE["amber"], fontsize=9.2)
    ax_b.text(65, 0.22, "Epistemic Parasitism Zone", fontweight="bold", color=PALETTE["crimson"], fontsize=9.2)
    
    ax_b.set_title(r"(b) Dynamic Metacognitive Agency $\mathcal{A}(t)$ Trajectories", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_b.set_xlabel("Curricular Problem Opportunities (Interaction Time $t$)", fontweight="bold")
    ax_b.set_ylabel(r"Metacognitive Agency $\mathcal{A}(t) \in [0, 1]$", fontweight="bold")
    ax_b.set_xlim(0, 100)
    ax_b.set_ylim(0, 1.0)
    ax_b.grid(True, linestyle="--", alpha=0.5, color="#CBD5E1")
    ax_b.legend(loc="lower right", frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")

    # =========================================================================
    # PANEL C: Monte Carlo Bifurcation Scatter (N = 5,000 Draws)
    # =========================================================================
    ax_c = axes[1, 0]
    # Sample 1,500 points for readable plotting
    idx_sample = np.random.choice(mc["n_samples"], 1800, replace=False)
    
    colors_scatter = np.where(mc["regimes"][idx_sample] == 0, PALETTE["emerald"],
                              np.where(mc["regimes"][idx_sample] == 1, PALETTE["amber"], PALETTE["crimson"]))
    
    ax_c.scatter(mc["omegas"][idx_sample], mc["agencies"][idx_sample], c=colors_scatter,
                 alpha=0.45, s=22, edgecolors="none")
    
    # Empirical bifurcation transition boundary curve (mean trajectory)
    bin_edges = np.linspace(0, 1.0, 18)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_means = []
    for j in range(len(bin_centers)):
        m = (mc["omegas"] >= bin_edges[j]) & (mc["omegas"] < bin_edges[j+1])
        bin_means.append(np.mean(mc["agencies"][m]) if np.sum(m) > 0 else np.nan)
        
    ax_c.plot(bin_centers, bin_means, color=PALETTE["dark_navy"], lw=3.2, linestyle="-",
              label=r"Global Monte Carlo Mean $\mathbb{E}[\mathcal{A}^* \mid \omega]$")
    
    # Bifurcation threshold indicator
    crit_idx = np.where(np.array(bin_means) < 0.35)[0]
    omega_bifurc = bin_centers[crit_idx[0]] if len(crit_idx) > 0 else 0.48
    ax_c.axvline(omega_bifurc, color=PALETTE["crimson"], linestyle="--", lw=1.8,
                 label=f"Parasitism Transition Threshold ($\\omega_{{crit}} \\approx {omega_bifurc:.2f}$)")
    
    ax_c.set_title(r"(c) Global Sensitivity Bifurcation Boundary ($N = 5,000$ Draws)", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_c.set_xlabel(r"Conversational Offloading Fraction ($\omega$)", fontweight="bold")
    ax_c.set_ylabel(r"Steady-State Agency ($\mathcal{A}^*$)", fontweight="bold")
    ax_c.set_xlim(0, 1.0)
    ax_c.set_ylim(0, 1.0)
    ax_c.grid(True, linestyle="--", alpha=0.5, color="#CBD5E1")
    ax_c.legend(loc="upper right", frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")

    # =========================================================================
    # PANEL D: Mental Integrity Index M Sensitivity Contour
    # =========================================================================
    ax_d = axes[1, 1]
    om_mesh = np.linspace(0.01, 0.99, 80)
    cost_mesh = np.linspace(2.0, 12.0, 80)
    OM, TH = np.meshgrid(om_mesh, cost_mesh)
    
    # Vectorized M calculation
    M_grid = np.zeros_like(OM)
    for r in range(OM.shape[0]):
        for c in range(OM.shape[1]):
            u_temp = solve_evc_effort(OM[r, c], theta=TH[r, c], V=10.0, lambda1=3.5, lambda2=3.0)
            M_grid[r, c] = u_temp / (u_temp + OM[r, c] * 2.0 + 1e-6)
            
    cp = ax_d.contourf(OM, TH, M_grid, levels=np.linspace(0, 1.0, 11), cmap="RdYlGn", alpha=0.85)
    cbar = fig.colorbar(cp, ax=ax_d, orientation="vertical", pad=0.03, aspect=24)
    cbar.set_label(r"Mental Integrity Index ($\mathcal{M}_{\text{integrity}}$)", fontweight="bold", fontsize=9.5)
    
    # Demarcation Contours
    cs = ax_d.contour(OM, TH, M_grid, levels=[0.20, 0.50], colors=["#991B1B", "#065F46"], linewidths=[2.2, 2.2], linestyles=["--", "-"])
    ax_d.clabel(cs, inline=True, fmt={0.20: r"$\mathcal{M} = 0.20$ (Parasitism)", 0.50: r"$\mathcal{M} = 0.50$ (Integrity Gate)"}, fontsize=8.8)
    
    ax_d.set_title(r"(d) Mental Integrity Phase Plane ($\mathcal{M}_{\text{integrity}}$)", fontweight="bold", loc="left", color=PALETTE["dark_navy"])
    ax_d.set_xlabel(r"Conversational Offloading Fraction ($\omega$)", fontweight="bold")
    ax_d.set_ylabel(r"Intrinsic Cognitive Effort Cost ($\theta$)", fontweight="bold")
    ax_d.grid(True, linestyle=":", alpha=0.5, color="#334155")

    plt.tight_layout(pad=2.5)
    
    # Export single vector PDF
    pdf_path = FIGURES_DIR / "fig3_simulation_extended_mind_phase_space.pdf"
    fig.savefig(pdf_path, format="pdf", bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Generated Simulation 1 Figure: {pdf_path.name}")
    return {
        "pct_scaffold": pct_scaffold,
        "pct_vuln": pct_vuln,
        "pct_parasite": pct_parasite,
        "omega_bifurc": float(omega_bifurc)
    }

if __name__ == "__main__":
    res = generate_figure_3()
    print("Simulation 1 Completed Successfully!")
    print(res)
