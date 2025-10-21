# ColorBlindnessEval

## 📊 Benchmark Details

**Name**: ColorBlindnessEval

**Overview**: ColorBlindnessEval is a novel benchmark designed to evaluate the robustness of Vision-Language Models (VLMs) in visually adversarial scenarios inspired by the Ishihara color blindness test, comprising 500 Ishihara-like images challenging VLMs to accurately recognize numerical information embedded in complex visual patterns.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- ColorFoil
- BlindTest

**Resources**:
- [GitHub Repository](https://github.com/ApplyU-ai/ColorBlindnessEval)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and improve the reliability of Vision-Language Models (VLMs) in real-world applications requiring accurate visual recognition.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Visual Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Dataset generated based on the Ishihara Test principles using a unique data generation pipeline.

**Size**: 500 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the ratio of correct predictions to total predictions.

**Interpretation**: Higher accuracy indicates better model performance in recognizing numbers in adversarial contexts.

**Baseline Results**: N/A

**Validation**: Evaluated across multiple VLMs using both Yes/No and open-ended prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Hallucination
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
