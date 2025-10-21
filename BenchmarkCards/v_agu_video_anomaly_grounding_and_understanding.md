# V AGU (Video Anomaly Grounding and Understanding)

## 📊 Benchmark Details

**Name**: V AGU (Video Anomaly Grounding and Understanding)

**Overview**: V AGU is the first benchmark that integrates anomaly grounding and anomaly understanding in video anomaly detection, providing annotations for anomaly category, semantic explanation, precise temporal grounding, and Video QA.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating and enabling video anomaly detection methods that integrate semantic understanding and temporal grounding.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Anomaly Classification
- Anomaly Understanding
- Anomaly Grounding
- Video Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Integrated from public datasets (CUV A, UCF-Crime, XD-Violence) and collected 7,567 high-quality anomalous videos from platforms like YouTube, BiliBili, and TikTok.

**Size**: 7,567 videos

**Format**: N/A

**Annotation**: Manual annotation with human verification involving multiple annotators.

## 🔬 Methodology

**Methods**:
- Evaluation of anomaly classification, understanding, and grounding capabilities; Video Question Answering

**Metrics**:
- JeAUG (Joint Evaluation of Anomaly Understanding and Detection)

**Calculation**: JeAUG combines scores of semantic accuracy and grounding precision, adjusting scores based on video length.

**Interpretation**: JeAUG scores represent the effectiveness in both anomaly understanding and grounding tasks.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted on the proposed benchmark demonstrate its robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data acquisition strictly complies with copyright regulations and implements privacy protection for identifiable features.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study adheres to ethical guidelines regarding data handling and participant protection.
