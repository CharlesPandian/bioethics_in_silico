#!/usr/bin/env bash
# ==============================================================================
# Master Automation Script: Neuroethics (Springer Nature) Research Pipeline
# "Extended Mind or Epistemic Parasitism? The Neuroethics of Generative AI in Childhood"
# Author: Charles Pandian (jcs.pandian@gmail.com)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=============================================================================="
echo "  NEUROETHICS (SPRINGER NATURE) RESEARCH PIPELINE & REPRODUCIBILITY SUITE"
echo "  Target Article: Original Research Article"
echo "=============================================================================="

# Detect Python interpreter
if [ -f "$SCRIPT_DIR/../.venv/bin/python" ]; then
    PYTHON="$SCRIPT_DIR/../.venv/bin/python"
elif [ -f "$SCRIPT_DIR/.venv/bin/python" ]; then
    PYTHON="$SCRIPT_DIR/.venv/bin/python"
else
    PYTHON="python3"
fi

# Detect LaTeX compiler (Tectonic or pdflatex)
if command -v /home/jason/.local/bin/tectonic &> /dev/null; then
    LATEX_BIN="/home/jason/.local/bin/tectonic"
elif command -v tectonic &> /dev/null; then
    LATEX_BIN="tectonic"
elif command -v pdflatex &> /dev/null; then
    LATEX_BIN="pdflatex"
else
    LATEX_BIN=""
fi

echo "[*] Python interpreter: $PYTHON"
echo "[*] LaTeX compiler:     ${LATEX_BIN:-'None detected'}"

# Step 1: Execute Simulation 1 - EVC Dynamical System & Monte Carlo Phase Transition
echo ""
echo "[Step 1/5] Executing Simulation 1: Coupled EVC & Metacognitive Agency Phase Transition (N = 5,000)..."
$PYTHON src/simulation_1_extended_mind_phase_space.py

# Step 2: Execute Simulation 2 - Bayesian Value-of-Information (VoI) 3Rs Decision Frontier
echo ""
echo "[Step 2/5] Executing Simulation 2: Bayesian Precautionary VoI 3Rs Decision Model..."
$PYTHON src/simulation_2_irb_precautionary_decision.py

# Step 3: Generate Conceptual & Normative Bioethical Framework Diagrams
echo ""
echo "[Step 3/5] Generating Conceptual & Normative Artwork Package..."
$PYTHON src/generate_exclusive_bioethics_diagrams.py
$PYTHON src/generate_exclusive_neuroethics_fig2.py
$PYTHON src/generate_normative_bioethical_matrix_fig5.py
$PYTHON src/generate_neuroethics_graphical_abstract.py

# Step 4: Compile Springer Nature LaTeX Manuscripts
echo ""
echo "[Step 4/5] Compiling Springer Nature sn-jnl LaTeX Manuscripts..."
if [ -n "$LATEX_BIN" ]; then
    cd manuscript
    if [ "$LATEX_BIN" = "tectonic" ] || [ "$LATEX_BIN" = "/home/jason/.local/bin/tectonic" ]; then
        $LATEX_BIN manuscript.tex
        $LATEX_BIN manuscript_anonymized.tex
        $LATEX_BIN manuscript_journal_twocolumn.tex
        $LATEX_BIN title_page.tex
        $LATEX_BIN cover_letter.tex
    else
        pdflatex -interaction=nonstopmode manuscript.tex
        bibtex manuscript || true
        pdflatex -interaction=nonstopmode manuscript.tex
        pdflatex -interaction=nonstopmode manuscript.tex
        pdflatex -interaction=nonstopmode manuscript_anonymized.tex
        bibtex manuscript_anonymized || true
        pdflatex -interaction=nonstopmode manuscript_anonymized.tex
        pdflatex -interaction=nonstopmode manuscript_anonymized.tex
        pdflatex -interaction=nonstopmode manuscript_journal_twocolumn.tex
        bibtex manuscript_journal_twocolumn || true
        pdflatex -interaction=nonstopmode manuscript_journal_twocolumn.tex
        pdflatex -interaction=nonstopmode manuscript_journal_twocolumn.tex
        pdflatex -interaction=nonstopmode title_page.tex
        pdflatex -interaction=nonstopmode cover_letter.tex
    fi
    cd "$SCRIPT_DIR"
    echo "  -> Manuscripts compiled successfully:"
    echo "     - manuscript/manuscript.pdf (Single-Column Submission with Line Numbers)"
    echo "     - manuscript/manuscript_anonymized.pdf (Double-Anonymous Blinded Review)"
    echo "     - manuscript/manuscript_journal_twocolumn.pdf (Two-Column Showcase Layout)"
    echo "     - manuscript/title_page.pdf (Title Page & Metadata Sheet)"
    echo "     - manuscript/cover_letter.pdf (Single-Page Executive Cover Letter)"
else
    echo "WARNING: No LaTeX compiler found. TeX source files ready in manuscript/."
fi

# Step 5: Execute Tier-1 Verification Audit
echo ""
echo "[Step 5/5] Running Comprehensive Tier-1 Verification Audit..."
$PYTHON verify_tier1_submission.py

echo ""
echo "=============================================================================="
echo "  PIPELINE EXECUTION COMPLETE! ALL NEUROETHICS ARTIFACTS 100% VERIFIED"
echo "=============================================================================="
