# Sylheti-English Benchmark

## 📊 Benchmark Details

**Name**: Sylheti-English Benchmark

**Overview**: This benchmark enhances machine translation evaluation for the Sylheti dialect of Bengali by incorporating reference-free evaluation techniques and facilitating Direct Assessment (DA) scores through a dialect-guided approach.

**Data Type**: Sylheti-English sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali
- English

**Resources**:
- [GitHub Repository](https://github.com/180041123-Atiq/MTEonLowResourceLanguage)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating machine translation in low-resource dialect-rich settings using Large Language Models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: The Sylheti-English benchmark was created by augmenting the existing ONUBAD dataset with additional Sylheti-English sentence pairs and their corresponding Direct Assessment scores from native speakers.

**Size**: 1,500 sentence pairs

**Format**: N/A

**Annotation**: Annotated by native speakers with Direct Assessment scores.

## 🔬 Methodology

**Methods**:
- Regression-based evaluation
- Dialect-guided prompting
- Comparative analysis of multiple LLMs

**Metrics**:
- Pearson correlation coefficient
- Spearman rank correlation coefficient

**Calculation**: Metrics were calculated to evaluate the correlation between predicted Direct Assessment scores and actual ratings from native speakers.

**Interpretation**: Higher correlation scores indicate better alignment with human evaluation, demonstrating stronger performance in machine translation quality assessment.

**Baseline Results**: N/A

**Validation**: Evaluations across multiple LLMs using different prompting strategies showed consistent performance improvements.

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
