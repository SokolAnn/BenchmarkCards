# PRISM (Privacy-aware Evaluation of Responses in Sensitive Modalities)

## 📊 Benchmark Details

**Name**: PRISM (Privacy-aware Evaluation of Responses in Sensitive Modalities)

**Overview**: PRISM is a comprehensive benchmark designed to assess Multimodal Large Language Models (MLLMs) on their ability to refuse biometric-related queries and mitigate implicit biometric leakage in open-ended responses while maintaining semantic faithfulness.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- PrivBench
- PrivQA

**Resources**:
- [Resource](https://huggingface.co/datasets/kyh9191/Safe-LLaVA)
- [GitHub Repository](https://github.com/Kimyounggun99/Safe-LLaVA.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate MLLMs' ability to handle biometric privacy concerns effectively.

**Target Audience**:
- ML Researchers
- Model Developers
- Privacy Advocates

**Tasks**:
- Explicit Refusal Assessment
- Implicit Leakage Detection

**Limitations**: N/A

## 💾 Data

**Source**: Images and questions/answers curated specifically for evaluating biometric privacy.

**Size**: 2,000 images with 26,000 QA pairs

**Format**: JSON

**Annotation**: Manually annotated for explicit and implicit biometric attributes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Refusal Accuracy
- Leakage Protection Score

**Calculation**: Refusal Accuracy is calculated based on the percentage of correctly refused biometric-related queries; Leakage Protection Score reflects the extent of hidden biometric implications in model-generated responses.

**Interpretation**: Higher scores indicate more effective refusal behavior and better protection against implicit biometric disclosure.

**Baseline Results**: Safe-LLaV A models consistently achieve high refusal accuracy and low implicit leakage compared to baseline models.

**Validation**: Evaluated using multiple Judges and metrics for robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of biometric trait distribution across varied demographics in the benchmark datasets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures are implemented to avoid revealing personal biometric information through model responses.

**Data Licensing**: The Safe-LLaVA dataset is licensed under Apache License 2.0.

**Consent Procedures**: Not applicable as dataset is derived from publicly available images.

**Compliance With Regulations**: The benchmark aligns with GDPR principles regarding the handling of sensitive biometric data.
