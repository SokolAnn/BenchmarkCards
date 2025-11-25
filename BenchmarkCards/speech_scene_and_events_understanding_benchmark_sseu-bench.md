# Speech, Scene and Events Understanding Benchmark (SSEU-Bench)

## 📊 Benchmark Details

**Name**: Speech, Scene and Events Understanding Benchmark (SSEU-Bench)

**Overview**: SSEU-Bench is the first versatile audio understanding benchmark that explicitly accounts for energy differences between speech and non-speech audio, with both independent and joint understanding settings for speech, scene, and events.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenAQA
- Open-ASQA
- AudioBench
- AIR-Bench
- MMAU

**Resources**:
- [Resource](https://sites.google.com/view/sseu-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the audio understanding capabilities of Large Audio Language Models (LALMs) in joint analysis of speech, scene, and events within the same audio clip.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Automatic Speech Recognition
- Acoustic Scene Classification
- Audio Tagging

**Limitations**: N/A

## 💾 Data

**Source**: Mixed audio samples consisting of clean speech clips from the VCTK corpus and non-speech background audio clips from existing SED datasets, curated to create varying SNR levels.

**Size**: 21.72 hours of audio data

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Word Error Rate (WER)
- Macro-average Accuracy (mACC)
- Mean Average Precision (mAP)

**Calculation**: WER is calculated based on the accuracy of transcribing spoken content, mACC evaluates classification accuracies for scenes, and mAP measures accuracy for event identification.

**Interpretation**: Lower WER indicates better performance in speech understanding; higher mACC and mAP indicate better performance in scene classification and event tagging respectively.

**Baseline Results**: N/A

**Validation**: Results are validated through comparison with ground truth as well as across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
