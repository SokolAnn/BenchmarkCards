# ECV A (Exploring the Causation of Video Anomalies)

## 📊 Benchmark Details

**Name**: ECV A (Exploring the Causation of Video Anomalies)

**Overview**: ECV A is a comprehensive benchmark for causation understanding of video anomalies, consisting of 2,240 video clips with detailed human annotations. It addresses the 'what', 'why', and 'how' of video anomalies.

**Data Type**: video with human annotations

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Dulpy/ECV A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale benchmark for causation understanding of video anomalies.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Anomaly Classification
- Anomaly Reasoning
- Anomaly Effect Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from video platforms such as Bilibili and YouTube.

**Size**: 2,240 video clips totaling 88.16 hours.

**Format**: N/A

**Annotation**: Manually annotated with detailed descriptions of anomalies, causes, and effects.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- AnomEval

**Calculation**: AnomEval assesses the ability of VLMs to understand anomalous events based on a combination of basic reasoning, consistency, and hallucination checks.

**Interpretation**: Higher scores on AnomEval indicate better understanding of the causative relationships in video anomalies.

**Baseline Results**: AnomShield achieved state-of-the-art performance on the ECV A benchmark.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
