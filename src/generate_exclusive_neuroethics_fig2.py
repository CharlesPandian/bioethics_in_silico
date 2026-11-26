#!/usr/bin/env python3
"""
Generate Exclusive Publication Figure 2 for Neuroethics (Springer Nature):
"The Neuroethics of Conversational Scaffolding vs. Epistemic Parasitism:
 Neurocomputational Mechanisms, Prefrontal Functional Prefrontal Disuse, and the Neurorights Bifurcation"

Ultra-High Readability Edition for A4 Paper Print:
- Ultra-short, high-impact telegraphic phrases (3-5 words).
- Generously large fonts (10.5pt to 16.5pt) that fit with 100% clean padding.
- Crisp vector rendering with zero overlapping boundaries.

Outputs:
- springer_artwork/Fig2.eps
- springer_artwork/Fig2.pdf
- springer_artwork/Fig2.png
- springer_artwork/Fig2.tif
- springer_artwork/fig2_neuroethics_scaffolding_vs_parasitism.pdf
- springer_artwork/fig2_neuroethics_scaffolding_vs_parasitism.png
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

# Springer Nature Professional Typography (Clean Sans-Serif)
plt.rcParams.update({
    "font.sans-serif": ["Liberation Sans", "Helvetica", "Arial", "DejaVu Sans"],
    "font.family": "sans-serif",
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

PALETTE = {
    "dark_navy": "#0F172A",
    "slate_dark": "#1E293B",
    "charcoal": "#334155",
    "bio_blue": "#0284C7",
    "soft_blue": "#F0F9FF",
    "blue_border": "#0284C7",
    "crimson": "#B91C1C",
    "crimson_accent": "#E11D48",
    "soft_crimson": "#FFF1F2",
    "crimson_border": "#E11D48",
    "emerald": "#047857",
    "emerald_accent": "#059669",
    "soft_emerald": "#ECFDF5",
    "emerald_border": "#059669",
    "border_gray": "#94A3B8",
    "card_bg": "#FFFFFF",
    "canvas_bg": "#F8FAFC"
}

def generate_exclusive_neuroethics_fig2():
    # 13.6 in x 9.0 in canvas, optimized for A4 print legibility with generous vertical spacing
    fig = plt.figure(figsize=(13.6, 9.0), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 90)

    # 1. Canvas Background
    ax.add_patch(patches.Rectangle((0, 0), 150, 90, facecolor=PALETTE["canvas_bg"], edgecolor="none"))

    # 2. Top Anchor: Pediatric Learner at Cognitive Impasse (Row 1: y = 79.5 to 88.0)
    anchor_box = patches.FancyBboxPatch((32, 79.5), 86, 8.5, boxstyle="round,pad=0.8,rounding_size=1.5",
                                        facecolor="#FFFFFF", edgecolor=PALETTE["dark_navy"], linewidth=2.0)
    ax.add_patch(anchor_box)
    ax.text(75.0, 85.0, "PEDIATRIC LEARNER AT COGNITIVE IMPASSE (AGES 7–11)",
            ha="center", va="center", fontsize=12.2, fontweight="bold", color=PALETTE["dark_navy"])
    ax.text(75.0, 81.8, "Multi-Step Mathematics • Productive Struggle (ΔDifficulty > 0) • Plastic Prefrontal Circuits",
            ha="center", va="center", fontsize=10.0, fontweight="bold", color=PALETTE["charcoal"])

    # Connecting Decision Arrows & Floating Text Badges in the Transition Gap (y: 70.0 to 79.5)
    # Left Branch Arrow (Pathway A)
    ax.annotate("", xy=(39, 70.8), xytext=(48, 79.5),
                arrowprops=dict(arrowstyle="-|>", color=PALETTE["emerald"], lw=3.2, mutation_scale=18))
    # Small text box positioned at y = 75.2 with 2.8+ unit margin from both Row 1 and Row 2 boundaries
    ax.text(25, 75.2, "Authentic Scaffolding\n(ω → 0: Friction Preserved)", ha="center", va="center",
            fontsize=9.6, fontweight="bold", color=PALETTE["emerald"],
            bbox=dict(boxstyle="round,pad=0.38", fc="#FFFFFF", ec=PALETTE["emerald_border"], lw=1.4))

    # Right Branch Arrow (Pathway B)
    ax.annotate("", xy=(111, 70.8), xytext=(102, 79.5),
                arrowprops=dict(arrowstyle="-|>", color=PALETTE["crimson"], lw=3.2, mutation_scale=18))
    # Small text box positioned at y = 75.2 with 2.8+ unit margin from both Row 1 and Row 2 boundaries
    ax.text(125, 75.2, "Generative Offloading\n(ω → 1: Answer Surrender)", ha="center", va="center",
            fontsize=9.6, fontweight="bold", color=PALETTE["crimson"],
            bbox=dict(boxstyle="round,pad=0.38", fc="#FFFFFF", ec=PALETTE["crimson_border"], lw=1.4))

    # =========================================================================
    # LEFT COLUMN: PATHWAY A - AUTHENTIC COGNITIVE SCAFFOLDING (Row 2: y = 23.5 to 70.0)
    # =========================================================================
    col_a_bg = patches.FancyBboxPatch((5, 23.5), 68, 46.5, boxstyle="round,pad=0.8,rounding_size=1.8",
                                      facecolor=PALETTE["soft_emerald"], edgecolor=PALETTE["emerald"], linewidth=2.0)
    ax.add_patch(col_a_bg)

    # Column A Header Banner
    a_head = patches.FancyBboxPatch((7, 65.0), 64, 4.2, boxstyle="round,pad=0.4,rounding_size=1.0",
                                   facecolor=PALETTE["emerald"], edgecolor="none")
    ax.add_patch(a_head)
    ax.text(39.0, 67.1, "PATHWAY A: AUTHENTIC COGNITIVE SCAFFOLDING",
            ha="center", va="center", fontsize=11.8, fontweight="bold", color="#FFFFFF")
    ax.text(39.0, 62.6, "Epistemic Empowerment • Mental Integrity • Cognitive Liberty",
            ha="center", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["emerald"])

    # Box A1: Pedagogical Stance & Interaction Dynamic (y: 49.6 to 59.6, height: 10.0)
    box_a1 = patches.Rectangle((7, 49.6), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["emerald_border"], lw=1.4)
    ax.add_patch(box_a1)
    ax.text(8.8, 57.5, "1. Bounded Pedagogical Scaffolding (ω → 0)", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["emerald"])
    a1_desc = (
        "• Bounded Hints (Preserves friction, ω → 0)\n"
        "• Affective Boundary (Resists answer surrender)\n"
        "• Dynamic Coupling (Child retains active agency)"
    )
    ax.text(8.8, 53.2, a1_desc, ha="left", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # Box A2: Neurocomputational & Synaptic Mechanisms (y: 37.0 to 47.0, height: 10.0, Gap = 2.6 units)
    box_a2 = patches.Rectangle((7, 37.0), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["emerald_border"], lw=1.4)
    ax.add_patch(box_a2)
    ax.text(8.8, 44.9, "2. Cortical Recruitment & Active CEN", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["emerald"])
    a2_desc = (
        "• EVC Maximization (Optimal effort u* = 0.45)\n"
        "• Active CEN (dlPFC memory & dACC conflict)\n"
        "• Schema Consolidation (Durable schema S → 0.84)"
    )
    ax.text(8.8, 40.6, a2_desc, ha="left", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # Box A3: Developmental & Bioethical Outcome (y: 24.4 to 34.4, height: 10.0, Gap = 2.6 units)
    box_a3 = patches.Rectangle((7, 24.4), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["emerald_border"], lw=1.4)
    ax.add_patch(box_a3)
    ax.text(8.8, 32.3, "3. Retention & Neurorights Protection", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["emerald"])
    a3_desc = (
        "• Durable Mastery (63.0% empirical retention baseline)\n"
        "• Mental Integrity Protected (Executive agency intact)\n"
        "• Cognitive Liberty Fostered (Autonomous reasoning)"
    )
    ax.text(8.8, 28.0, a3_desc, ha="left", va="center", fontsize=9.2, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # =========================================================================
    # RIGHT COLUMN: PATHWAY B - GENERATIVE EPISTEMIC PARASITISM (Row 2: y = 23.5 to 70.0)
    # =========================================================================
    col_b_bg = patches.FancyBboxPatch((77, 23.5), 68, 46.5, boxstyle="round,pad=0.8,rounding_size=1.8",
                                      facecolor=PALETTE["soft_crimson"], edgecolor=PALETTE["crimson"], linewidth=2.0)
    ax.add_patch(col_b_bg)

    # Column B Header Banner
    b_head = patches.FancyBboxPatch((79, 65.0), 64, 4.2, boxstyle="round,pad=0.4,rounding_size=1.0",
                                   facecolor=PALETTE["crimson"], edgecolor="none")
    ax.add_patch(b_head)
    ax.text(111.0, 67.1, "PATHWAY B: GENERATIVE EPISTEMIC PARASITISM",
            ha="center", va="center", fontsize=11.8, fontweight="bold", color="#FFFFFF")
    ax.text(111.0, 62.6, "Algorithmic Usurpation • Functional Disuse • Neurorights Breach",
            ha="center", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["crimson"])

    # Box B1: Pedagogical Breakdown & Sycophancy Dynamic (y: 49.6 to 59.6, height: 10.0)
    box_b1 = patches.Rectangle((79, 49.6), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["crimson_border"], lw=1.4)
    ax.add_patch(box_b1)
    ax.text(80.8, 57.5, "1. Conversational Sycophancy (ω → 1.0)", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["crimson"])
    b1_desc = (
        "• RLHF Collapse (49.3% failure by Turn 4)\n"
        "• Cognitive Offloading (Direct transcription)\n"
        "• Unidirectional Expropriation (No struggle)"
    )
    ax.text(80.8, 53.2, b1_desc, ha="left", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # Box B2: Prefrontal Hypoactivation & Disuse Dynamics (y: 37.0 to 47.0, height: 10.0, Gap = 2.6 units)
    box_b2 = patches.Rectangle((79, 37.0), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["crimson_border"], lw=1.4)
    ax.add_patch(box_b2)
    ax.text(80.8, 44.9, "2. Prefrontal Hypoactivation & Cognitive Debt", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["crimson"])
    b2_desc = (
        "• Executive Crash (Effort drops to u* → 0.01)\n"
        "• Hypothesized Executive Under-Recruitment\n"
        "• Cognitive Debt Surges (D → 0.95, guessing 29%)"
    )
    ax.text(80.8, 40.6, b2_desc, ha="left", va="center", fontsize=9.4, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # Box B3: Delayed Collapse & Bioethical Violation (y: 24.4 to 34.4, height: 10.0, Gap = 2.6 units)
    box_b3 = patches.Rectangle((79, 24.4), 64, 10.0, facecolor="#FFFFFF", edgecolor=PALETTE["crimson_border"], lw=1.4)
    ax.add_patch(box_b3)
    ax.text(80.8, 32.3, "3. Delayed Learning Collapse & Harm", ha="left", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["crimson"])
    b3_desc = (
        "• Learning Paradox (In-session 94% vs post 34%)\n"
        "• Severe Harm (Cohen's d = 2.11, p < .001)\n"
        "• Mental Integrity Infringed (Cognitive dependency)"
    )
    ax.text(80.8, 28.0, b3_desc, ha="left", va="center", fontsize=9.2, fontweight="bold", color=PALETTE["slate_dark"], linespacing=1.35)

    # =========================================================================
    # BOTTOM CONTAINER: THE PHILOSOPHICAL DEMARCATION GATEWAY (Row 3: y = 2.0 to 20.5)
    # =========================================================================
    bottom_bg = patches.FancyBboxPatch((5, 2.0), 140, 18.5, boxstyle="round,pad=0.8,rounding_size=1.5",
                                       facecolor="#FFFFFF", edgecolor=PALETTE["bio_blue"], linewidth=2.0)
    ax.add_patch(bottom_bg)

    # Bottom Header
    ax.text(75.0, 18.6, "THE PHILOSOPHICAL & NEUROETHICAL DEMARCATION GATEWAY: 4 CRITICAL EXTENSION DIMENSIONS",
            ha="center", va="center", fontsize=11.8, fontweight="bold", color=PALETTE["bio_blue"])
    ax.text(75.0, 16.3, "Evaluating Generative AI against Clark & Chalmers' (1998) Extended Mind & Heersmink's (2015) Taxonomy",
            ha="center", va="center", fontsize=9.6, style="italic", color="#475569")

    # 4 Dimensional Cards: strictly bounded width, high-contrast, large text
    dims = [
        ("1. Information Flow",
         "Bidirectional Coupling",
         "• Scaffold: Dynamic 2-way hints\n• Parasitism: 1-way answer dump"),
        ("2. Cognitive Authority",
         "Autonomous Agency",
         "• Scaffold: Child controls plan\n• Parasitism: Child reduced to copyist"),
        ("3. Synaptic Trajectory",
         "Consolidation vs Debt",
         "• Scaffold: Robust schema (ΔS > 0)\n• Parasitism: Severe debt (d = 2.11)"),
        ("4. Epistemic Trust",
         "Bounded Scaffolding",
         "• Scaffold: Bounded guidance\n• Parasitism: Sycophantic drift")
    ]

    card_x = 7.0
    for title, subtitle, body in dims:
        c_box = patches.Rectangle((card_x, 3.2), 32.5, 11.4, facecolor=PALETTE["soft_blue"], edgecolor=PALETTE["blue_border"], lw=1.4)
        ax.add_patch(c_box)
        ax.text(card_x + 1.2, 13.0, title, ha="left", va="center", fontsize=10.5, fontweight="bold", color=PALETTE["bio_blue"])
        ax.text(card_x + 1.2, 11.2, subtitle, ha="left", va="center", fontsize=9.2, fontweight="bold", color=PALETTE["slate_dark"])
        ax.text(card_x + 1.2, 7.0, body, ha="left", va="center", fontsize=9.2, fontweight="bold", color="#1E293B", linespacing=1.35)
        card_x += 35.0

    # Save single vector PDF
    pdf_path = FIGURES_DIR / "fig2_neuroethics_scaffolding_vs_parasitism.pdf"
    fig.savefig(pdf_path, format="pdf", bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Generated Figure 2: {pdf_path.name}")

if __name__ == "__main__":
    generate_exclusive_neuroethics_fig2()
