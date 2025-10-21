# Multi-P2A (Multi-perspective Benchmark on Privacy Assessment for Large Vision-Language Models)

## 📊 Benchmark Details

**Name**: Multi-P2A (Multi-perspective Benchmark on Privacy Assessment for Large Vision-Language Models)

**Overview**: Multi-P2A is a comprehensive benchmark for evaluating the privacy preservation capabilities of large vision-language models (LVLMs) in terms of privacy awareness and leakage. The benchmark covers 26 categories of personal privacy, 15 categories of trade secrets, and 18 categories of state secrets, totaling 31,962 samples. It assesses the model’s ability to recognize privacy sensitivity in input data and the risk of unintentionally disclosing private information in its output.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TrustLLM
- MultiTrust

**Resources**:
- [Resource](https://arxiv.org/abs/2412.19496)

## 🎯 Purpose and Intended Users

**Goal**: To systematically analyze the limitations and vulnerabilities inherent in existing privacy preservation mechanisms of LVLMs, and to inform the development of more robust privacy-preserving models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Privacy Awareness
- Privacy Leakage
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from existing datasets and social media platforms, including a mix of personal images, trade secrets, and state secrets.

**Size**: 31,962 samples

**Format**: N/A

**Annotation**: Manually filtered and annotated to ensure high quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Pearson correlation coefficient
- Refuse-to-Answer (RtA)
- Expect-to-Answer (EtA)

**Calculation**: Metrics are calculated based on the model's performance in recognizing privacy-sensitive data and tasks related to privacy awareness and leakage.

**Interpretation**: Higher accuracy signifies stronger privacy awareness, and RtA reflects the model's ability to preserve privacy by refusing to answer sensitive questions.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Images collected are for academic research purposes and adhere to privacy standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
