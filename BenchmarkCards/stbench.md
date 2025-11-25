# STBench

## 📊 Benchmark Details

**Name**: STBench

**Overview**: STBench serves as a comprehensive evaluation framework assessing the ability of large language models in spatio-temporal analysis, consisting of 13 distinct tasks and over 60,000 question-answer pairs across four dimensions: knowledge comprehension, spatio-temporal reasoning, accurate computation, and downstream applications.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LwbXc/STBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of STBench is to evaluate the spatio-temporal understanding capabilities of large language models through a systematic assessment of their performance on various tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Knowledge Comprehension
- Spatio-Temporal Reasoning
- Accurate Computation
- Downstream Applications

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various datasets including Yelp, New Orleans Region Dataset, Xi’an Dataset, EULUC Dataset, and Geolife Dataset.

**Size**: 60,000 question-answer pairs

**Format**: JSON

**Annotation**: Manually curated and verified

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the correctness of the model's responses compared to the ground truth answers.

**Interpretation**: An accuracy of 100% indicates perfect performance, while lower percentages highlight areas of improvement.

**Baseline Results**: N/A

**Validation**: Performance across 13 large language models evaluated on STBench tasks

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
