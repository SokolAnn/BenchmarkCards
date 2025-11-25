# Inconsistency Detection Benchmark

## 📊 Benchmark Details

**Name**: Inconsistency Detection Benchmark

**Overview**: The Inconsistency Detection Benchmark provides a dataset of 698 human-annotated pairs of political statements to facilitate the task of detecting inconsistencies in political discourse. It aims to identify various types of inconsistencies and thereby promote accountability in politics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nursaltyn/Inconsistency Detection Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for detecting inconsistencies in political statements.

**Target Audience**:
- ML Researchers
- Journalists
- Political Analysts

**Tasks**:
- Inconsistency Detection

**Limitations**: N/A

## 💾 Data

**Source**: Dataset includes statements from voting assistant platforms such as Wahl-O-Mat in Germany and Smartvote in Switzerland.

**Size**: 698 examples

**Format**: CSV

**Annotation**: Human-annotated with explanations for selected samples.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on comparisons between model predictions and human-annotated ground truth.

**Interpretation**: Performance is evaluated against multiple classes of inconsistency, with different thresholds for acceptable accuracy based on the complexity of inconsistencies.

**Baseline Results**: ChatGPT-4 turbo and LLaMA 70B models are benchmarked against human performance.

**Validation**: Inter-annotator agreement measured using Krippendorff’s alpha.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
