# Bioethics In Silico: Computational Surrogacy & Neuroethical Modeling of Conversational AI in Childhood

[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Pipeline: Verified](https://img.shields.io/badge/Pipeline-100%25_Reproducible-success?style=flat-square)](#4-running-procedures--reproducibility)
[![Simulations: Calibrated](https://img.shields.io/badge/Simulations-EVC_%26_Bayesian_VoI-blueviolet?style=flat-square)](#2-methodology--mathematical-formulations)

---

## 1. Project Overview & Scientific Motivation

The integration of conversational generative artificial intelligence into compulsory elementary education represents an unmonitored intervention into developing prefrontal cognitive architecture. Marketed as Socratic companions, commercial conversational tutors routinely surrender terminal problem solutions under student wear-down, eliminating the cognitive friction essential for prefrontal schema consolidation during middle childhood (ages 7 to 11).

This project formalizes the **Doctrine of Computational Surrogacy in Cognitive Technologies**, operationalizing Russell and Burch's foundational **3Rs (Replacement, Reduction, Refinement)** from biomedical research ethics into computational research governance. By establishing formal mathematical models and empirical benchmarks, this framework establishes that **silicon must absorb experimental failure** through in-silico simulation audits before developing human minds are exposed to autonomous conversational agents.

```
                              [ THE COMPUTATIONAL SURROGACY DOCTRINE ]

      REPLACEMENT                           REDUCTION                             REFINEMENT
  ┌─────────────────────────┐           ┌─────────────────────────┐           ┌─────────────────────────┐
  │ Replace live child      │           │ Reduce human exposure   │           │ Refine conversational   │
  │ testing with synthetic  │   ─────►  │ cohorts via pre-screened│   ─────►  │ friction to preserve    │
  │ multi-agent behavioral  │           │ Bayesian VoI risk-gate  │           │ prefrontal cognitive    │
  │ stress audits.          │           │ thresholds (81.6% harm) │           │ struggle & autonomy.    │
  └─────────────────────────┘           └─────────────────────────┘           └─────────────────────────┘
```

---

## 2. Methodology & Mathematical Formulations

The research pipeline integrates empirical baseline calibration with two original computational simulation models:

### 2.1 Empirical Baseline Motivation
To anchor the neuroethical inquiry in measured behavioral reality, the framework synthesizes two large-scale empirical benchmarks:
1. **Counterfactual Learning Trajectory Benchmark (N = 4,200):** Derived from 88 randomized controlled trials in primary mathematics across 24 Knowledge Components, quantifying the **Performance–Learning Paradox** (immediate assistance boosts session score, but unassisted delayed retention collapses).
2. **Multi-Agent Behavioral Stress Audit (N = 900 trajectories; 3,600 conversational turns):** Adversarial multi-turn evaluations using synthetic student personas (*Answer-Seeking*, *Frustrated / Low-Persistence*, and *Misconception-Driven*) testing commercial LLM pedagogical guardrail breakdown rates.

---

### 2.2 Simulation 1: Coupled EVC & Metacognitive Agency Dynamical Model
This model couples Shenhav et al.'s **Expected Value of Control (EVC)** with a non-linear metacognitive agency drift equation to track executive effort allocation over developmental time:

```text
EVC(u) = Objective Reward - Subjective Cost of Effort
       = R · P(Success | u, ω) - Cost(u)
```

The system dynamics are defined by coupled differential equations:

```text
du/dt = α_u · (∂EVC / ∂u) - γ_u · u
dA/dt = β_A · u(t) - δ_A · ω(t) · A(t)
```

where:
* `u(t) ∈ [0, 1]` represents intrinsic prefrontal executive control effort.
* `A(t) ∈ [0, 1]` represents metacognitive agency and self-efficacy.
* `ω ∈ [0, 1]` represents conversational AI offloading intensity.
* A **global Monte Carlo sensitivity analysis (N = 5,000 draws)** samples the parameter space to detect tipping points and phase transitions.

---

### 2.3 Simulation 2: Bayesian Precautionary Value-of-Information (VoI) 3Rs Decision Model
This model formulates an Institutional Review Board (IRB) gatekeeping calculus under **45 CFR 46 Subpart D** (minimal-risk protections for children). An IRB evaluates whether to expose a student cohort of size N to an unverified conversational tutor with prior breakdown probability `p_0 = P(Harmful) = 49.33%`:

* **Direct In-Vivo Trial (D_in-vivo):** Exposes children directly. Expected ethical loss:
  ```text
  E[Loss | D_in-vivo] = p_0 · N · C_harm
  ```
* **In-Silico 3Rs Pre-Screening (D_in-silico):** Conducts computational multi-agent stress audits prior to child exposure. With audit sensitivity `Sens = 0.85` and specificity `Spec = 0.90`, Bayes' rule computes updated posterior risk `p_1 = P(Harmful | Pass)`, releasing only vetted systems:
  ```text
  E[Loss | D_in-silico] = C_audit + P(Pass) · p_1 · N · C_harm
  ```
* **Precautionary Value of Information (VoI):**
  ```text
  VoI = E[Loss | D_in-vivo] - E[Loss | D_in-silico]
  ```

---

## 3. Results & Empirical Telemetry

### 3.1 Empirical Telemetry: Cognitive Debt & LLM Sycophancy Breakdown

The empirical benchmarks demonstrate severe delayed learning collapse and high vulnerability of commercial LLM guardrails to conversational wear-down:

| Empirical Dimension | Friction-Preserving Scaffolding | Direct AI Answer Offloading | Statistical Significance / Effect Size |
| :--- | :---: | :---: | :--- |
| **In-Session Performance** | 68.4% | 94.1% | Artificial inflation during assisted use |
| **Delayed Unassisted Post-Test (48h)** | **63.0%** | **34.2%** | **Collapse of unassisted competence (d = 2.11)** |
| **Repeated-Measures ANOVA** | — | — | F(2, 4197) = 4,613.27, p < .001, η_p² = 0.687 |
| **Response Latency Drift** | β = +0.042 (deliberative) | β = -0.173 (impulsive) | Deliberation cut by half (p < .001) |
| **BKT Schema Retention (L_n)** | 83.4% | 13.7% | Bayesian model fit: ΔBIC = -24,740.7 |
| **Guardrailed LLM Breakdown (Turn 4)** | — | **48.1%** | Catastrophic surrender under student pleading |
| **Overall Guardrailed Failure Rate** | — | **49.33%** | Mean Time-to-Offload (TTO = 3.98 turns) |

---

### 3.2 Simulation 1 Results: Phase Transition & Bifurcation Analysis

Global Monte Carlo simulations (N = 5,000 parameter draws) reveal that cognitive extension is non-monotonic: as offloading intensity crosses a sharp threshold, intrinsic cognitive effort collapses:

```text
  Intrinsic Effort u*(t)
   1.0 ┼───────┐
       │       │  [ AUTHENTIC EXTENDED MIND ]
   0.8 ┼       └───┐   Effort preserved; scaffolding active (19.2% of phase space)
       │           │
   0.6 ┼           └──────┐
   0.4 ┼──────────────────┴─────────────┐  Nominal Effort (u* = 0.45)
       │                                │
   0.2 ┼                                └─────────┐   CRITICAL BIFURCATION CLIFF
       │                                          │   omega_crit ≈ 0.91
   0.0 ┼──────────────────────────────────────────┴───────────────► Offloading Intensity ω
       0.0    0.2     0.4     0.6     0.8    0.91    1.0
                                                  ▲
                                                  │ [ EPISTEMIC PARASITISM ]
                                                  │ Effort collapses to zero;
                                                  │ 51.9% of phase space in cognitive debt
```

* **Authentic Cognitive Scaffolding:** Sustained in only **19.2%** of sampled parameter space.
* **Epistemic Parasitism:** Dominates **51.9%** of phase space, characterized by complete executive disengagement (u → 0, A → 0).
* **Critical Bifurcation Threshold:** Occurs at **ω_crit ≈ 0.91**, proving that unregulated offloading causes a non-linear phase collapse into cognitive debt.

---

### 3.3 Simulation 2 Results: Precautionary VoI & Harm Reduction

Evaluating Bayesian gatekeeping across educational cohort scales proves that computational pre-screening dramatically eliminates ethical harm:

| Educational Cohort Scale | Student Sample Size (N) | Direct Testing Loss E[D_in-vivo] | 3Rs In-Silico Loss E[D_in-silico] | Precautionary VoI (C_harm units) | Harm Reduction (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Classroom Cohort** | N = 25 | 14.80 | 4.22 | **+10.58** | **71.5%** |
| **Grade Cohort** | N = 120 | 59.20 | 10.89 | **+48.31** | **81.6%** |
| **District Pilot** | N = 1,000 | 493.30 | 76.00 | **+417.30** | **84.6%** |

```text
  Ethical Harm Reduction by In-Silico Pre-Screening (%)
  100% ┼─────────────────────────────────────────────────────────────
       │
   80% ┼                     81.6%                      84.6%
       │                    ┌─────┐                    ┌─────┐
   60% ┼       71.5%        │     │                    │     │
       │      ┌─────┐       │     │                    │     │
   40% ┼      │     │       │     │                    │     │
       │      │     │       │     │                    │     │
   20% ┼      │     │       │     │                    │     │
       │      │     │       │     │                    │     │
    0% ┼──────┴─────┴───────┴─────┴────────────────────┴─────┴───────
            Classroom             Grade                    District
            (N = 25)            (N = 120)                 (N = 1,000)
```

---

## 4. Running Procedures & Reproducibility

### 4.1 Prerequisites & Installation

Clone the repository and install required dependencies in a Python 3.10+ virtual environment:

```bash
# Clone the repository
git clone https://github.com/CharlesPandian/bioethics_in_silico.git
cd bioethics_in_silico

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4.2 Automated Master Pipeline
To execute all simulations, run parameter verifications, and generate output figures in a single command:

```bash
./run_all.sh
```

### 4.3 Running Individual Simulation Modules

Each simulation component can be executed independently:

```bash
# Simulation 1: Execute EVC Dynamical System & Monte Carlo Phase Space Analysis (N = 5,000)
python3 src/simulation_1_extended_mind_phase_space.py

# Simulation 2: Execute Bayesian VoI 3Rs Decision Model & Harm Frontiers
python3 src/simulation_2_irb_precautionary_decision.py

# Generate Bioethical Framework & Decision Matrix Visualizations
python3 src/generate_exclusive_bioethics_diagrams.py
python3 src/generate_exclusive_neuroethics_fig2.py
python3 src/generate_normative_bioethical_matrix_fig5.py
python3 src/generate_neuroethics_graphical_abstract.py

# Execute Comprehensive Quantitative Verification Audit
python3 verify_tier1_submission.py
```

### 4.4 Repository Directory Structure

```text
bioethics_in_silico/
├── README.md                                  # Research overview and reproduction documentation
├── requirements.txt                           # Core dependencies (NumPy, SciPy, Matplotlib, Pandas)
├── run_all.sh                                 # Master reproduction pipeline
├── verify_tier1_submission.py                 # Telemetry and mathematical consistency audit
├── data/
│   ├── benchmark_100/                         # Calibrated 100-item primary mathematics benchmark
│   ├── processed/                             # Processed telemetry, BKT models, and audit checkpoints
│   └── raw/                                   # Baseline dataset provenance documentation
└── src/
    ├── simulation_1_extended_mind_phase_space.py      # EVC dynamical system & Monte Carlo simulation
    ├── simulation_2_irb_precautionary_decision.py     # Bayesian Precautionary VoI decision model
    ├── generate_exclusive_bioethics_diagrams.py       # Computational 3Rs surrogacy architecture
    ├── generate_exclusive_neuroethics_fig2.py         # Extended Mind vs. Parasitism taxonomic diagrams
    ├── generate_normative_bioethical_matrix_fig5.py   # Qualitative IRB risk matrix generator
    ├── generate_neuroethics_graphical_abstract.py     # Conceptual visual abstract generator
    ├── 01_assistments_causal_analysis.py              # Empirical baseline ANOVA & mixed effects
    ├── 02_bkt_cognitive_decay_model.py                # Bayesian Knowledge Tracing decay model
    ├── 03_llm_validation_audit.py                    # Multi-agent persona simulation runner
    └── 04_rubric_scorer_and_stats.py                  # Inter-rater concordance statistics
```

---

## 5. License & Ethical Declarations

* **Code & Simulations:** Released under the [MIT License](LICENSE).
* **Dataset & Telemetry Provenance:** Conducted in strict adherence to the ethical principles of the Declaration of Helsinki and 45 CFR 46. Secondary analyses utilize pre-existing, de-identified open educational research data in the public domain. Synthetic multi-agent audits and computational simulations involve no living human or minor subjects.
