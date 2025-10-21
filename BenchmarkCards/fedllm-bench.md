# FedLLM-Bench

## 📊 Benchmark Details

**Name**: FedLLM-Bench

**Overview**: FedLLM-Bench is a realistic benchmark for Federated Learning of Large Language Models (FedLLM) that offers comprehensive datasets and establishes 8 training methods and 6 evaluation metrics to evaluate and enhance federated instruction tuning and preference alignment in real-world scenarios.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- French
- Russian
- Portuguese
- Chinese
- Arabic
- Telugu

**Similar Benchmarks**:
- LEAF

**Resources**:
- [GitHub Repository](https://github.com/rui-ye/FedLLM-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic benchmark for evaluating Federated Learning methods in the context of large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Federated Instruction Tuning
- Federated Preference Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Four user-annotated datasets designed for Federated Learning: Fed-Aya, Fed-ChatbotIT, Fed-WildChat, and Fed-ChatbotPA.

**Size**: 100,000 examples

**Format**: N/A

**Annotation**: User-annotated

## 🔬 Methodology

**Methods**:
- Federated Averaging (FedAvg)
- FedProx
- SCAFFOLD
- FedAvgM
- FedAdagrad
- FedYogi
- FedAdam

**Metrics**:
- MT-Bench
- Vicuna
- Ref-GPT4
- MMLU
- HumanEval
- AdvBench

**Calculation**: Metrics are computed based on the evaluation results of the models tested on the datasets within FedLLM-Bench.

**Interpretation**: Higher scores indicate better performance in terms of following user instructions and generating appropriate responses.

**Baseline Results**: FedAdagrad shows the best average performance across the tested methods.

**Validation**: Extensive experiments were conducted to analyze the effectiveness of various federated learning methods on the provided datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: The datasets exhibit diverse language groups representing different demographics.

**Potential Harm**: Potential for data leakage or exposure of sensitive information.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets have been screened for personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
