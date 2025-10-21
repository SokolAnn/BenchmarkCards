# VELOCITI

## 📊 Benchmark Details

**Name**: VELOCITI

**Overview**: VELOCITI is a benchmark to study Video-LLMs by disentangling and assessing the comprehension of agents, actions, and their associations across multiple events in videos. It adopts a video-language entailment setup with strict scoring metrics.

**Data Type**: video-language entailment pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AGQA
- STAR
- ContrastSets

**Resources**:
- [Resource](https://katha-ai.github.io/projects/velociti)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the compositional reasoning capabilities of video-language models through structured tests covering various aspects of agent and action understanding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video-Language Compositional Reasoning

**Limitations**: The benchmark is not intended for evaluating all abilities of Video-LLMs but focuses on compositionality.

## 💾 Data

**Source**: Videos are sourced from the VidSitu dataset, which includes annotations for multiple events.

**Size**: 3,101 video-language pairs

**Format**: N/A

**Annotation**: Annotations include semantic role labeling and captions generated via an open LLM.

## 🔬 Methodology

**Methods**:
- Strict VLE
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Strict VLE requires models to proactively identify positive and negative captions correctly, offering a binary 'Yes' or 'No' response.

**Interpretation**: Models are expected to predict 'Yes' for aligned captions and 'No' for misaligned ones. A correct prediction is a sample where the positive caption scores higher than the threshold while the negative caption scores below the threshold.

**Baseline Results**: The best performing model, Gemini-1.5-Pro, achieves 49.3% accuracy compared to human performance at 93.0%.

**Validation**: Quality control of test samples is performed through human verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
