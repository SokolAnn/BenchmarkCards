# HapticCap

## 📊 Benchmark Details

**Name**: HapticCap

**Overview**: HapticCap is the first fully human-annotated haptic-captioned dataset, containing 92,070 haptic-text pairs for user descriptions of sensory, emotional, and associative attributes of vibrations.

**Data Type**: haptic-text pairs

**Domains**:
- Haptics

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.13318)

## 🎯 Purpose and Intended Users

**Goal**: To create a large multimodal dataset and task for understanding user experiences with vibration haptic signals.

**Target Audience**:
- ML Researchers
- Haptics Designers

**Tasks**:
- Haptic-Caption Retrieval

**Limitations**: HapticCap may not encompass the full range of possible signals and user experiences, and user descriptions are only in English and geographically limited.

## 💾 Data

**Source**: Collected from user studies with diverse participants in controlled lab settings.

**Size**: 92,070 pairs

**Format**: N/A

**Annotation**: Human-annotated with users providing descriptions based on sensory, emotional, and associative perspectives.

## 🔬 Methodology

**Methods**:
- Supervised Learning
- Contrastive Learning

**Metrics**:
- Precision@10
- Recall@10
- Mean Average Precision at 10 (mAP@10)
- Normalized Discounted Cumulative Gain at 10 (nDCG@10)

**Calculation**: Metrics are calculated based on retrieved descriptions' relevance to given haptic signals.

**Interpretation**: Higher values in metrics indicate better retrieval performance.

**Baseline Results**: Comparison of various models trained on combined and individual description categories.

**Validation**: Dataset validated through user agreement scores and diversity checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis includes a breakdown of user demographics and description variety.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data was anonymized and consent obtained from participants.

**Data Licensing**: Dataset expected to be released under Creative Commons Attribution-NonCommercial 4.0 International License.

**Consent Procedures**: User consent obtained prior to participation in the study.

**Compliance With Regulations**: IRB approval was obtained for the collection and management of personal data.
