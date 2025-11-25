# OmniACT

## 📊 Benchmark Details

**Name**: OmniACT

**Overview**: We introduce OmniACT, the first-of-a-kind dataset and benchmark for assessing an agent’s capability to generate executable programs to accomplish computer tasks. The dataset contains over 9.8K pairs of images and instructions for tasks across diverse desktop and web applications.

**Data Type**: image and natural language task pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- WebArena
- Mind2Web
- VisualWebArena

**Resources**:
- [Resource](https://huggingface.co/datasets/Writer/omniact)

## 🎯 Purpose and Intended Users

**Goal**: To provide a platform to measure and evaluate the progress of language model agents in automating computer tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Over 9.8K pairs of images and natural language tasks collected through human annotation.

**Size**: 9,802 examples

**Format**: N/A

**Annotation**: Human annotation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Sequence Score
- Action Score

**Calculation**: Scores are calculated based on the matching of action sequences and the accuracy of action coordinates against given UI elements.

**Interpretation**: Scores reflect the efficiency and correctness of agents in executing tasks based on visual and textual inputs.

**Baseline Results**: Strong baseline performance observed with models such as GPT-4 and others.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
