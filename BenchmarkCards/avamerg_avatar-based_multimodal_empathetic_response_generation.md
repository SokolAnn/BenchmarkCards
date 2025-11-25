# AvaMERG (Avatar-based Multimodal Empathetic Response Generation)

## 📊 Benchmark Details

**Name**: AvaMERG (Avatar-based Multimodal Empathetic Response Generation)

**Overview**: AvaMERG is a large-scale benchmark dataset designed for Multimodal Empathetic Response Generation (MERG), which incorporates authentic human speech audio and dynamic talking-face avatar videos along with text, enabling the generation of emotionally nuanced and contextually appropriate responses across multiple modalities.

**Data Type**: text, speech audio, talking-head video

**Domains**:
- Natural Language Processing
- Human-centered Computing

**Languages**:
- English

**Similar Benchmarks**:
- Empathetic Dialogue

**Resources**:
- [Resource](https://AvaMERG.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive benchmark for developing and evaluating models that generate empathetic responses across multiple modalities.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Empathetic Response Generation

**Limitations**: N/A

## 💾 Data

**Source**: AvaMERG dataset constructed by augmenting the existing Pure-text Empathetic Dialogue dataset with multimodal signals and identity-specific information.

**Size**: 33,048 dialogues with 152,021 utterances

**Format**: JSON

**Annotation**: Human annotation with cross-checking for content accuracy and emotional accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Emotion Accuracy
- Distinct-1
- Distinct-2
- MOS (Mean Opinion Score)
- CPBD (Cumulative Probability of Blur Detection)
- SSIM (Structural Similarity Index Measure)

**Calculation**: Various evaluation scores calculated to assess consistency and quality of generated responses across text, audio, and video outputs.

**Interpretation**: Scores reflect the emotional accuracy, coherence, and quality of generated multimodal empathetic outputs.

**Baseline Results**: Results show Empatheia model significantly outperforms baselines on multiple metrics.

**Validation**: Comprehensive validation through human evaluation and automated metrics on the AvaMERG dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Dataset includes diverse age, gender, and emotional expression profiles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization and user control over personal data ensured.

**Data Licensing**: Open access under specified terms.

**Consent Procedures**: Informed consent obtained from all participants involved in data collection.

**Compliance With Regulations**: ADheres to data protection regulations like GDPR.
