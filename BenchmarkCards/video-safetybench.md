# Video-SafetyBench

## 📊 Benchmark Details

**Name**: Video-SafetyBench

**Overview**: Video-SafetyBench is the first comprehensive benchmark designed to evaluate the safety of LVLMs under video-text attacks, comprising 2,264 video-text pairs spanning 48 fine-grained unsafe categories.

**Data Type**: video-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MM-SafetyBench
- HADES
- JailbreakV

**Resources**:
- [Resource](https://liuxuannan.github.io/Video-SafetyBench.github.io/)
- [Resource](https://huggingface.co/datasets/BAAI/Video-SafetyBench)
- [GitHub Repository](https://github.com/flageval-baai/Video-SafetyBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the safety of video LVLMs and identify vulnerabilities in model outputs.

**Target Audience**:
- AI Researchers
- Safety Evaluators
- Model Developers

**Tasks**:
- Safety Evaluation
- Video Classification
- Adversarial Testing

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from diverse datasets and generated using controlled pipelines combining LLMs and video synthesis models.

**Size**: 2,264 video-text pairs

**Format**: N/A

**Annotation**: Generated and reviewed using LLM-guided prompts with human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- RJScore

**Calculation**: RJScore is calculated by assessing the confidence of judge models using logit distributions and calibrating decision thresholds through cross-validation.

**Interpretation**: A higher RJScore indicates greater toxicity and risk of harmful outputs.

**Validation**: Video-SafetyBench is validated through extensive evaluations across 24 state-of-the-art LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Prompt injection attack
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
