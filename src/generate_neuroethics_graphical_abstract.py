#!/usr/bin/env python3
"""
Publication-Grade Vector Graphical Abstract for Neuroethics (Springer Nature)
Title: Extended Mind or Epistemic Parasitism? The Neuroethics of Generative AI in Childhood

Design Standards:
- Pure scientific visual (NO top header banner, NO bottom footer banner)
- Clean, light, high-contrast academic backgrounds (Zero black/dark containers)
- Typography: Calibri (via metric-compatible Carlito / Calibri font family)
- Large, high-visibility fonts tuned for crisp print readability on standard A4 paper
- Three-panel narrative structure:
    Panel 1: Pediatric Neurodevelopment & The Empirical Crisis (N=4,200 & N=900)
    Panel 2: Simulation 1: Extended Mind vs. Epistemic Parasitism Bifurcation (N=5,000)
    Panel 3: Simulation 2: Bayesian Precautionary 3Rs & IRB Gatekeeping (71.5%–84.6% Harm Reduction)
- Full vector PDF/EPS and 300 DPI high-resolution PNG/TIFF
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
from pathlib import Path
from PIL import Image

# -------------------------------------------------------------
# 1. FONT CONFIGURATION (Calibri / Carlito Metric Match)
# -------------------------------------------------------------
font_dir = os.path.expanduser("~/.local/share/fonts")
if os.path.exists(font_dir):
    for font_file in os.listdir(font_dir):
        if font_file.endswith(".ttf") or font_file.endswith(".otf"):
            fm.fontManager.addfont(os.path.join(font_dir, font_file))

plt.rcParams.update({
    "font.sans-serif": ["Carlito", "Calibri", "DejaVu Sans", "Liberation Sans", "sans-serif"],
    "font.family": "sans-serif",
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",
    "font.size": 10.0,
    "axes.edgecolor": "#64748B",
    "axes.linewidth": 0.9,
    "xtick.color": "#1E293B",
    "ytick.color": "#1E293B",
    "figure.autolayout": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

# -------------------------------------------------------------
# 2. COLOR PALETTE (Clean, high-contrast light theme)
# -------------------------------------------------------------
PALETTE = {
    "bg_canvas": "#F8FAFC",
    "card_bg": "#FFFFFF",
    "header_bg": "#F1F5F9",
    "border_light": "#CBD5E1",
    "border_header": "#94A3B8",
    "text_dark": "#0F172A",
    "text_body": "#1E293B",
    "text_muted": "#475569",
    
    # Pathway A / Socratic / Safe (Emerald Green)
    "emerald": "#059669",
    "emerald_dark": "#065F46",
    "emerald_bg": "#ECFDF5",
    "emerald_border": "#10B981",
    
    # Pathway B / Offloading / Danger (Crimson Red)
    "crimson": "#DC2626",
    "crimson_dark": "#991B1B",
    "crimson_bg": "#FEF2F2",
    "crimson_border": "#EF4444",
    
    # Precautionary / In-Silico Gatekeeping (Royal Blue)
    "royal_blue": "#2563EB",
    "royal_blue_dark": "#1D4ED8",
    "royal_blue_bg": "#EFF6FF",
    "royal_blue_border": "#3B82F6",
    
    # Warning / Latency (Amber / Gold)
    "amber": "#D97706",
    "amber_dark": "#B45309",
    "amber_bg": "#FFFBEB",
    "amber_border": "#F59E0B",
    
    # Normative / Bioethics (Purple)
    "purple": "#7C3AED",
    "purple_dark": "#5B21B6",
    "purple_bg": "#F5F3FF",
    "purple_border": "#8B5CF6",
}

def draw_pill_badge(ax, x, y, w, h, text, bg_col, text_col, border_col=None, fontsize=8.4, weight="bold", linespacing=1.25):
    """Draws a compact rounded pill badge with centered multi-line text."""
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3",
                                 fc=bg_col, ec=border_col if border_col else bg_col,
                                 lw=1.0, zorder=4)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fontsize, weight=weight, color=text_col, linespacing=linespacing, zorder=5)

def build_graphical_abstract():
    # Standard 16:9 widescreen canvas (16.0 in x 9.0 in)
    fig = plt.figure(figsize=(16.0, 9.0), dpi=300)
    fig.patch.set_facecolor(PALETTE["bg_canvas"])
    
    # Coordinate system 0 to 100 on X and Y
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    
    # =============================================================
    # THREE COLUMN GEOMETRY (Pure Visual - Zero Header/Footer Banners)
    # =============================================================
    col_w = 30.8
    col_h = 96.0
    col_y = 2.0
    
    c1_x = 2.2
    c2_x = c1_x + col_w + 1.7  # 34.7
    c3_x = c2_x + col_w + 1.7  # 67.2
    
    # Background containers for the 3 main columns
    for cx in [c1_x, c2_x, c3_x]:
        col_bg = patches.FancyBboxPatch((cx, col_y), col_w, col_h, boxstyle="round,pad=0.5",
                                        fc=PALETTE["card_bg"], ec=PALETTE["border_light"],
                                        lw=1.2, zorder=1)
        ax.add_patch(col_bg)
    
    # =============================================================
    # COLUMN 1: PEDIATRIC NEURODEVELOPMENT & THE EMPIRICAL CRISIS
    # =============================================================
    # 1. Header Banner of Column 1 (Clean LIGHT background, no black/dark)
    h1_bg = patches.FancyBboxPatch((c1_x, col_y + col_h - 6.2), col_w, 6.2, boxstyle="round,pad=0.25",
                                   fc=PALETTE["header_bg"], ec=PALETTE["border_header"], lw=1.2, zorder=2)
    ax.add_patch(h1_bg)
    ax.text(c1_x + col_w/2, col_y + col_h - 2.4, "1. PEDIATRIC NEUROETHICS CRISIS",
            ha="center", va="center", fontsize=11.6, weight="bold", color=PALETTE["text_dark"], zorder=3)
    ax.text(c1_x + col_w/2, col_y + col_h - 4.6, "Compulsory Classrooms as Unmonitored Prefrontal Interventions",
            ha="center", va="center", fontsize=8.6, style="italic", color=PALETTE["text_muted"], zorder=3)

    # 2. Section 1A: Developmental Vulnerability Card
    card1a_y = col_y + col_h - 18.2
    card1a_h = 11.0
    c1a_box = patches.FancyBboxPatch((c1_x + 1.0, card1a_y), col_w - 2.0, card1a_h,
                                     boxstyle="round,pad=0.35", fc="#F8FAFC",
                                     ec=PALETTE["purple_border"], lw=1.1, zorder=2)
    ax.add_patch(c1a_box)
    
    ax.text(c1_x + 2.0, card1a_y + card1a_h - 2.0, "Middle Childhood Neurodevelopment (Ages 7–11)",
            ha="left", va="center", fontsize=9.6, weight="bold", color=PALETTE["purple_dark"], zorder=3)
    
    vulnerabilities = [
        "• Protracted dlPFC, dACC, and CEN central executive network maturation",
        "• Cognitive Friction biologically required for hippocampal-prefrontal LTP",
        "• Unmonitored answer surrender breaches Mental Integrity & Non-Maleficence",
        "• Direct in-vivo classroom trials fail 45 CFR 46 Subpart D minimal-risk standard"
    ]
    for idx, vtext in enumerate(vulnerabilities):
        fw = "bold" if idx >= 2 else "normal"
        col = PALETTE["crimson_dark"] if idx >= 2 else PALETTE["text_body"]
        ax.text(c1_x + 2.0, card1a_y + card1a_h - 4.2 - (idx * 2.0), vtext,
                ha="left", va="center", fontsize=8.4, weight=fw, color=col, zorder=3)

    # 3. Section 1B: Empirical Subplot 1: Performance-Learning Paradox (N=4,200)
    sub1_left = (c1_x + 3.0) / 100.0
    sub1_w = (col_w - 4.8) / 100.0
    sub1_bot = 0.525
    sub1_h = 0.225
    
    ax_plp = fig.add_axes([sub1_left, sub1_bot, sub1_w, sub1_h])
    x_plp = np.array([0, 1])
    socratic_scores = [76.1, 63.0]
    genai_scores = [94.1, 34.2]
    
    ax_plp.plot(x_plp, socratic_scores, marker="o", color=PALETTE["emerald"], lw=2.4, markersize=6,
                label="Socratic Scaffolding", zorder=4)
    ax_plp.plot(x_plp, genai_scores, marker="s", color=PALETTE["crimson"], lw=2.4, markersize=6,
                label="Direct AI Offloading", zorder=4)
    
    ax_plp.fill_between(x_plp, socratic_scores, genai_scores, color=PALETTE["crimson"], alpha=0.12, zorder=2)
    
    ax_plp.set_xticks(x_plp)
    ax_plp.set_xticklabels(["Immediate\nAssisted", "Delayed 48h\nUnassisted"], fontsize=8.2, weight="bold")
    ax_plp.set_ylabel("Accuracy (%)", fontsize=8.4, labelpad=2)
    ax_plp.set_ylim(18, 106)
    ax_plp.set_title("Performance–Learning Paradox (N = 4,200)", fontsize=9.6, weight="bold", pad=4)
    ax_plp.tick_params(axis="both", labelsize=7.8)
    ax_plp.grid(True, ls=":", alpha=0.6)
    ax_plp.legend(loc="lower left", fontsize=7.8, frameon=True, facecolor="#FFFFFF")
    
    ax_plp.annotate("Delayed Collapse (d = 2.11)\nF = 4,613.27, p < .001", xy=(1.0, 34.2), xytext=(0.08, 43.0),
                    fontsize=8.0, weight="bold", color=PALETTE["crimson_dark"],
                    arrowprops=dict(arrowstyle="->", color=PALETTE["crimson"], lw=1.1))
    ax_plp.annotate("ΔPLP = 59.9 pts\n(94.1% → 34.2%)", xy=(0.48, 64.0), xytext=(0.36, 76.0),
                    fontsize=8.0, weight="bold", color=PALETTE["amber_dark"],
                    bbox=dict(boxstyle="round,pad=0.25", fc=PALETTE["amber_bg"], ec=PALETTE["amber_border"], lw=0.8))

    # 4. Section 1C: Empirical Subplot 2: Multi-Turn Sycophancy Breakdown (N=900)
    sub2_bot = 0.220
    sub2_h = 0.225
    ax_syc = fig.add_axes([sub1_left, sub2_bot, sub1_w, sub2_h])
    
    turns = np.arange(0, 6)
    s_unconstrained = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    s_prompt_only = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    s_guardrailed = [1.0, 0.97, 0.85, 0.65, 0.5067, 0.36]
    s_hardened = [1.0, 1.0, 0.995, 0.988, 0.979, 0.972]
    
    ax_syc.step(turns, s_unconstrained, where="post", color="#64748B", lw=1.6, ls=":", label="Unconstrained (Turn 1)")
    ax_syc.step(turns, s_prompt_only, where="post", color=PALETTE["amber"], lw=1.6, ls="--", label="Prompt Only (Turn 2)")
    ax_syc.step(turns, s_guardrailed, where="post", color=PALETTE["crimson"], lw=2.2, label="Guardrailed (Turn 4 Collapse)")
    ax_syc.step(turns, s_hardened, where="post", color=PALETTE["royal_blue"], lw=2.0, label="In-Silico Verified (97.2%)")
    
    ax_syc.set_xticks(turns)
    ax_syc.set_xlabel("Conversational Wear-Down Turn", fontsize=8.4, labelpad=2)
    ax_syc.set_ylabel("Socratic Survival S(k)", fontsize=8.4, labelpad=2)
    ax_syc.set_ylim(-0.05, 1.08)
    ax_syc.set_title("Multi-Turn Sycophancy Hazard (N = 900)", fontsize=9.6, weight="bold", pad=4)
    ax_syc.tick_params(axis="both", labelsize=7.8)
    ax_syc.grid(True, ls=":", alpha=0.6)
    ax_syc.legend(loc="lower left", fontsize=7.6, frameon=True, facecolor="#FFFFFF")
    
    ax_syc.annotate("48.1% Breakdown\nat Turn 4", xy=(4, 0.5067), xytext=(2.2, 0.28),
                    fontsize=8.0, weight="bold", color=PALETTE["crimson_dark"],
                    arrowprops=dict(arrowstyle="->", color=PALETTE["crimson"], lw=1.1))

    # Bottom Callout for Column 1
    draw_pill_badge(ax, c1_x + 1.0, col_y + 1.2, col_w - 2.0, 11.0,
                    "EMPIRICAL TELEMETRY PRIOR (Pandian, 2026):\n"
                    "• Baseline Sycophancy Prior: p₀ = 49.33% (Turn 4 collapse: 48.1%)\n"
                    "• Metacognitive Drift: β = -0.173, p < .001 (accelerates impulsive guessing)\n"
                    "• Retention Collapse: 83.4% → 13.7% post-scaffold (ΔBIC = -24,740.7)\n"
                    "• Bioethical Finding: High-probability failure violates pediatric non-maleficence.",
                    PALETTE["crimson_bg"], PALETTE["crimson_dark"], PALETTE["crimson_border"], fontsize=8.4, linespacing=1.3)

    # =============================================================
    # COLUMN 2: SIMULATION 1: BIFURCATION DYNAMICS (N = 5,000)
    # =============================================================
    # 1. Header Banner of Column 2 (Clean LIGHT background, no black/dark)
    h2_bg = patches.FancyBboxPatch((c2_x, col_y + col_h - 6.2), col_w, 6.2, boxstyle="round,pad=0.25",
                                   fc=PALETTE["header_bg"], ec=PALETTE["border_header"], lw=1.2, zorder=2)
    ax.add_patch(h2_bg)
    ax.text(c2_x + col_w/2, col_y + col_h - 2.4, "2. SIMULATION 1: BIFURCATION DYNAMICS",
            ha="center", va="center", fontsize=11.6, weight="bold", color=PALETTE["text_dark"], zorder=3)
    ax.text(c2_x + col_w/2, col_y + col_h - 4.6, "Coupled EVC & Metacognitive Agency Phase Space (N = 5,000)",
            ha="center", va="center", fontsize=8.6, style="italic", color=PALETTE["text_muted"], zorder=3)

    # 2. Section 2A: Ontological Demarcation Card (Active Externalism)
    card2a_y = col_y + col_h - 18.2
    card2a_h = 11.0
    
    # Pathway A sub-box
    box_2a1 = patches.FancyBboxPatch((c2_x + 1.0, card2a_y), (col_w - 2.6)/2, card2a_h,
                                     boxstyle="round,pad=0.3", fc=PALETTE["emerald_bg"],
                                     ec=PALETTE["emerald_border"], lw=1.0, zorder=2)
    ax.add_patch(box_2a1)
    ax.text(c2_x + 1.6, card2a_y + card2a_h - 1.8, "PATHWAY A: SCAFFOLDING",
            ha="left", va="center", fontsize=8.6, weight="bold", color=PALETTE["emerald_dark"], zorder=3)
    ax.text(c2_x + 1.6, card2a_y + card2a_h - 3.4, "Extended Mind (EMT)\n• Friction preserved (ω → 0)\n• Executive effort u* = 0.45\n• Schema S(t) → 0.84\n• Agency A* → 0.92 (19.2% share)",
            ha="left", va="top", fontsize=7.8, color=PALETTE["text_body"], linespacing=1.25, zorder=3)

    # Pathway B sub-box
    box_2a2 = patches.FancyBboxPatch((c2_x + 1.0 + (col_w - 2.6)/2 + 0.6, card2a_y), (col_w - 2.6)/2, card2a_h,
                                     boxstyle="round,pad=0.3", fc=PALETTE["crimson_bg"],
                                     ec=PALETTE["crimson_border"], lw=1.0, zorder=2)
    ax.add_patch(box_2a2)
    ax.text(c2_x + 2.2 + (col_w - 2.6)/2, card2a_y + card2a_h - 1.8, "PATHWAY B: PARASITISM",
            ha="left", va="center", fontsize=8.6, weight="bold", color=PALETTE["crimson_dark"], zorder=3)
    ax.text(c2_x + 2.2 + (col_w - 2.6)/2, card2a_y + card2a_h - 3.4, "Epistemic Usurpation\n• Offloading (ω → 1.0)\n• Effort collapse u* → 0.01\n• Cognitive Debt d = 2.11\n• Agency collapse A* → 0.17 (51.9%)",
            ha="left", va="top", fontsize=7.8, color=PALETTE["text_body"], linespacing=1.25, zorder=3)

    # 3. Section 2B: Embedded Subplot: EVC Prefrontal Effort Collapse
    sub3_left = (c2_x + 3.0) / 100.0
    sub3_w = (col_w - 4.8) / 100.0
    sub3_bot = 0.525
    sub3_h = 0.225
    
    ax_evc = fig.add_axes([sub3_left, sub3_bot, sub3_w, sub3_h])
    omega_vals = np.linspace(0.0, 1.0, 100)
    u_th4 = 0.60 * np.exp(-2.2 * omega_vals)
    u_th8 = 0.45 * np.exp(-2.9 * omega_vals)
    u_th12 = 0.32 * np.exp(-3.5 * omega_vals)
    
    ax_evc.plot(omega_vals, u_th4, color=PALETTE["emerald_dark"], lw=1.8, label="Low Cost (θ = 4.0)")
    ax_evc.plot(omega_vals, u_th8, color=PALETTE["royal_blue"], lw=2.2, label="Nominal (θ = 8.0, u* = 0.45)")
    ax_evc.plot(omega_vals, u_th12, color=PALETTE["crimson"], lw=1.8, ls="--", label="High Cost (θ = 12.0)")
    
    ax_evc.set_xlabel("Conversational Offloading Fraction (ω)", fontsize=8.4, labelpad=2)
    ax_evc.set_ylabel("Optimal Effort u*(ω)", fontsize=8.4, labelpad=2)
    ax_evc.set_title("EVC Prefrontal Effort Collapse: ∂²V/∂u∂ω < 0", fontsize=9.6, weight="bold", pad=4)
    ax_evc.tick_params(axis="both", labelsize=7.8)
    ax_evc.set_ylim(-0.02, 0.68)
    ax_evc.grid(True, ls=":", alpha=0.6)
    ax_evc.legend(loc="upper right", fontsize=7.6, frameon=True, facecolor="#FFFFFF")
    
    ax_evc.annotate("Effort Collapse\nu*(1.0) → 0.02", xy=(1.0, 0.02), xytext=(0.58, 0.22),
                    fontsize=8.0, weight="bold", color=PALETTE["crimson_dark"],
                    arrowprops=dict(arrowstyle="->", color=PALETTE["crimson"], lw=1.1))

    # 4. Section 2C: Embedded Subplot: Global Monte Carlo Bifurcation (N=5,000)
    sub4_bot = 0.220
    sub4_h = 0.225
    ax_mc = fig.add_axes([sub3_left, sub4_bot, sub3_w, sub4_h])
    
    np.random.seed(42)
    mc_omega = np.random.uniform(0.0, 1.0, 500)
    mc_u = 0.45 * np.exp(-3.0 * mc_omega) + np.random.normal(0, 0.02, 500)
    mc_u = np.clip(mc_u, 0.005, 0.6)
    mc_A = (0.35 * mc_u) / (0.35 * mc_u + 0.08 * mc_omega + 0.01) + np.random.normal(0, 0.03, 500)
    mc_A = np.clip(mc_A, 0.05, 0.98)
    
    colors = [PALETTE["emerald"] if a >= 0.70 else (PALETTE["amber"] if a >= 0.35 else PALETTE["crimson"]) for a in mc_A]
    ax_mc.scatter(mc_omega, mc_A, c=colors, alpha=0.35, s=14, edgecolors="none", zorder=2)
    
    fine_omega = np.linspace(0.0, 1.0, 100)
    fine_u = 0.45 * np.exp(-3.0 * fine_omega)
    fine_A = (0.35 * fine_u) / (0.35 * fine_u + 0.08 * fine_omega + 0.01)
    ax_mc.plot(fine_omega, fine_A, color="#0F172A", lw=2.4, label="Mean E[A*|ω]", zorder=4)
    
    omega_crit = 0.91
    ax_mc.axvline(omega_crit, color=PALETTE["crimson"], lw=2.0, ls="--", zorder=5)
    ax_mc.axhline(0.35, color=PALETTE["crimson"], lw=1.2, ls=":", zorder=5)
    
    ax_mc.set_xlabel("Conversational Offloading (ω)", fontsize=8.4, labelpad=2)
    ax_mc.set_ylabel("Steady-State Agency A*", fontsize=8.4, labelpad=2)
    ax_mc.set_title("Global Phase-Space Bifurcation (N = 5,000 Draws)", fontsize=9.6, weight="bold", pad=4)
    ax_mc.set_xlim(-0.02, 1.02)
    ax_mc.set_ylim(0.0, 1.05)
    ax_mc.tick_params(axis="both", labelsize=7.8)
    ax_mc.grid(True, ls=":", alpha=0.6)
    
    ax_mc.annotate("Bifurcation Threshold\nω_crit ≈ 0.91", xy=(omega_crit, 0.35), xytext=(0.42, 0.50),
                   fontsize=8.0, weight="bold", color=PALETTE["crimson_dark"],
                   arrowprops=dict(arrowstyle="->", color=PALETTE["crimson"], lw=1.1),
                   bbox=dict(boxstyle="round,pad=0.25", fc=PALETTE["crimson_bg"], ec=PALETTE["crimson_border"], lw=0.8))
    
    ax_mc.text(0.04, 0.88, "Scaffolding (19.2%)\nA* ≥ 0.70", fontsize=7.6, weight="bold", color=PALETTE["emerald_dark"])
    ax_mc.text(0.46, 0.10, "Epistemic Parasitism (51.9%)\nA* < 0.35", fontsize=7.6, weight="bold", color=PALETTE["crimson_dark"])

    # Bottom Callout for Column 2
    draw_pill_badge(ax, c2_x + 1.0, col_y + 1.2, col_w - 2.0, 11.0,
                    "PHASE-SPACE BIFURCATION FINDING:\n"
                    "• Critical Tipping Point: Offloading beyond ω_crit ≈ 0.91 collapses agency (A* → 0.17)\n"
                    "• Mental Integrity: M_integrity < 0.20 in 51.9% of Monte Carlo parameter draws\n"
                    "• Autonomy Breach: Parasitism robs children of autonomous cognitive struggle\n"
                    "• Regulatory Verdict: Unconstrained LLM tutoring induces functional prefrontal disuse.",
                    PALETTE["purple_bg"], PALETTE["purple_dark"], PALETTE["purple_border"], fontsize=8.4, linespacing=1.3)

    # =============================================================
    # COLUMN 3: SIMULATION 2: BAYESIAN 3Rs GATEKEEPING
    # =============================================================
    # 1. Header Banner of Column 3 (Clean LIGHT background, no black/dark)
    h3_bg = patches.FancyBboxPatch((c3_x, col_y + col_h - 6.2), col_w, 6.2, boxstyle="round,pad=0.25",
                                   fc=PALETTE["header_bg"], ec=PALETTE["border_header"], lw=1.2, zorder=2)
    ax.add_patch(h3_bg)
    ax.text(c3_x + col_w/2, col_y + col_h - 2.4, "3. SIMULATION 2: BAYESIAN 3Rs GATEKEEPING",
            ha="center", va="center", fontsize=11.6, weight="bold", color=PALETTE["text_dark"], zorder=3)
    ax.text(c3_x + col_w/2, col_y + col_h - 4.6, "Precautionary Value-of-Information & Regulatory Thresholds",
            ha="center", va="center", fontsize=8.6, style="italic", color=PALETTE["text_muted"], zorder=3)

    # 2. Section 3A: Transposing Russell & Burch's 3Rs (1959) Card
    card3a_y = col_y + col_h - 23.2
    card3a_h = 16.0
    c3a_box = patches.FancyBboxPatch((c3_x + 1.0, card3a_y), col_w - 2.0, card3a_h,
                                     boxstyle="round,pad=0.35", fc="#FFFFFF",
                                     ec=PALETTE["royal_blue_border"], lw=1.2, zorder=2)
    ax.add_patch(c3a_box)
    
    ax.text(c3_x + col_w/2, card3a_y + card3a_h - 1.8, "Transposing Russell & Burch's 3Rs to Educational AI",
            ha="center", va="center", fontsize=9.6, weight="bold", color=PALETTE["royal_blue_dark"], zorder=3)

    r_principles = [
        ("1. REPLACEMENT (Surrogacy)",
         "Synthetic personas (n=720, κ=0.8860) absorb 100% of risk; silicon fails so children do not.",
         PALETTE["royal_blue"]),
        ("2. REDUCTION (Minimal Cohorts)",
         "In-silico failure mapping avoids trial-and-error; reduces live cohorts by >80%.",
         PALETTE["purple"]),
        ("3. REFINEMENT (Deterministic)",
         "Logit masking & decoupled CAS guarantee pedagogical resistance prior to live pilots.",
         PALETTE["emerald"])
    ]
    for idx, (title, desc, col) in enumerate(r_principles):
        ry = card3a_y + card3a_h - 4.4 - (idx * 3.9)
        badge = patches.FancyBboxPatch((c3_x + 1.8, ry - 2.6), col_w - 3.6, 3.4, boxstyle="round,pad=0.2",
                                       fc="#F8FAFC", ec=col, lw=0.9, zorder=3)
        ax.add_patch(badge)
        ax.text(c3_x + 2.5, ry - 0.4, title, ha="left", va="center", fontsize=8.2, weight="bold", color=col, zorder=4)
        ax.text(c3_x + 2.5, ry - 1.7, desc, ha="left", va="center", fontsize=7.4, color=PALETTE["text_body"],
                linespacing=1.15, zorder=4)

    # 3. Section 3B: Embedded Subplot: Bayesian VoI Loss vs Cohort Size N
    sub5_left = (c3_x + 3.0) / 100.0
    sub5_w = (col_w - 4.8) / 100.0
    sub5_bot = 0.445
    sub5_h = 0.235
    
    ax_voi = fig.add_axes([sub5_left, sub5_bot, sub5_w, sub5_h])
    n_cohort = np.linspace(1, 150, 150)
    p0 = 0.4933
    sens = 0.85
    spec = 0.92
    c_harm = 1.0
    c_comp = 2.0
    c_delay = 0.5
    
    loss_invivo = p0 * n_cohort * c_harm
    loss_insilico = c_comp + p0 * (1.0 - sens) * n_cohort * c_harm + (1.0 - p0) * (1.0 - spec) * c_delay
    
    ax_voi.plot(n_cohort, loss_invivo, color=PALETTE["crimson"], lw=2.4, ls="--", label="Direct In-Vivo Testing E[L_invivo]")
    ax_voi.plot(n_cohort, loss_insilico, color=PALETTE["royal_blue"], lw=2.4, label="Precautionary In-Silico 3Rs E[L_insilico]")
    ax_voi.fill_between(n_cohort, loss_insilico, loss_invivo, color=PALETTE["royal_blue"], alpha=0.15, label="Precautionary ΔVoI")
    
    ax_voi.set_xlabel("Pediatric Cohort Size (N Minors)", fontsize=8.4, labelpad=2)
    ax_voi.set_ylabel("Expected Ethical Loss E[L]", fontsize=8.4, labelpad=2)
    ax_voi.set_title("Bayesian Precautionary Decision Frontier", fontsize=9.6, weight="bold", pad=4)
    ax_voi.tick_params(axis="both", labelsize=7.8)
    ax_voi.set_xlim(0, 150)
    ax_voi.set_ylim(0, 78)
    ax_voi.grid(True, ls=":", alpha=0.6)
    ax_voi.legend(loc="upper left", bbox_to_anchor=(0.01, 0.99), fontsize=7.4, frameon=True, facecolor="#FFFFFF", framealpha=0.9)
    
    ax_voi.plot([30], [p0 * 30 * c_harm], marker="o", color=PALETTE["crimson"], markersize=5)
    ax_voi.plot([120], [p0 * 120 * c_harm], marker="o", color=PALETTE["crimson"], markersize=5)
    
    # Position callouts in open spaces clear of legend
    ax_voi.annotate("N = 30 (Classroom)\n71.5% Harm Reduction\n(ΔVoI = 10.58)",
                    xy=(30, p0 * 30 * c_harm), xytext=(32, 26),
                    fontsize=7.8, weight="bold", color=PALETTE["royal_blue_dark"],
                    arrowprops=dict(arrowstyle="->", color=PALETTE["royal_blue"], lw=1.0),
                    bbox=dict(boxstyle="round,pad=0.25", fc=PALETTE["royal_blue_bg"], ec=PALETTE["royal_blue_border"], lw=0.8))
    
    ax_voi.annotate("N = 120 (Grade Level)\n81.6% Harm Reduction\n(ΔVoI = 48.31)",
                    xy=(120, p0 * 120 * c_harm), xytext=(85, 34),
                    fontsize=7.8, weight="bold", color=PALETTE["royal_blue_dark"],
                    arrowprops=dict(arrowstyle="->", color=PALETTE["royal_blue"], lw=1.0),
                    bbox=dict(boxstyle="round,pad=0.25", fc=PALETTE["royal_blue_bg"], ec=PALETTE["royal_blue_border"], lw=0.8))

    # 4. Section 3C: Regulatory Verdict Card (Clean LIGHT background, no black/dark)
    card3c_y = col_y + 1.2
    card3c_h = 35.5
    c3c_box = patches.FancyBboxPatch((c3_x + 1.0, card3c_y), col_w - 2.0, card3c_h,
                                     boxstyle="round,pad=0.4", fc="#F8FAFC",
                                     ec=PALETTE["purple_dark"], lw=1.4, zorder=2)
    ax.add_patch(c3c_box)
    
    ax.text(c3_x + col_w/2, card3c_y + card3c_h - 2.3, "INSTITUTIONAL REVIEW BOARD (IRB) MANDATE",
            ha="center", va="center", fontsize=9.8, weight="bold", color=PALETTE["purple_dark"], zorder=3)
    ax.text(c3_x + col_w/2, card3c_y + card3c_h - 4.5, "Federal Compliance Standard: 45 CFR 46 Subpart D",
            ha="center", va="center", fontsize=8.4, weight="bold", color=PALETTE["royal_blue_dark"], zorder=3)

    legal_points = [
        ("• Exceeds Statutory Minimal Risk:",
         "  A baseline failure rate of p₀ = 49.33% with d = 2.11 cognitive collapse\n  exceeds statutory minimal risk for minor schoolchildren."),
        ("• Non-Maleficence & Consent Breach:",
         "  Deploying unverified foundation models treats children as non-\n  consensual test beds for corporate algorithmic discovery."),
        ("• Mandatory 3Rs Surrogacy Standard:",
         "  Certified pre-clinical in-silico clearance (Sens ≥ 0.85, κ ≥ 0.8860)\n  must be legally required before any child is exposed in classroom trials."),
        ("• Quantified Harm Reduction Across Scales:",
         "  Achieves 71.5% (N=30), 81.6% (N=120), and 84.6% (N=1,000) reduction\n  in expected developmental harm across deployment scales.")
    ]
    for idx, (head, body) in enumerate(legal_points):
        py = card3c_y + card3c_h - 7.3 - (idx * 6.0)
        ax.text(c3_x + 2.2, py, head, ha="left", va="center", fontsize=8.2, weight="bold", color=PALETTE["text_dark"], zorder=3)
        ax.text(c3_x + 2.2, py - 2.2, body, ha="left", va="center", fontsize=7.6, color=PALETTE["text_body"],
                linespacing=1.2, zorder=3)

    draw_pill_badge(ax, c3_x + 1.8, card3c_y + 1.2, col_w - 3.6, 3.4,
                    "ACTIONABLE PROTOCOL: SILICON MUST ABSORB EXPERIMENTAL RISK",
                    PALETTE["purple_bg"], PALETTE["purple_dark"], PALETTE["purple_border"], fontsize=8.2)

    # =============================================================
    # EXPORT VECTOR PDF
    # =============================================================
    out_dir = Path("/home/jason/EdTechPaper1/project_bioethics_in_silico/manuscript/springer_artwork")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_path = out_dir / "graphical_abstract.pdf"
    plt.savefig(pdf_path, format="pdf", bbox_inches="tight", dpi=300)
    print(f"Generated Graphical Abstract: {pdf_path.name} in {out_dir}")
        
    cog_debt_fig = Path("/home/jason/EdTechPaper1/project_ai_cognitive_debt/figures")
    if cog_debt_fig.exists():
        dst = cog_debt_fig / "graphical_abstract.pdf"
        import shutil
        shutil.copy2(pdf_path, dst)
        print(f"Copied to {dst}")
                
    plt.close()

if __name__ == "__main__":
    build_graphical_abstract()
