# JEEB ENCH

## 📊 Benchmark Details

**Name**: JEEB ENCH

**Overview**: JEEB ENCH is a benchmark dataset for evaluating the problem solving abilities of large language models, consisting of 515 challenging pre-engineering mathematics, physics, and chemistry problems from the IIT JEE-Advanced exam.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM-8K
- ScienceQA

**Resources**:
- [GitHub Repository](https://github.com/dair-iitd/jeebench)

## 🎯 Purpose and Intended Users

**Goal**: To guide future research in problem-solving using large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Physics Problem Solving
- Chemistry Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Curated from the IIT JEE-Advanced exam papers from 2016 to 2023.

**Size**: 515 problems

**Format**: N/A

**Annotation**: Problems were manually curated and formatted.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: For different question types, scores are determined based on matching the model output to the expected correct answers.

**Interpretation**: An accuracy score reflects the ratio of correct answers produced by the model against the total number of problems.

**Validation**: Evaluation on various LLMs including GPT-4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
