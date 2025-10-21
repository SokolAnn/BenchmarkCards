# THOS: A Benchmark Dataset for Targeted Hate and Offensive Speech

## 📊 Benchmark Details

**Name**: THOS: A Benchmark Dataset for Targeted Hate and Offensive Speech

**Overview**: THOS is a dataset of 8.3k tweets manually labeled with fine-grained annotations about the target of the message, aimed at improving hate and offensive speech detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mohaimeed/THOS)

## 🎯 Purpose and Intended Users

**Goal**: To support research for creating and evaluating accurate and detailed classifiers of harmful speech on the internet.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected through the Twitter API using keyword search.

**Size**: 8,282 tweets

**Format**: N/A

**Annotation**: Manually labeled by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score
- AUROC

**Calculation**: Metrics were evaluated independently for each TPC and STPC and averaged.

**Interpretation**: Higher accuracy indicates better classification capabilities for hate/offensive speech.

**Baseline Results**: Preliminary results indicate F1 scores above 0.78.

**Validation**: The dataset was used to train LLM-based classifiers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
