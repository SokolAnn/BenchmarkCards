# SpeciesismBench

## 📊 Benchmark Details

**Name**: SpeciesismBench

**Overview**: SpeciesismBench is a 1,003-item benchmark assessing recognition and moral evaluation of speciesist statements by large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ETHICS benchmark
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [Resource](https://osf.io/69epv)

## 🎯 Purpose and Intended Users

**Goal**: To investigate speciesist bias in large language models and assess their ethical reasoning regarding species membership.

**Target Audience**:
- AI Researchers
- Ethicists
- Model Developers

**Tasks**:
- Moral Evaluation
- Text Classification

**Limitations**: The benchmark targets Western speciesist norms, limiting the generalizability of the results across cultures and languages.

## 💾 Data

**Source**: Model-generated speciesist statements created through prompts from Claude 3.5 Sonnet.

**Size**: 1,003 statements

**Format**: N/A

**Annotation**: Manual review and double checks by researchers to ensure accuracy and consistency.

## 🔬 Methodology

**Methods**:
- Speciesism classification
- Moral evaluation

**Metrics**:
- Accuracy

**Calculation**: Model performance is assessed based on response classification and moral evaluations.

**Interpretation**: High accuracy indicates the model's ability to recognize speciesist content, while low moral judgment scores suggest acceptance of such content.

**Validation**: Evaluations conducted across multiple AI model families including multiple runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Potential Harm**: ['Normalization of speciesist attitudes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
