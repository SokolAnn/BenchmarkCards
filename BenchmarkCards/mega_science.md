# MEGA SCIENCE

## 📊 Benchmark Details

**Name**: MEGA SCIENCE

**Overview**: MEGA SCIENCE is a large-scale mixture of high-quality open-source datasets consisting of 1.25 million instances, developed through systematic ablation studies to identify optimal subsets for scientific reasoning tasks across various benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- Nemotron-Science
- NaturalReasoning

**Resources**:
- [GitHub Repository](https://github.com/GAIR-NLP/lm-open-science-evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To advance open-source post-training datasets for scientific reasoning and improve the performance of language models in scientific tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Scientific Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from 12k university-level scientific textbooks and other public datasets.

**Size**: 1.25 million instances

**Format**: CSV

**Annotation**: Manual annotation and LLM-based decontamination.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the performance of models fine-tuned on datasets from MEGA SCIENCE.

**Interpretation**: Higher accuracy indicates better performance on scientific reasoning tasks.

**Baseline Results**: Compared against models fine-tuned with other datasets.

**Validation**: Evaluation was conducted across 15 benchmarks for reproducibility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
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
