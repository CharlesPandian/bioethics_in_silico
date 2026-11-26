# Extended Mind or Epistemic Parasitism? The Neuroethics of Generative AI in Childhood

[![Target Journal: Neuroethics](https://img.shields.io/badge/Target_Journal-Neuroethics-0072B2?style=flat-square)](https://www.springer.com/journal/12152)
[![Publisher: Springer Nature](https://img.shields.io/badge/Publisher-Springer_Nature-orange?style=flat-square)](https://www.springernature.com)
[![Citation Style: sn--basic--Numbered](https://img.shields.io/badge/Citation_Style-sn--basic%2CNumbered-blueviolet?style=flat-square)](#)
[![Submission Audit: 100% Compliant](https://img.shields.io/badge/Submission_Audit-100%25_Compliant-success?style=flat-square)](#reproducibility--verification)
[![Double-Anonymous Review: Verified](https://img.shields.io/badge/Peer_Review-Double--Anonymous_Ready-green?style=flat-square)](#)

---

## 1. Executive Summary & Philosophical Rationale

The rapid, unvetted integration of conversational generative artificial intelligence (GenAI) into compulsory elementary classrooms represents an unprecedented, unmonitored intervention into developing human cognitive architecture. Marketed by commercial edtech developers as benign "Socratic companions" and "one-on-one personal tutors," empirical evaluations reveal that conversational language models routinely suffer sycophantic breakdown—surrendering terminal problem solutions under iterative student wear-down. This dynamic systematically bypasses the cognitive friction and productive struggle essential for prefrontal schema consolidation and metacognitive calibration during middle childhood (ages 7 to 11).

Grounding our inquiry in **active externalism**, **pediatric neuroethics**, and **neurorights**, this project investigates a fundamental normative question:
> *Does conversational generative AI operate as an authentic cognitive scaffold under the Extended Mind Thesis, or does it instantiate an insidious regime of epistemic parasitism that incurs long-term cognitive debt?*

### Key Conceptual Pillars
1. **Extended Mind vs. Epistemic Parasitism:** Drawing on Clark and Chalmers' active externalism, we formalize criteria distinguishing legitimate cognitive extension (trust, reliability, cognitive symbiosis) from epistemic parasitism (the covert subversion of autonomous cognitive effort).
2. **Pediatric Neurorights:** Extending the four core neurorights (cognitive liberty, mental privacy, mental integrity, and psychological continuity) to developing children, whose prefrontal executive control networks are structurally immature and uniquely susceptible to conversational dependency.
3. **Translational Bioethics (The In-Silico 3Rs):** Operationalizing Russell and Burch's foundational 3Rs of animal and biomedical research ethics—**Replacement**, **Reduction**, and **Refinement**—into institutional mandates for algorithmic research governance. We argue that silicon must absorb experimental failure to protect developing children from foreseeable cognitive harm.

---

## 2. Core Computational & Theoretical Models

To bridge normative philosophy with rigorous quantitative modeling, this repository provides two original computational neuroethics models:

```
                                  [ THE DUAL-MODEL FRAMEWORK ]

     MODEL 1: COGNITIVE PHASE TRANSITION                   MODEL 2: BIOETHICAL GOVERNANCE
  ┌────────────────────────────────────────┐            ┌────────────────────────────────────────┐
  │ Coupled EVC-Metacognitive Dynamical   │            │ Bayesian Precautionary VoI Decision    │
  │ Model: Phase space bifurcation at      │   ─────►   │ Model: Institutional Review Board gate-│
  │ critical offloading threshold          │            │ keeping operationalizing 3Rs to absorb │
  │        (omega_crit ≈ 0.91)             │            │ adverse risks in-silico (81.6% harm red)│
  └────────────────────────────────────────┘            └────────────────────────────────────────┘
```

### Model 1: Coupled EVC & Metacognitive Agency Dynamical Model
- **Theory:** Couples Shenhav et al.'s **Expected Value of Control (EVC)** with a non-linear metacognitive agency drift equation.
- **Monte Carlo Sensitivity:** Global sensitivity analysis ($N = 5,000$ draws) across five behavioral parameters.
- **Key Finding:** Uncovers a non-linear phase transition into epistemic parasitism once conversational offloading exceeds a critical bifurcation threshold ($\omega_{\text{crit}} \approx 0.91$), demonstrating that cognitive extension is non-monotonic and collapses into cognitive debt.
- **Implementation:** [`src/simulation_1_extended_mind_phase_space.py`](src/simulation_1_extended_mind_phase_space.py)

### Model 2: Bayesian Precautionary Value-of-Information (VoI) 3Rs Decision Model
- **Theory:** Translates biomedical research ethics into a Bayesian decision-theoretic framework for Institutional Review Boards (IRBs) and Research Ethics Committees (RECs).
- **Statutory Benchmark:** Evaluated against federal minimal-risk thresholds under **45 CFR 46 Subpart D** (Special Protections for Children as Research Subjects).
- **Key Finding:** Certified in-silico pre-screening achieves an **$81.6\%$ reduction in expected ethical harm** for a single grade cohort ($N = 120$) and **$84.6\%$** for a district pilot ($N = 1,000$), demonstrating that direct live classroom testing of unverified LLMs is bioethically impermissible when computational surrogates are available.
- **Implementation:** [`src/simulation_2_irb_precautionary_decision.py`](src/simulation_2_irb_precautionary_decision.py)

### Empirical Baseline Anchor
To prevent detached armchair abstraction, the models are calibrated against empirical baseline parameters from prior technical audits ([Pandian, 2026](https://github.com/CharlesPandian/ai_cognitive_debt)):
- **Performance–Learning Paradox:** Calibrated on $N = 4,200$ learner trajectories across 24 mathematics Knowledge Components (derived from 88 ASSISTments RCTs), demonstrating that direct answer offloading increases assisted completion to $94.1\%$ but collapses unassisted 48-hour retention to $34.2\%$ ($F = 4,613.27, p < .001, d = 2.11, \Delta\text{BIC} = -24,740.7$).
- **Multi-Agent Conversational Breakdown:** Multi-agent adversarial stress audits ($N = 900$ trajectories; 3,600 turns) show that commercial guardrailed conversational models suffer a **$48.1\%$ breakdown rate at Turn 4** under student emotional wear-down (overall failure rate $49.33\%$).

---

## 3. Target Journal & Article Specifications

- **Journal:** [*Neuroethics*](https://www.springer.com/journal/12152) (Springer Nature)
- **ISSN:** 1874-5490 (print) | 1874-5504 (electronic)
- **Aims & Scope:** Philosophical, empirical, and ethical questions emerging at the intersection of neuroscience, emerging cognitive technologies, mind philosophy, and law.
- **Article Type:** Original Research Article
- **Reference & Citation House Style:** Springer Nature Basic Numbered (`sn-basic,Numbered`)
  - In-text bracketed numeric citations: `[3]`, `[1-3, 7]`, and author-in-text callouts `Heinrichs [13]`, `Clark and Chalmers [5]`.
  - Numbered reference list alphabetized by author with full DOI hyperlinks.
- **Peer Review:** Double-Anonymous (blinded manuscript strictly decoupled from author identity).

---

## 4. Repository & Artifact Directory Structure

```text
project_bioethics_in_silico/
├── README.md                                  # Project overview and reproduction guide
├── requirements.txt                           # Python dependencies (NumPy, SciPy, Matplotlib, etc.)
├── verify_tier1_submission.py                 # Automated 7-point Tier-1 verification audit
├── TIER1_DATA_AUDIT.md                        # Formal data and statistical audit log
├── data/
│   ├── benchmark_100/                         # Calibrated benchmark datasets
│   ├── processed/                             # Processed telemetry trajectories
│   └── raw/                                   # Baseline RCT data structures
├── figures/                                   # Master figure outputs
├── src/
│   ├── simulation_1_extended_mind_phase_space.py      # EVC dynamical model & Monte Carlo simulation
│   ├── simulation_2_irb_precautionary_decision.py     # Bayesian VoI 3Rs decision model
│   ├── generate_exclusive_bioethics_diagrams.py       # Fig 1: 3Rs computational surrogacy architecture
│   ├── generate_exclusive_neuroethics_fig2.py         # Fig 2: Extended mind vs. parasitism taxonomy
│   ├── generate_normative_bioethical_matrix_fig5.py   # Fig 5: Qualitative IRB review matrix
│   ├── generate_neuroethics_graphical_abstract.py     # Visual graphical abstract pipeline
│   ├── 01_assistments_causal_analysis.py              # Empirical baseline ANOVA & mixed effects
│   ├── 02_bkt_cognitive_decay_model.py                # Bayesian Knowledge Tracing cognitive debt model
│   ├── 03_llm_validation_audit.py                    # Multi-agent persona simulation runner
│   └── 04_rubric_scorer_and_stats.py                  # Inter-rater reliability (Cohen's kappa)
└── manuscript/
    ├── manuscript.tex                         # Complete submission manuscript (sn-jnl, single-column)
    ├── manuscript.pdf                         # Compiled PDF with line numbers
    ├── manuscript_anonymized.tex              # Anonymized version for double-anonymous review
    ├── manuscript_anonymized.pdf              # Blinded PDF (0 author tokens)
    ├── manuscript_journal_twocolumn.tex       # Journal-layout showcase (sn-jnl, two-column)
    ├── manuscript_journal_twocolumn.pdf       # Typeset two-column PDF
    ├── title_page.tex                         # Standalone title page & metadata sheet
    ├── title_page.pdf                         # Compiled title page PDF
    ├── cover_letter.tex                       # Executive letterhead cover letter to Editor-in-Chief
    ├── cover_letter.pdf                       # Single-page executive PDF
    ├── references.bib                         # 35 authenticated BibTeX references
    ├── sn-jnl.cls                             # Official Springer Nature LaTeX class
    ├── sn-basic.bst                           # Official Springer Nature Basic bibliography style
    └── springer_artwork/                      # Standardized vector PDF artwork package
        ├── fig1_bioethics_framework_3rs.pdf
        ├── fig2_neuroethics_scaffolding_vs_parasitism.pdf
        ├── fig3_simulation_extended_mind_phase_space.pdf
        ├── fig4_simulation_irb_decision_frontier.pdf
        ├── fig5_qualitative_normative_matrix.pdf
        ├── fig6_bioethics_calculus_harm_tradeoff.pdf
        └── graphical_abstract.pdf
```

---

## 5. Submission Artifacts

All submission assets are typeset using the official Springer Nature macro package and compiled via [Tectonic](https://tectonic-typesetting.github.io/):

| Artifact | Purpose | Style / Layout |
| :--- | :--- | :--- |
| [`manuscript/manuscript.pdf`](manuscript/manuscript.pdf) | Formal Submission Version | Single-column, double-spaced lines, numbered lines (`lineno`) |
| [`manuscript/manuscript_anonymized.pdf`](manuscript/manuscript_anonymized.pdf) | Blinded Review Version | 100% redacted for double-anonymous review |
| [`manuscript/manuscript_journal_twocolumn.pdf`](manuscript/manuscript_journal_twocolumn.pdf) | Visual Showcase | Two-column journal production layout (`iicol`) |
| [`manuscript/title_page.pdf`](manuscript/title_page.pdf) | Metadata Sheet | Full author info, affiliation, declarations, abstract, keywords |
| [`manuscript/cover_letter.pdf`](manuscript/cover_letter.pdf) | Editor-in-Chief Letter | 1-page executive letterhead with prior work demarcation |
| [`manuscript/springer_artwork/`](manuscript/springer_artwork/) | Vector Artwork Package | Standardized vector PDF figures (Figures 1--6 + Graphical Abstract) |

---

## 6. Reproducibility & Verification

### Running the Automated Verification Audit
The repository includes an automated verification script that audits **7 comprehensive quality dimensions** (compilation, broken citations, Springer word count and heading rules, mandatory declarations, anonymization integrity, numerical telemetry verification, and artwork specifications):

```bash
python3 verify_tier1_submission.py
```

Expected output:
```text
===========================================================================
ALL SPRINGER NATURE NEUROETHICS TIER-1 VERIFICATION AUDITS PASSED (100% COMPLIANT)!
===========================================================================
```

### Reproducing Computational Simulations
To re-run the Monte Carlo phase transition simulation and generate Figure 3:
```bash
python3 src/simulation_1_extended_mind_phase_space.py
```

To re-run the Bayesian VoI IRB decision frontier simulation and generate Figure 4:
```bash
python3 src/simulation_2_irb_precautionary_decision.py
```

### Compiling LaTeX Documents
Using Tectonic:
```bash
tectonic manuscript/manuscript.tex
tectonic manuscript/manuscript_anonymized.tex
tectonic manuscript/manuscript_journal_twocolumn.tex
tectonic manuscript/title_page.tex
tectonic manuscript/cover_letter.tex
```

---

## 7. Citation & Provenance

If citing this neuroethical framework or utilizing the computational models, please cite:

```bibtex
@article{pandian2026neuroethics,
  title     = {Extended Mind or Epistemic Parasitism? The Neuroethics of Generative {AI} in Childhood},
  author    = {Pandian, Charles},
  journal   = {Neuroethics},
  year      = {2026},
  note      = {Submitted / Under Consideration},
  url       = {https://github.com/CharlesPandian/Research}
}
```

### Prior Empirical Motivation Benchmark
The secondary baseline telemetry referenced in Section 2 is archived at:
```bibtex
@article{pandian2026illusion,
  title     = {The Illusion of Competence and Cognitive Debt in Primary Mathematics: Causal Telemetry and Multi-Agent Behavioral Audits of Generative {AI} Tutoring},
  author    = {Pandian, Charles},
  journal   = {Preprint / Open-Access Research Archive},
  year      = {2026},
  url       = {https://github.com/CharlesPandian/ai_cognitive_debt}
}
```

---

## 8. License & Ethical Declarations
- **Code & Simulations:** Released under the [MIT License](LICENSE).
- **Manuscript Text & Figures:** © 2026 Charles Pandian. All rights reserved.
- **Ethical Compliance:** Conducted in strict adherence to the Declaration of Helsinki and 45 CFR 46. No living human or minor subjects were exposed to experimental interventions.
