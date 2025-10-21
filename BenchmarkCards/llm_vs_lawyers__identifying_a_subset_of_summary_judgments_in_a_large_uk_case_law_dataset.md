# LLM vs. Lawyers: Identifying a Subset of Summary Judgments in a Large UK Case Law Dataset

## 📊 Benchmark Details

**Name**: LLM vs. Lawyers: Identifying a Subset of Summary Judgments in a Large UK Case Law Dataset

**Overview**: This study introduces a methodology for identifying summary judgment cases from the Cambridge Law Corpus using two computational methods: a traditional NLP approach and a large language model (LLM), effectively demonstrating the utility of NLP technologies in legal research.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- Cambridge Law Corpus

**Resources**:
- [GitHub Repository](https://github.com/Anaffinis/LLM-vs-Lawyers)
- [Resource](https://doi.org/10.17863/CAM.100221)

## 🎯 Purpose and Intended Users

**Goal**: To accurately identify summary judgment cases within a large corpus of UK court decisions to support legal research.

**Target Audience**:
- Legal Researchers
- Lawyers
- AI Practitioners

**Tasks**:
- Case Identification
- Legal Text Classification

**Limitations**: This study may not encompass all summary judgments delivered by the courts.

## 💾 Data

**Source**: Cambridge Law Corpus (CLC)

**Size**: 356,011 cases

**Format**: XML

**Annotation**: Manually reviewed and identified by legal experts and analyzed using computational methods.

## 🔬 Methodology

**Methods**:
- Traditional NLP methods
- Large Language Model analysis

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated for each method based on precision and recall.

**Interpretation**: An F1 Score closer to 1 indicates better classification performance.

**Baseline Results**: Traditional NLP based approach achieved an F1 score of 0.78; LLM approach achieved an F1 score of 0.94.

**Validation**: Manual review of sampled data to ensure accurate identification of summary judgment cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misclassification of non-summary judgment cases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
