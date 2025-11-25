# BackdoorMBTI: A Backdoor Learning Multimodal Benchmark Tool Kit for Backdoor Defense Evaluation

## 📊 Benchmark Details

**Name**: BackdoorMBTI: A Backdoor Learning Multimodal Benchmark Tool Kit for Backdoor Defense Evaluation

**Overview**: BackdoorMBTI is the first backdoor learning toolkit and benchmark designed for multimodal evaluation across three representative modalities from eleven commonly used datasets. It provides a systematic backdoor learning pipeline, encompassing data processing, data poisoning, backdoor training, and evaluation.

**Data Type**: text, image, audio

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio Processing

**Languages**:
- English

**Similar Benchmarks**:
- BackdoorBench
- TrojanZoo

**Resources**:
- [GitHub Repository](https://github.com/SJTUHaiyangYu/BackdoorMBTI)
- [Resource](https://doi.org/10.1145/3690624.3709385)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the research in multimodal backdoor learning and provide a unified benchmark for evaluating backdoor defenses in multimodal contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Backdoor Detection
- Classification

**Limitations**: It currently supports a limited number of datasets and models, and does not yet support all multimodal applications.

## 💾 Data

**Source**: Eleven commonly used datasets including CIFAR10, SST-2, SpeechCommands among others.

**Size**: 110,000 images, 630,000 text instances, 105,829 audio samples

**Format**: N/A

**Annotation**: Manually labeled or sourced datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Attack Success Rate (ASR)
- Detection Accuracy (DAC)

**Calculation**: Metrics are calculated based on the performance of attacks and defenses against the benchmark datasets.

**Interpretation**: Higher accuracy indicates better model performance, while lower ASR indicates more effective defense mechanisms.

**Baseline Results**: N/A

**Validation**: Evaluated through experiments on different datasets and performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under a Creative Commons 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
