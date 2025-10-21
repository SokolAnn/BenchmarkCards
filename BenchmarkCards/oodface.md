# OODFace

## 📊 Benchmark Details

**Name**: OODFace

**Overview**: OIDFace explores the OOD challenges faced by facial recognition models from two perspectives: common corruptions and appearance variations, systematically designed with 30 OOD scenarios across 9 categories. This results in three robustness benchmarks: LFW-C/V, CFP-C/V, and YTF-C/V, aimed at evaluating the robustness of face recognition systems against various OOD factors.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- LFW
- CFP
- YTF

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for assessing the robustness of facial recognition models against common corruptions and appearance variations in out-of-distribution scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Facial Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Public datasets used to test benchmarks: LFW, CFP-FP, YTF.

**Size**: 3 benchmarks (LFW-C/V, CFP-C/V, YTF-C/V), 150 unique corruptions and variations

**Format**: N/A

**Annotation**: Augmented existing public datasets to create challenging conditions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Performance calculated as the average accuracy across all models on each corruption or variation type.

**Interpretation**: Higher accuracy indicates better robustness against OOD challenges.

**Baseline Results**: N/A

**Validation**: Validated through extensive experiments on 19 facial recognition models and 3 commercial APIs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Facial recognition technology may lead to privacy concerns and ethical implications regarding surveillance.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Explicit consent obtained from participants for data collection and usage in research.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided consent before data collection.

**Compliance With Regulations**: Study adheres to ethical guidelines and privacy regulations.
