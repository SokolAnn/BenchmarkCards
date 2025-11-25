# Codecfake: An Initial Dataset for Detecting LLM-based Deepfake Audio

## 📊 Benchmark Details

**Name**: Codecfake: An Initial Dataset for Detecting LLM-based Deepfake Audio

**Overview**: The Codecfake dataset is proposed for detecting LLM-based deepfake audio, leveraging seven representative neural codecs to generate fake audio, providing a resource for research on audio deepfake detection methodologies.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://huggingface.co/facebook/wav2vec2-xls-r-300m)
- [GitHub Repository](https://github.com/asvspoof-challenge/2021/blob/main/eval-package/eval_metrics.py)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for effectively detecting LLM-based deepfake audio, enhancing detection systems' performance and generalizability.

**Target Audience**:
- ML Researchers
- Audio Processing Engineers

**Tasks**:
- Audio Deepfake Detection

**Limitations**: The dataset may not cover all possible neural codec generation methods which could limit its applicability in real-world scenarios.

## 💾 Data

**Source**: The dataset is generated using seven representative neural codec methods trained on the LibriTTS dataset and evaluated on audio from the VCTK and AISHELL3 datasets.

**Size**: 1,058,216 audio samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Equal Error Rate (EER)

**Calculation**: Metrics are calculated to assess the performance of ADD models on detecting codec-based audio.

**Interpretation**: Lower EER values indicate better detection performance, reflecting the models' ability to correctly identify real versus fake audio.

**Baseline Results**: The baseline results include EER values from vocoder-trained models compared to those trained on the Codecfake dataset.

**Validation**: Performance is validated on both seen (C1-C6) and unseen (C7) conditions with different codec methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: Potential risks related to misclassifying real audio as fake and vice versa, affecting user trust in audio systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
