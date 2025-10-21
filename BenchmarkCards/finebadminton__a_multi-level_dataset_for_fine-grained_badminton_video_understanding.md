# FineBadminton: A Multi-Level Dataset for Fine-Grained Badminton Video Understanding

## 📊 Benchmark Details

**Name**: FineBadminton: A Multi-Level Dataset for Fine-Grained Badminton Video Understanding

**Overview**: FineBadminton features a unique multi-level semantic annotation hierarchy for comprehensive badminton understanding. It provides a novel and large-scale dataset aimed at fine-grained analysis of badminton videos, evaluating MLLMs on nuanced spatio-temporal reasoning and tactical comprehension.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- FineGym
- SoccerNet
- FineSports
- ShuttleSet

**Resources**:
- [Resource](https://finebadminton.github.io/FineBadminton/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and in-depth dataset for analyzing badminton gameplay and to evaluate multimodal large language models (MLLMs) on fine-grained video understanding tasks.

**Target Audience**:
- ML Researchers
- Sports Analysts
- Model Developers

**Tasks**:
- Action Classification
- Spatio-temporal Reasoning
- Tactical Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Publicly accessible professional badminton match videos released by the Badminton World Federation on YouTube.

**Size**: 3,215 rally clips (33,325 strokes)

**Format**: N/A

**Annotation**: Multi-level semantic annotations including Foundational Actions, Tactical Semantics, and Decision Evaluation created through a combination of human annotation and MLLM-generated proposals.

## 🔬 Methodology

**Methods**:
- MLLM-driven annotation pipeline
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Performance on tasks is calculated based on accuracy for multiple-choice questions and a scoring system for open-ended responses using GPT-4.

**Interpretation**: Higher accuracy indicates better understanding of the fine-grained actions and strategies within badminton videos.

**Baseline Results**: Competing MLLMs were tested, showing competitive accuracy improvements with the proposed strategies.

**Validation**: Extensive experiments validating the utility of the dataset, measuring model performance against various benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
