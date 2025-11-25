# DsDm (Dataset Selection with Datamodels)

## 📊 Benchmark Details

**Name**: DsDm (Dataset Selection with Datamodels)

**Overview**: The paper presents a new method for dataset selection in training large-scale models, specifically aimed at maximizing model performance during training by selecting optimal data subsets for given target tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD (Stanford Question Answering Dataset)
- LAMBADA (LAnguage Modeling Broadened to Account for Discourse Aspects)
- Jeopardy

**Resources**:
- [Resource](https://arxiv.org/abs/2401.12926)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of large-scale language models through optimal dataset selection by modeling the impact of training data on target task performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Dataset Selection
- Language Modeling

**Limitations**: N/A

## 💾 Data

**Source**: The English subset of C4 (Colossal Cleaned Common Crawl)

**Size**: 216,948,746 examples

**Format**: text

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Cross-Validation

**Metrics**:
- Log-Probability
- Accuracy

**Calculation**: Mean log-probability is calculated based on model predictions across benchmark samples.

**Interpretation**: A higher log-probability indicates better performance in generating correct answers.

**Baseline Results**: Models trained with the proposed method (DsDm) outperform traditional dataset selection methodologies.

**Validation**: Evaluated on a range of standard benchmarks related to language understanding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Data poisoning
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
