# Def_Wiki and Def_ArXiv

## 📊 Benchmark Details

**Name**: Def_Wiki and Def_ArXiv

**Overview**: The paper introduces two novel datasets, Def_Wiki and Def_ArXiv, that collect and evaluate autoformalization of real-world mathematical definitions, assessing LLMs' performance in translating these definitions into a formal language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- miniF2F

**Resources**:
- [GitHub Repository](https://github.com/lanzhang128/definition_autoformalization)

## 🎯 Purpose and Intended Users

**Goal**: Assess the autoformalization capabilities of LLMs on complex mathematical definitions from real-world sources.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Autoformalization

**Limitations**: Existing benchmarks often focus on simpler problems; the datasets highlight more complex, real-world definitions.

## 💾 Data

**Source**: Collected from Wikipedia (Def_Wiki) and arXiv papers (Def_ArXiv).

**Size**: 56 definitions for Def_Wiki, 30 definitions for Def_ArXiv

**Format**: LaTeX

**Annotation**: Manual curation for collection.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Refinement via external feedback

**Metrics**:
- Pass rate
- Error types (Syntax Errors, Undefined Item Errors, Type Unification Failed Errors)

**Calculation**: Metrics are calculated as the proportion ofcorrect formalization outputs as evaluated by Isabelle/HOL.

**Interpretation**: Higher pass rates and lower error rates indicate better performance in autoformalization.

**Baseline Results**: Results against the miniF2F benchmark.

**Validation**: Evaluation through success rates and error analysis on Isabelle/HOL.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
