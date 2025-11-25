# TuringQ

## 📊 Benchmark Details

**Name**: TuringQ

**Overview**: TuringQ is designed to evaluate the reasoning capabilities of large language models (LLMs) in the theory of computation, consisting of 4,006 undergraduate and graduate-level question-answer pairs categorized into four difficulty levels and covering seven core theoretical areas.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIG-Bench

**Resources**:
- [Resource](https://huggingface.co/datasets/TuringQ)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for assessing LLMs' understanding of computational theory and driving advancements in enhancing their skills.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available exam sets and homework solutions from universities worldwide, validated by domain experts.

**Size**: 4,006 question-answer pairs

**Format**: N/A

**Annotation**: Expert-reviewed and edited for quality

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Binary accuracy
- Exact alignment

**Calculation**: Binary accuracy is calculated as the percentage of valid responses classified as 'valid' (scores 3-4).

**Interpretation**: Higher scores indicate superior quality, with binary accuracy representing the proportion of valid responses.

**Baseline Results**: N/A

**Validation**: Majority voting among human evaluators for final scoring.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All questions sourced from publicly available materials with proper attribution.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
