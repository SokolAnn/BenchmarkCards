# BraFiNER (Brazilian Financial Named Entity Recognition)

## 📊 Benchmark Details

**Name**: BraFiNER (Brazilian Financial Named Entity Recognition)

**Overview**: Development of the BraFiNER, a Portuguese dataset for Named Entity Recognition in finance, using earnings call transcripts from Brazilian banks.

**Data Type**: annotated sentences

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/rsabilio/NerEval-BrazilianCorporateTranscripts)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate mono- and multilingual transformer models for Named Entity Recognition in Brazilian financial texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Earnings call transcripts of Brazilian banks from the Comissao de Valores Mobiliarios (CVM) open data.

**Size**: 384 transcripts, 57,933 annotated sentences

**Format**: CSV

**Annotation**: Weakly supervised annotation using regular expressions and heuristics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the comparisons of annotations and model outputs.

**Interpretation**: Higher values in Precision, Recall, and F1 Score indicate better model performance.

**Baseline Results**: The macro F1-score achieved by the best model ranged from 98.33% to 98.99%.

**Validation**: Results were validated using multiple statistical tests including Friedman and Wilcoxon tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
