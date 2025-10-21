# VaxConcerns

## 📊 Benchmark Details

**Name**: VaxConcerns

**Overview**: VaxConcerns is a disease-agnostic taxonomy of vaccine concerns organized into parent categories and child classes, used for the hierarchical multi-label classification of text related to vaccine issues.

**Data Type**: passage-label pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the VaxConcerns benchmark is to detect vaccine concerns in online discourse using large language models in a zero-shot setting.

**Target Audience**:
- ML Researchers
- Public Health Officials

**Tasks**:
- Hierarchical Multi-Label Classification

**Limitations**: The dataset focuses exclusively on anti-vaccination blog text, which may not generalize to other domains.

## 💾 Data

**Source**: The VaxConcerns dataset is composed of passage-label pairs sourced from expert annotations of anti-vaccination texts.

**Size**: 4,800 passage-label pairs

**Format**: N/A

**Annotation**: Labeled by experts through multiple rounds of consensus.

## 🔬 Methodology

**Methods**:
- Classification using Large Language Models
- Prompting strategies

**Metrics**:
- F1 Score

**Calculation**: F1 scores are calculated against expert-determined ground-truth values using a macro-average.

**Interpretation**: Scores reflect the model's accuracy in detecting vaccine concerns as defined within the VaxConcerns taxonomy.

**Baseline Results**: The best-performing model achieves an F1 score of 78.65%, surpassing human annotation baselines.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
