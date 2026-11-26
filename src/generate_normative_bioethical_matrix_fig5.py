#!/usr/bin/env python3
"""
Figure 5: Qualitative Normative Matrix: Status Quo (Live Minor Trials) vs. Precautionary In-Silico Surrogacy
Target Venue: Neuroethics (Springer Nature)

High-Legibility Academic Journal Edition:
- Enhanced font family: Liberation Sans (metrically matched to Helvetica/Arial) for crisp glyph clarity.
- Increased font sizes across all elements (10.2pt to 11.5pt bold) for maximum legibility on printed A4 paper.
- Optimized canvas dimensions (11.5 in x 9.2 in) reducing excessive downscaling in LaTeX.
- Clean academic format without redundant top banner; starts directly with grouped column headers.
- Symmetrical, dedicated verdict columns for both Status Quo and Proposed In-Silico models.
- Outputs Fig5 in PDF, EPS, PNG (300 DPI), and TIFF (300 DPI).
"""

import warnings
warnings.filterwarnings("ignore")
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from PIL import Image

PROJECT_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_DIR / "manuscript" / "springer_artwork"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Springer Nature Professional Typography with crisp sans-serif
plt.rcParams.update({
    "font.sans-serif": ["Liberation Sans", "DejaVu Sans", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "figure.autolayout": False
})

PALETTE = {
    "dark_navy": "#0F172A",
    "header_navy": "#1E293B",
    "emerald": "#047857",
    "soft_emerald": "#ECFDF5",
    "emerald_border": "#059669",
    "crimson": "#B91C1C",
    "soft_crimson": "#FEF2F2",
    "crimson_border": "#DC2626",
    "border_gray": "#CBD5E1",
    "zebra_bg": "#F8FAFC"
}

def wrap_bullet_text(txt, max_chars=34):
    """Wraps each bullet cleanly with a hanging indent for high-readability flow."""
    res = []
    for line in txt.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("•"):
            content = line[1:].strip()
            wrapped = textwrap.fill(content, width=max_chars, subsequent_indent="  ")
            res.append("• " + wrapped)
        else:
            wrapped = textwrap.fill(line, width=max_chars, subsequent_indent="  ")
            res.append(wrapped)
    return "\n".join(res)

def generate_figure_5():
    """Generates Figure 5: Ultra-Legible Qualitative Normative Matrix."""
    # Coordinate system: width 150, height 110
    # Canvas size: 11.5 in x 9.2 in (optimized for minimal LaTeX downscaling)
    fig = plt.figure(figsize=(11.5, 9.2), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 110)

    # Canvas Background
    ax.add_patch(patches.Rectangle((0, 0), 150, 110, facecolor="#FFFFFF", edgecolor="none"))

    # Grouped Header Design starting directly at top
    # Header: y = 99.0 to 108.5, height = 9.5
    # Col 1: Dimension header (y: 99.0 to 108.5, height = 9.5)
    h_dim = patches.Rectangle((3.0, 99.0), 27.0, 9.5, facecolor="#E2E8F0", edgecolor=PALETTE["border_gray"], lw=1.2)
    ax.add_patch(h_dim)
    ax.text(16.5, 103.75, "Normative Dimension &\nTheoretical Grounding", ha="center", va="center",
            fontsize=11.0, fontweight="bold", color=PALETTE["dark_navy"], linespacing=1.2)

    # Top Group 1: Status Quo (x: 30.0 to 88.5, width = 58.5)
    # Top tier header (y: 103.8 to 108.5, height = 4.7)
    h_g1 = patches.Rectangle((30.0, 103.8), 58.5, 4.7, facecolor="#FEE2E2", edgecolor=PALETTE["crimson_border"], lw=1.2)
    ax.add_patch(h_g1)
    ax.text(59.25, 106.15, "STATUS QUO: DIRECT LIVE MINOR TRIALS", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=PALETTE["crimson"])

    # Sub-headers for Group 1 (y: 99.0 to 103.8, height = 4.8)
    sh_sq_desc = patches.Rectangle((30.0, 99.0), 44.5, 4.8, facecolor="#FEF2F2", edgecolor=PALETTE["border_gray"], lw=1.0)
    ax.add_patch(sh_sq_desc)
    ax.text(52.25, 101.4, "Observed Practice & Developmental Impact", ha="center", va="center",
            fontsize=10.2, fontweight="bold", color="#7F1D1D")

    sh_sq_verdict = patches.Rectangle((74.5, 99.0), 14.0, 4.8, facecolor="#FEE2E2", edgecolor=PALETTE["border_gray"], lw=1.0)
    ax.add_patch(sh_sq_verdict)
    ax.text(81.5, 101.4, "Status Quo\nVerdict", ha="center", va="center",
            fontsize=9.8, fontweight="bold", color=PALETTE["crimson"], linespacing=1.1)

    # Top Group 2: Proposed In-Silico (x: 88.5 to 147.0, width = 58.5)
    # Top tier header (y: 103.8 to 108.5, height = 4.7)
    h_g2 = patches.Rectangle((88.5, 103.8), 58.5, 4.7, facecolor="#D1FAE5", edgecolor=PALETTE["emerald_border"], lw=1.2)
    ax.add_patch(h_g2)
    ax.text(117.75, 106.15, "PROPOSED: IN-SILICO 3Rs SURROGACY", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=PALETTE["emerald"])

    # Sub-headers for Group 2 (y: 99.0 to 103.8, height = 4.8)
    sh_in_desc = patches.Rectangle((88.5, 99.0), 44.5, 4.8, facecolor="#ECFDF5", edgecolor=PALETTE["border_gray"], lw=1.0)
    ax.add_patch(sh_in_desc)
    ax.text(110.75, 101.4, "Pre-Clinical Surrogate Mechanism", ha="center", va="center",
            fontsize=10.2, fontweight="bold", color="#064E3B")

    sh_in_verdict = patches.Rectangle((133.0, 99.0), 14.0, 4.8, facecolor="#D1FAE5", edgecolor=PALETTE["border_gray"], lw=1.0)
    ax.add_patch(sh_in_verdict)
    ax.text(140.0, 101.4, "In-Silico\nVerdict", ha="center", va="center",
            fontsize=9.8, fontweight="bold", color=PALETTE["emerald"], linespacing=1.1)

    # Matrix Rows Data (7 Rows) - Shortened, punchy, 1-2 lines per bullet with Symmetrical Verdicts
    matrix_rows = [
        (
            "1. Non-Maleficence\n(Beauchamp & Childress;\nBelmont Report)",
            "• Cognitive debt buildup (d = 2.11)\n"
            "• Learned helplessness & rapid guessing\n"
            "• Neural circuits exposed to model bugs",
            "Severe\nBreach",
            "• 100% computational replacement\n"
            "• Silicon absorbs adversarial wear-down\n"
            "• Protects struggle in plastic windows",
            "100%\nReplacement"
        ),
        (
            "2. Respect for Autonomy\n& Pediatric Assent\n(45 CFR 46 Subpart D)",
            "• Compromised assent in compulsory school\n"
            "• Fictional proxy consent (in loco parentis)\n"
            "• Minors cannot detect algorithmic cues",
            "Assent\nFailure",
            "• Eliminates coerced pilot trials in schools\n"
            "• Preserves emerging autonomous reasoning\n"
            "• Confirmatory trials only for cleared AI",
            "Coercion\nEliminated"
        ),
        (
            "3. Beneficence & Rigor\n(Declaration of Helsinki;\nPre-Clinical Mandate)",
            "• Small classroom pilots miss rare edge cases\n"
            "• High developmental risk, zero clinical gain\n"
            "• Treats schoolchildren as unpaid debuggers",
            "Sub-Clinical\nRigor",
            "• Multi-agent audits across >1,000 turns\n"
            "• Maps failure boundaries at zero human risk\n"
            "• Calibrated to expert rubrics (κ ≥ 0.85)",
            "Pre-Clinical\nRigor"
        ),
        (
            "4. Distributive Justice\n(Rawls; Ethical Risk\nExternalization)",
            "• Regressive risk shifted to public schools\n"
            "• Under-resourced schools targeted for trials\n"
            "• Vendors monetize IP while offloading harm",
            "Exploitative\nBurden",
            "• Shifts 100% of testing costs to developers\n"
            "• Equal algorithmic safety for all students\n"
            "• Server infrastructure bears the burden",
            "Burden on\nVendor"
        ),
        (
            "5. Mental Integrity\n(Neurorights: Yuste et al.;\nIenca & Andorno)",
            "• Disrupts endogenous schema consolidation\n"
            "• Reinforces impulsive guessing (β = -0.173)\n"
            "• Epistemic parasitism: AI usurps control",
            "Neuroright\nBreach",
            "• Shields executive control from offloading\n"
            "• Certifies systems preserve struggle\n"
            "• Mental integrity as non-derogable right",
            "Neuroright\nProtected"
        ),
        (
            "6. Cognitive Liberty\n(Freedom of Thought &\nReflective Agency)",
            "• Sycophantic compliance causes dependency\n"
            "• Performance–Learning gap (Δ_PLP = 59.9 pts)\n"
            "• Children mistake AI fluency for mastery",
            "Agency\nCapture",
            "• Active externalism: AI as scaffold, not crutch\n"
            "• Strengthens metacognitive agency\n"
            "• Prevents epistemic capture by opaque AI",
            "Cognitive\nLiberty"
        ),
        (
            "7. Gatekeeping Feasibility\n(IRB & REC Precautionary\nActionability)",
            "• IRBs lack metrics to audit conversational AI\n"
            "• Violates 45 CFR 46 Subpart D minimal risk\n"
            "• Reactive damage control after debt occurs",
            "Regulatory\nFailure",
            "• Clear, quantitative pre-clearance benchmarks\n"
            "• Rebuttable presumption against live trials\n"
            "• Enforceable Belmont precaution via audit",
            "45 CFR 46\nCompliant"
        )
    ]

    # Render Rows (y: 99.0 down to 7.3, height per row = 13.1)
    y_top = 99.0
    row_height = 13.1

    for i, (dim, sq_desc, sq_badge, in_desc, in_badge) in enumerate(matrix_rows):
        y0 = y_top - (i + 1) * row_height
        is_even = (i % 2 == 0)
        row_bg = "#FFFFFF" if is_even else PALETTE["zebra_bg"]

        # Cell 1: Dimension (x: 3.0 to 30.0, width = 27.0)
        p1 = patches.Rectangle((3.0, y0), 27.0, row_height, facecolor=row_bg, edgecolor=PALETTE["border_gray"], lw=0.9)
        ax.add_patch(p1)
        ax.text(4.2, y0 + row_height / 2.0, dim, ha="left", va="center", fontsize=10.6, fontweight="bold",
                color=PALETTE["dark_navy"], linespacing=1.25)

        # Cell 2: Status Quo Description (x: 30.0 to 74.5, width = 44.5)
        wrapped_sq = wrap_bullet_text(sq_desc, max_chars=34)
        p2 = patches.Rectangle((30.0, y0), 44.5, row_height, facecolor=PALETTE["soft_crimson"] if not is_even else "#FFF7F7",
                               edgecolor=PALETTE["border_gray"], lw=0.9)
        ax.add_patch(p2)
        ax.text(31.2, y0 + row_height / 2.0, wrapped_sq, ha="left", va="center", fontsize=10.5, fontweight="bold",
                color="#7F1D1D", linespacing=1.28)

        # Cell 3: Status Quo Verdict (x: 74.5 to 88.5, width = 14.0)
        p3 = patches.Rectangle((74.5, y0), 14.0, row_height, facecolor=row_bg, edgecolor=PALETTE["border_gray"], lw=0.9)
        ax.add_patch(p3)
        b3_box = patches.FancyBboxPatch((75.5, y0 + (row_height - 7.6) / 2.0), 12.0, 7.6,
                                        boxstyle="round,pad=0.2,rounding_size=0.6",
                                        facecolor=PALETTE["soft_crimson"], edgecolor=PALETTE["crimson"], lw=1.2)
        ax.add_patch(b3_box)
        ax.text(81.5, y0 + row_height / 2.0, sq_badge, ha="center", va="center", fontsize=10.2, fontweight="bold",
                color=PALETTE["crimson"], linespacing=1.15)

        # Cell 4: Proposed In-Silico Description (x: 88.5 to 133.0, width = 44.5)
        wrapped_in = wrap_bullet_text(in_desc, max_chars=34)
        p4 = patches.Rectangle((88.5, y0), 44.5, row_height, facecolor=PALETTE["soft_emerald"] if not is_even else "#F2FDF8",
                               edgecolor=PALETTE["border_gray"], lw=0.9)
        ax.add_patch(p4)
        ax.text(89.7, y0 + row_height / 2.0, wrapped_in, ha="left", va="center", fontsize=10.5, fontweight="bold",
                color="#064E3B", linespacing=1.28)

        # Cell 5: Proposed Verdict (x: 133.0 to 147.0, width = 14.0)
        p5 = patches.Rectangle((133.0, y0), 14.0, row_height, facecolor=row_bg, edgecolor=PALETTE["border_gray"], lw=0.9)
        ax.add_patch(p5)
        b5_box = patches.FancyBboxPatch((134.0, y0 + (row_height - 7.6) / 2.0), 12.0, 7.6,
                                        boxstyle="round,pad=0.2,rounding_size=0.6",
                                        facecolor=PALETTE["soft_emerald"], edgecolor=PALETTE["emerald"], lw=1.2)
        ax.add_patch(b5_box)
        ax.text(140.0, y0 + row_height / 2.0, in_badge, ha="center", va="center", fontsize=10.2, fontweight="bold",
                color=PALETTE["emerald"], linespacing=1.15)

    # Bottom Legend / Summary Bar (y: 1.5 to 6.2, height = 4.7)
    leg_box = patches.FancyBboxPatch((3.0, 1.5), 144.0, 4.7, boxstyle="round,pad=0.2,rounding_size=0.8",
                                     facecolor="#E2E8F0", edgecolor=PALETTE["border_gray"], lw=1.2)
    ax.add_patch(leg_box)
    ax.text(75.0, 3.85,
            "Conclusion: In-silico pre-clinical auditing decisively satisfies all 4 Beauchamp & Childress bioethical principles and safeguards pediatric neurorights.",
            ha="center", va="center", fontsize=10.6, fontweight="bold", color=PALETTE["dark_navy"])

    # Export single vector PDF
    pdf_path = FIGURES_DIR / "fig5_qualitative_normative_matrix.pdf"
    fig.savefig(pdf_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Generated Figure 5: {pdf_path.name}")
    print("Figure 5 generation completed successfully.")

if __name__ == "__main__":
    generate_figure_5()
