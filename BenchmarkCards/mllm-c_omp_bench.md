# MLLM-C OMP BENCH

## 📊 Benchmark Details

**Name**: MLLM-C OMP BENCH

**Overview**: A benchmark designed to evaluate the comparative reasoning capability of multimodal large language models (MLLMs) through visually oriented questions spanning eight dimensions of relative comparison.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/RaptorMai/CompBench)
- [Resource](https://compbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To assess the comparative reasoning abilities of multimodal large language models (MLLMs) across various dimensions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Comparative Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from diverse vision datasets through visually oriented questions covering eight dimensions of relativity, including comparative reasoning tasks between image pairs.

**Size**: 39,800 triplets

**Format**: JSON

**Annotation**: Manual annotation by human annotators for accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by comparing model predictions with ground-truth answers for each question in the benchmark.

**Interpretation**: A question is answered correctly if the model's prediction exactly matches the ground-truth answer.

**Baseline Results**: GPT-4V reached an accuracy of 74.7% on the benchmark test split.

**Validation**: Cross-verification by multiple annotators to ensure quality and consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
