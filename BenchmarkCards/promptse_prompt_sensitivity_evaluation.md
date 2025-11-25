# PromptSE (Prompt Sensitivity Evaluation)

## 📊 Benchmark Details

**Name**: PromptSE (Prompt Sensitivity Evaluation)

**Overview**: PromptSE is a framework that creates semantically equivalent prompt variants with emotion and personality templates and evaluates model stability using probability-aware continuous scoring.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework for quantifying prompt stability in code generation models under natural expression variations.

**Target Audience**:
- ML Researchers
- Model Developers
- Industrial Practitioners

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is generated using the Python HumanEval benchmark with semantically equivalent variants.

**Size**: 14,760 examples

**Format**: N/A

**Annotation**: The data was generated using automated methods based on emotion and personality templates.

## 🔬 Methodology

**Methods**:
- Probability-aware evaluation
- Human evaluation

**Metrics**:
- AUC-E (Area Under Curve of Elasticity)
- Pass rates

**Calculation**: AUC-E is computed using Simpson’s rule numerical integration over elasticity measurements.

**Interpretation**: Higher AUC-E values indicate better prompt stability, with values approaching 1 suggesting highly robust models.

**Baseline Results**: N/A

**Validation**: Statistical analysis employing robust methods including correlation tests and confidence intervals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
