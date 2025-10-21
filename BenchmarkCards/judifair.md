# JudiFair

## 📊 Benchmark Details

**Name**: JudiFair

**Overview**: JudiFair is an evaluation benchmark comprising 177,100 unique case facts across 65 labels, designed to measure judicial fairness in large language models (LLMs).

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- LEEC

**Resources**:
- [GitHub Repository](https://github.com/THUYRan/LLM-Fairness/blob/main/Toolkit%20Vedio%20Upload.mp4)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate judicial fairness in large language models used in high-stakes decision-making contexts.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Model Developers

**Tasks**:
- Bias Detection
- Fairness Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: JudiFair dataset constructed from legal documents and annotated by legal experts.

**Size**: 177,100 unique case facts

**Format**: Text files

**Annotation**: Annotated by a team of legal experts using a combination of automated and manual methods.

## 🔬 Methodology

**Methods**:
- Statistical Inference
- Regression Analysis
- Bernoulli Tests

**Metrics**:
- Inconsistency
- Bias
- Imbalanced Inaccuracy

**Calculation**: Calculated using regression models controlling for document effects and evaluating statistical significance of label impacts.

**Interpretation**: Results indicate the presence of bias and unfairness patterns among different demographic labels.

**Baseline Results**: Results from 16 LLMs showed significant biases and inconsistencies across multiple demographic labels.

**Validation**: Validated through rigorous statistical testing and expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of demographic factors indicates significant bias against various population segments.

**Potential Harm**: ['Judicial Inequity', 'Social Justice Risks']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information was used; all data sourced from publicly available datasets.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
