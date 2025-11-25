# CANDY

## 📊 Benchmark Details

**Name**: CANDY

**Overview**: CANDY is a benchmark designed to systematically evaluate the capabilities and limitations of large language models in fact-checking Chinese misinformation, including a curated dataset of approximately 20,000 instances.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CHEF

**Resources**:
- [GitHub Repository](https://github.com/SCUNLP/CANDY)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation and in-depth analysis of large language models’ ability to fact-check Chinese misinformation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact-Checking Conclusion
- Fact-Checking Explanation
- LLM-Assisted Fact-Checking

**Limitations**: N/A

## 💾 Data

**Source**: Collected from authoritative Chinese fact-checking platforms such as the China Internet United Rumor Refutation Platform.

**Size**: 20,435 entries

**Format**: JSON

**Annotation**: Manual annotation by a team of annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated using micro-averaging methods.

**Interpretation**: Higher metrics indicate better fact-checking performance.

**Baseline Results**: Baseline models include sixteen large language models and three large reasoning models.

**Validation**: Validation procedures involved inter-rater reliability checks using Fleiss' Kappa.

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
