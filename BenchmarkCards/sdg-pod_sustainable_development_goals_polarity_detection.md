# SDG-POD (Sustainable Development Goals POlarity Detection)

## 📊 Benchmark Details

**Name**: SDG-POD (Sustainable Development Goals POlarity Detection)

**Overview**: SDG-POD is a benchmark dataset designed specifically for the task of polarity detection in the context of Sustainable Development Goals (SDGs). It combines manually annotated and synthetically generated data to facilitate the training and evaluation of large language models in determining whether a text indicates progress toward a specific SDG or conveys intention to achieve such progress.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/vincenzodeleo/sdg_polarity_detection/tree/main)
- [Resource](https://zenodo.org/records/5550238)

## 🎯 Purpose and Intended Users

**Goal**: To support research in the area of SDG polarity detection and advance the methodological toolkit for sustainability monitoring.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Polarity Detection

**Limitations**: N/A

## 💾 Data

**Source**: The dataset contains 6,400 texts sampled from the OSDG community dataset, which is derived from publicly available documents such as reports, policy documents, and publication abstracts, annotated with respect to 16 different SDGs.

**Size**: 6,400 texts

**Format**: N/A

**Annotation**: The training set was automatically annotated using multiple LLMs, and the test set was annotated by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on standard evaluation procedures for single-label, multi-class classification tasks.

**Interpretation**: Results are interpreted based on F1 scores, detailing performance across different SDGs and classifications.

**Baseline Results**: The QWQ-32B model achieved the highest F1 score of 61.6% after fine-tuning.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
