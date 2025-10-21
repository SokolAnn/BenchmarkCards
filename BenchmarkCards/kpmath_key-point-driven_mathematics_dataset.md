# KPMath (Key-Point-Driven Mathematics Dataset)

## 📊 Benchmark Details

**Name**: KPMath (Key-Point-Driven Mathematics Dataset)

**Overview**: KPMath is a synthetic dataset tailored for mathematical reasoning, comprising over 800K question-answer pairs. It utilizes a novel Key-Point-Driven Data Synthesis framework to enhance the quality and diversity of mathematical questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K

**Resources**:
- [Resource](https://arxiv.org/abs/2403.02333)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality dataset for training language models on mathematical reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a data synthesis framework (Key-Point-Driven Data Synthesis) leveraging existing mathematical datasets including MATH and GSM8K.

**Size**: 1,576,000 examples

**Format**: JSON

**Annotation**: Automatically generated with quality assessments through consensus scoring.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Quality assessment using GPT-4
- Consensus scoring

**Metrics**:
- PASS@1 accuracy

**Calculation**: Metrics are calculated by evaluating model predictions on test sets like GSM8K and MATH.

**Interpretation**: High PASS@1 accuracy indicates effective performance in mathematical reasoning.

**Baseline Results**: The fine-tuned Qwen1.5-72B model achieved 87.0% PASS@1 accuracy on GSM8K and 58.3% on MATH.

**Validation**: Validation performed by testing on multiple established math reasoning datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
