# VisualProcessBench

## 📊 Benchmark Details

**Name**: VisualProcessBench

**Overview**: VisualProcessBench is designed to measure the abilities of PRMs and MLLMs to identify erroneous steps in multimodal reasoning tasks, comprising 2,866 samples with step-wise correctness annotations.

**Data Type**: multimodal reasoning questions and step-wise solutions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMMU
- MathVision
- MathVerse
- DynaMath
- WeMath

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of multimodal Process Reward Models (PRMs) and other MLLMs in detecting erroneous reasoning steps.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Error Detection in Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from multimodal reasoning benchmarks including MMMU, MathVision, MathVerse, and others; annotated by human experts.

**Size**: 2,866 samples with 26,950 step-wise correctness labels

**Format**: N/A

**Annotation**: Manually annotated by experts with at least a university degree.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score

**Calculation**: Macro F1 Scores are computed separately for correct and incorrect steps and then averaged.

**Interpretation**: Higher scores indicate better performance in identifying correct and incorrect steps.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
