# ANPMI (Asymmetric NPMI)

## 📊 Benchmark Details

**Name**: ANPMI (Asymmetric NPMI)

**Overview**: ANPMI is a novel metric designed to evaluate the true comprehension capabilities of language models in multiple-choice tasks by normalizing Pointwise Mutual Information with the objective of reducing the influence of prior probability. It aims to provide a reliable assessment of a model's understanding of prompts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HellaSwag
- PiQA
- ARC
- LogiQA
- RACE
- SciQ
- MMLU

**Resources**:
- [Resource](https://arxiv.org/abs/2502.18798)

## 🎯 Purpose and Intended Users

**Goal**: To accurately measure the natural language understanding capabilities of language models using a normalized metric that reduces bias.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multiple Choice Question Answering

**Limitations**: ANPMI may not be suitable for benchmarks where the model's choice is as critical as understanding the prompt.

## 💾 Data

**Source**: Experiments conducted on seven multiple-choice benchmarks using pre-trained language models.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation with language models using various benchmarks

**Metrics**:
- ANPMI
- Accuracy
- PMI
- Length-normalized Accuracy

**Calculation**: ANPMI is calculated by normalizing PMI using -logP(Choice).

**Interpretation**: A higher ANPMI score indicates a better understanding of the prompt by the model.

**Baseline Results**: N/A

**Validation**: The model performances were validated against known benchmarks and analyzed for variance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
