# Live-E2T (Real-time Threat Monitoring in Video via Deduplicated Event Reasoning and Chain-of-Thought)

## 📊 Benchmark Details

**Name**: Live-E2T (Real-time Threat Monitoring in Video via Deduplicated Event Reasoning and Chain-of-Thought)

**Overview**: Live-E2T is a novel framework for real-time threat monitoring that identifies threatening behaviors in video streams and provides reasoning and assessment of threat events through explanatory text. It uniquely combines high performance and explainability through its hierarchical understanding mechanism, event deduplication, and fine-tuned language model.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- XD-Violence
- UCF-Crime

**Resources**:
- [Resource](https://arxiv.org/abs/2509.18571)

## 🎯 Purpose and Intended Users

**Goal**: To develop a robust, real-time threat monitoring system capable of accurate threat detection and providing interpretable reasoning for decision-making.

**Target Audience**:
- ML Researchers
- Security Practitioners
- Surveillance Technology Developers

**Tasks**:
- Threat Detection
- Video Analysis

**Limitations**: N/A

## 💾 Data

**Source**: XD-Violence, UCF-Crime, Real Life Violence Situations Dataset, Large-scale Anomaly Detection dataset

**Size**: 120 videos (high-quality evaluation subset)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Area Under the Curve (AUC)
- Average Precision (AP)

**Calculation**: Metrics are calculated based on standard evaluation paradigms and comparative analysis with existing methods.

**Interpretation**: Higher scores indicate better performance in threat detection and explainability.

**Baseline Results**: Achieved AP of 91.38% on XD-Violence and AUC of 90.53% on UCF-Crime.

**Validation**: Extensive experiments were conducted to validate performance against state-of-the-art methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
