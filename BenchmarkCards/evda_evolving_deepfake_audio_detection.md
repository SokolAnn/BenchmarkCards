# EVDA (EVolving Deepfake Audio Detection)

## 📊 Benchmark Details

**Name**: EVDA (EVolving Deepfake Audio Detection)

**Overview**: EVDA is a benchmark for evaluating continual learning methods in deepfake audio detection, encompassing classic and newly emerging datasets, and supporting various continual learning algorithms.

**Data Type**: audio

**Domains**:
- Computer Vision

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/Cecile-hi/Evolving-FAD-CL-Benchmark.git)

## 🎯 Purpose and Intended Users

**Goal**: To address the challenges posed by evolving deepfake audio generation techniques using continual learning approaches.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Audio Deepfake Detection

**Limitations**: The scope of continual learning methods explored is limited, and the benchmark may not fully capture the diversity of audio deepfakes encountered in practice.

## 💾 Data

**Source**: Various datasets including Anti-Spoofing Voice series and Chinese fake audio detection datasets.

**Size**: 16,000 samples per task

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Elastic Weight Consolidation (EWC)
- Learning without Forgetting (LwF)
- Regularized Adaptive Weight Modification (RAWM)
- Radian Weight Modification (RWM)

**Metrics**:
- Equal Error Rate (EER)

**Calculation**: EER is calculated to evaluate performance across tasks.

**Interpretation**: Lower EER values indicate better performance.

**Baseline Results**: Replay and EWC showed the lowest average EER across tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
