# MFC-Bench (Multimodal Fact-Checking Benchmark)

## 📊 Benchmark Details

**Name**: MFC-Bench (Multimodal Fact-Checking Benchmark)

**Overview**: MFC-Bench is a rigorous benchmark designed to evaluate the factual accuracy of large vision-language models (LVLMs) across three stages of verdict prediction for multimodal fact-checking: Manipulation Classification, Out-of-Context Classification, and Veracity Classification.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMFakeBench
- COSMOS
- NewsCLIPpings

**Resources**:
- [GitHub Repository](https://github.com/wskbest/MFC-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation platform for the factual accuracy of LVLMs in multimodal fact-checking tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Manipulation Classification
- Out-of-Context Classification
- Veracity Classification

**Limitations**: The current benchmark may not fully capture the complexity of real-world multimodal fact-checking due to the dynamic and context-specific nature of misinformation.

## 💾 Data

**Source**: A mix of diverse datasets specifically designed for multimodal fact-checking.

**Size**: 35,000 examples

**Format**: N/A

**Annotation**: Human evaluation and automated methods for verifying manipulation techniques.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are computed based on the performance of the LVLMs across different tasks in the benchmark.

**Interpretation**: A higher F1 Score indicates better performance in correctly identifying facts vs. non-facts.

**Baseline Results**: Human performance serves as a baseline, significantly outperforming the LVLMs in detection tasks.

**Validation**: Multiple levels of quality assurance checks and evaluations were performed on the collected data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to prevent the spread of misinformation and enhance the trustworthiness of AI systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data utilized in this research does not contain any user information from social media and adheres to the terms of datasets used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all human evaluators involved.

**Compliance With Regulations**: Not Applicable
