# Winogender Schemas for Coreference Resolution Systems

## 📊 Benchmark Details

**Name**: Winogender Schemas for Coreference Resolution Systems

**Overview**: This study examines gender bias in coreference resolution systems by utilizing Winogender schemas—minimal pair sentences differing only by pronoun gender—to reveal systematic biases across three publicly available coreference systems.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Coreference Resolution

**Languages**:
- English

**Similar Benchmarks**:
- WinoBias

**Resources**:
- [GitHub Repository](https://github.com/rudinger/winogender-schemas)

## 🎯 Purpose and Intended Users

**Goal**: To identify and analyze gender bias in coreference resolution systems.

**Target Audience**:
- NLP researchers
- AI developers
- Ethics researchers
- Academics

**Tasks**:
- Coreference resolution
- Bias analysis
- Gender studies

**Limitations**: The Winogender schemas may demonstrate the presence of gender bias but not prove its absence.

**Out of Scope Uses**:
- Evaluation of systems outside of coreference resolution

## 💾 Data

**Source**: U.S. Bureau of Labor Statistics, various textual datasets

**Size**: 720 sentences

**Format**: text

**Annotation**: Validated by human annotators with a 94.9% agreement rate.

## 🔬 Methodology

**Methods**:
- Human validation of sentence templates
- Statistical correlation analysis

**Metrics**:
- Accuracy of coreference resolution
- Bias correlation coefficients

**Calculation**: Statistical measures of bias based on pronoun resolution outcomes.

**Interpretation**: Evaluation of how resolutions are affected by pronoun gender, comparing system performance across different models.

**Baseline Results**: N/A

**Validation**: Sentences validated through crowdsourcing with Mechanical Turk.

## ⚠️ Targeted Risks

**Risk Categories**:
- Gender bias
- Systematic bias reinforcement

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Gender statistics from U.S. Bureau of Labor Statistics correlated with model outputs.

**Potential Harm**: Reinforcement of gender stereotypes through biased model predictions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
