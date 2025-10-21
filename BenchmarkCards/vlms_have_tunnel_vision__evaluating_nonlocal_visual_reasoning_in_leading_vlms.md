# VLMs have Tunnel Vision: Evaluating Nonlocal Visual Reasoning in Leading VLMs

## 📊 Benchmark Details

**Name**: VLMs have Tunnel Vision: Evaluating Nonlocal Visual Reasoning in Leading VLMs

**Overview**: We present an evaluation that tests vision-language models’ capacity for nonlocal visual reasoning - reasoning that requires chaining evidence collected from multiple, possibly distant, regions of an image. Our structured evaluation suite allows us to see if VLMs can perform similar visual algorithms to humans, focusing on three types of nonlocal reasoning: comparative perception, saccadic search, and smooth visual search. Our findings show that current models lack core visual reasoning capabilities.

**Data Type**: image-question pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- HallusionBench

**Resources**:
- [Resource](https://arxiv.org/abs/2507.13361)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the nonlocal visual reasoning capabilities of vision-language models and to identify their limitations in basic perceptual tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Comparative perception
- Saccadic search
- Smooth visual search

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic image-question pairs generated specifically for this evaluation.

**Size**: 1,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluation metrics calculated based on the models' ability to correctly perform tasks on the provided image-question pairs.

**Interpretation**: Accuracy scores are interpreted based on the models' performance relative to the human baseline.

**Baseline Results**: Humans achieved 100% accuracy on most tasks while VLMs performed significantly below this level.

**Validation**: Tasks were validated through trials with human evaluators to establish a baseline performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
