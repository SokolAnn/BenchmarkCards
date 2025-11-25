# HealthBench

## 📊 Benchmark Details

**Name**: HealthBench

**Overview**: HealthBench is a large-scale, physician-curated benchmark comprising 5,000 clinically realistic examples designed to evaluate the performance of large language models in realistic healthcare scenarios.

**Data Type**: conversational exchanges

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- USMLE

**Resources**:
- [Resource](https://doi.org/10.48550/arXiv.2505.08775)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models on their ability to generate high-quality, accurate, situationally aware answers to clinical questions in real-world contexts.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Clinical Decision Support
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of clinician-validated interactions that include various patient queries and model responses evaluated by expert rubric criteria.

**Size**: 5,000 examples

**Format**: N/A

**Annotation**: Expert annotation by physicians using a rubric-based framework.

## 🔬 Methodology

**Methods**:
- Rubric-based evaluation
- Performance scoring

**Metrics**:
- Accuracy
- Completeness
- Instruction Following
- Context Awareness

**Calculation**: Scores are normalized based on point values assigned to rubric criteria, allowing for interpretability.

**Interpretation**: Higher scores indicate better model performance across various clinical behavior dimensions.

**Baseline Results**: DR.INFO achieved an HB score of 0.51 on the Hard subset of HealthBench.

**Validation**: Performance validation through comparison against frontier LLMs and other clinical assistants using the same benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
