# Explainable Argumentation Computation Benchmark

## 📊 Benchmark Details

**Name**: Explainable Argumentation Computation Benchmark

**Overview**: This benchmark comprises diverse abstract argumentation frameworks, enabling the training of explainable large language models (LLMs) to compute extensions using labeling algorithms, focusing on grounded and complete extension-solving tasks with accompanying explanations.

**Data Type**: graph representations with explanations

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AGNN (Argumentation Graph Neural Networks)
- EGNN (Explainable Graph Neural Networks)

**Resources**:
- [Resource](https://arxiv.org/abs/2412.16725)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the computation of extensions in argumentation frameworks using large language models while improving explainability.

**Target Audience**:
- Researchers in Artificial Intelligence
- Natural Language Processing Domain Experts
- Model Developers in Machine Learning

**Tasks**:
- Grounded Extension Computation
- Complete Extension Computation

**Limitations**: N/A

## 💾 Data

**Source**: Generated diverse abstract argumentation frameworks with explanations.

**Size**: 60,000 training samples, 2,000 test samples

**Format**: JSON, GraphML, DOT

**Annotation**: Instruction-tuning data template including instruction, problem, explanation, and answer.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Matthews Correlation Coefficient (MCC)

**Calculation**: Metrics are calculated through direct comparison of predicted outputs against ground truths.

**Interpretation**: Higher accuracy indicates better performance of the LLMs in computing argumentation semantics.

**Baseline Results**: LLMs trained with explanations exhibit significant improvements over zero-shot prompting.

**Validation**: Performance validated by comparing LLMs before and after fine-tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Explainability

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Explainability**: Unexplainable output

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
