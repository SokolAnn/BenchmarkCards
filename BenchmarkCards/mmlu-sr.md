# MMLU-SR

## 📊 Benchmark Details

**Name**: MMLU-SR

**Overview**: MMLU-SR is a novel dataset designed to measure the true comprehension abilities of Large Language Models by challenging their performance in question-answering tasks with modified terms, emphasizing reasoning over mere memorization.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- AGIEval
- BoolQ
- GSM8K
- DROP

**Resources**:
- [Resource](https://arxiv.org/abs/2406.15468)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the reasoning and understanding capabilities of LLMs by testing their performance with modified questions and answers.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Modified questions and answers from the MMLU dataset, with key terms replaced by dummy words and their definitions.

**Size**: N/A

**Format**: JSON

**Annotation**: Terms extracted and definitions generated with some manual modifications for accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation of model performance based on accuracy in relation to original MMLU benchmarks.

**Interpretation**: Higher accuracy indicates better reasoning and comprehension capabilities of the models.

**Validation**: Models validated through comparative analysis with original MMLU dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
