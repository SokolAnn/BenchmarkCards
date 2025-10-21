# T2V-CompBench (Text-to-Video Compositional Benchmark)

## 📊 Benchmark Details

**Name**: T2V-CompBench (Text-to-Video Compositional Benchmark)

**Overview**: T2V-CompBench is a comprehensive benchmark designed for compositional text-to-video generation, consisting of seven categories with 1400 text prompts. It emphasizes compositionality through multiple objects, attributes, actions, and interactions within dynamic scenes, utilizing various MLLM-based, detection-based, and tracking-based evaluation metrics.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/username/T2V-CompBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for compositional text-to-video generation, addressing the rich complexity of actions, attributes, and interactions in generated videos.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text-to-Video Generation

**Limitations**: N/A

## 💾 Data

**Source**: Composed of 1400 text prompts across seven categories generated from real user inputs and verified by humans.

**Size**: 1400 prompts

**Format**: text

**Annotation**: Prompt generation using GPT-4, with human verification for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- MLLM-based evaluation
- Detection-based evaluation
- Tracking-based evaluation

**Metrics**:
- Grid-LLaVA
- D-LLaVA
- G-Dino
- DOT

**Calculation**: Metrics are calculated based on correspondence to human evaluations, with various methods applied based on the category of prompts.

**Interpretation**: A higher score indicates better alignment of generated video content with the corresponding text prompt.

**Baseline Results**: N/A

**Validation**: The validity of the metrics has been established through correlation studies with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
