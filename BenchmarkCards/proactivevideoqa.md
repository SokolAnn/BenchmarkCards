# ProactiveVideoQA

## 📊 Benchmark Details

**Name**: ProactiveVideoQA

**Overview**: ProactiveVideoQA is the first comprehensive benchmark designed to evaluate the proactive interaction capabilities of Multimodal Large Language Models (MLLMs) during video playback. It focuses on systems' abilities to engage users by determining when to respond as relevant information appears over time.

**Data Type**: video

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VideoQA
- TVQA
- Ego4D Goalstep

**Resources**:
- [GitHub Repository](https://github.com/yellow-binary-tree/ProactiveVideoQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and promote the development of proactive interaction capabilities in video multimodal systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Video Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Collected from multiple datasets including Shot2story-MAGQA-39k, Ego4D Goalstep, TVQA, and UCF-Crime.

**Size**: 1,377 videos

**Format**: N/A

**Annotation**: Annotations provided include questions, answers, and relevant timestamps. Generated from dense captions and manual descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User study

**Metrics**:
- PAUC (Proactive Area Under Curve)

**Calculation**: PAUC is calculated based on the temporal evolution of response quality and is designed to account for timing and accuracy of model outputs.

**Interpretation**: Higher PAUC scores indicate better alignment with user experience in proactive interactions.

**Baseline Results**: N/A

**Validation**: Validated through comparison of model performance against human preferences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
