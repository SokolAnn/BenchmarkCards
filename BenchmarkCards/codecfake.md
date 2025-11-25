# Codecfake

## 📊 Benchmark Details

**Name**: Codecfake

**Overview**: Codecfake is a large-scale dataset for detecting ALM-based deepfake audio, comprising over 1 million audio samples in both English and Chinese, designed to tackle challenges in audio deepfake detection and improve generalization capabilities across diverse test conditions.

**Data Type**: audio

**Domains**:
- Audio Deepfake Detection

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://zenodo.org/records/13838106)
- [GitHub Repository](https://github.com/xieyuankun/Codecfake)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for the detection of ALM-based deepfake audio and advance research in audio deepfake detection methods.

**Target Audience**:
- ML Researchers
- Audio Signal Processing Engineers
- AI Practitioners

**Tasks**:
- Audio Deepfake Detection

**Limitations**: The current dataset only includes clean audio conditions, lacking robustness in complex real-world noise environments.

## 💾 Data

**Source**: Comprises audio samples generated from a variety of neural audio codec models.

**Size**: 1,058,216 audio samples

**Format**: Audio files

**Annotation**: Generated algorithmically using codecs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Equal Error Rate (EER)

**Calculation**: EER calculated during evaluation on different test conditions including codings and unseen audio types.

**Interpretation**: Lower average EER indicates better performance in distinguishing between real and fake audio samples.

**Validation**: The validation of the dataset was done through its application in training and testing audio deepfake detection models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
