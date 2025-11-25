# Omni-SafetyBench

## 📊 Benchmark Details

**Name**: Omni-SafetyBench

**Overview**: Omni-SafetyBench is the first comprehensive parallel benchmark designed specifically for the safety evaluation of omni-modal large language models (OLLMs), featuring 24 modality variations with 972 samples each, including audio-visual harm cases.

**Data Type**: text, audio, video, image

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio Processing

**Languages**:
- English

**Similar Benchmarks**:
- MM-SafetyBench

**Resources**:
- [GitHub Repository](https://github.com/THU-BPM/Omni-SafetyBench)
- [Resource](https://huggingface.co/datasets/Leyiii/Omni-SafetyBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the safety performance of omni-modal large language models under diverse audio-visual inputs and assess cross-modal safety consistency.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Safety Evaluation
- Cross-Modal Consistency Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Derived from an existing seed dataset (MM-SafetyBench) with transformed modalities.

**Size**: 23,328 total samples

**Format**: N/A

**Annotation**: Generated using a variety of multimedia generation methods, including text-to-speech and diffusion-based transformations.

## 🔬 Methodology

**Methods**:
- Safety evaluation on individual modality variations
- Cross-modal safety consistency assessment

**Metrics**:
- Conditional Attack Success Rate (C-ASR)
- Conditional Refusal Rate (C-RR)
- Safety-score
- Cross-Modal Safety Consistency score (CMSC-score)

**Calculation**: Safety-score is calculated based on a combination of C-ASR and C-RR, prioritizing the safety concerns in derived outputs.

**Interpretation**: A higher Safety-score indicates better safety performance of the model under evaluation.

**Baseline Results**: Evaluated 10 state-of-the-art OLLMs; only 3 models achieved an average Safety-score above 0.6.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Harmful outputs related to audio-visual processing']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
