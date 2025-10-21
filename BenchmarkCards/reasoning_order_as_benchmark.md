# Reasoning Order as Benchmark

## 📊 Benchmark Details

**Name**: Reasoning Order as Benchmark

**Overview**: This benchmark method assesses the consistency of large language model reasoning processes by comparing outputs generated through answer-first and logic-first prompts.

**Data Type**: multiple choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- TruthfulQA
- LogiQA
- BIG-Bench

**Resources**:
- [Resource](https://arxiv.org/abs/2408.05093)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate the consistency of reasoning in large language models by utilizing different prompting strategies.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reasoning Assessment
- Question Answering

**Limitations**: Due to budget constraints, experiments were limited to smaller datasets and fewer LLMs.

## 💾 Data

**Source**: Datasets used include MMLU, TruthfulQA, LogiQA, and BigBench.

**Size**: 1,531 multiple choice questions (MMLU); 817 questions (TruthfulQA); 1,000 questions (LogiQA); 447 questions (BigBench)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Comparison of answer-first and logic-first prompts
- Reflexive prompting strategy

**Metrics**:
- Accuracy
- Pearson Correlation Coefficient

**Calculation**: Accuracies are calculated based on model outputs for multiple choice questions; correlations are evaluated between consistency and accuracy across models.

**Interpretation**: Higher consistency and accuracy indicate better reliability of language model outputs.

**Baseline Results**: Baseline comparisons presented across various prompts resulted in nuanced performance differentials.

**Validation**: Experimental validation through multiple reasoning datasets and comparison across prompt types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
