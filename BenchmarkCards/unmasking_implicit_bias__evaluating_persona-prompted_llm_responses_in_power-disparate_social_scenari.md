# Unmasking Implicit Bias: Evaluating Persona-Prompted LLM Responses in Power-Disparate Social Scenarios

## 📊 Benchmark Details

**Name**: Unmasking Implicit Bias: Evaluating Persona-Prompted LLM Responses in Power-Disparate Social Scenarios

**Overview**: This study introduces a novel evaluation framework using cosine distance and an LLM-judged Preference Win Rate to measure how demographic prompts affect response quality across power-disparate social scenarios, revealing biases in large language models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SOTOPIA

**Resources**:
- [Resource](https://arxiv.org/abs/2503.01532)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively assess how demographic information influences LLM-generated responses across diverse social contexts and power dynamics.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- AI Practitioners

**Tasks**:
- Bias Assessment
- Response Evaluation

**Limitations**: Responses and findings may not generalize to all contexts or demographics, as the study focused on specific social scenarios.

## 💾 Data

**Source**: Generated social scenarios using LLMs with demographic prompts and responses evaluated for biases and quality.

**Size**: 100 unique scenarios

**Format**: N/A

**Annotation**: Responses were evaluated based on qualitative criteria including Helpfulness, Honesty, and Harmlessness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Preference Win Rate (WR)
- Cosine Distance

**Calculation**: Cosine distance measures identity shifts in responses induced by demographic prompts; Win Rate compares responses based on evaluated criteria.

**Interpretation**: A lower average cosine distance indicates a model's sensitivity to demographic changes; a higher Win Rate reflects better quality responses under demographic prompts.

**Validation**: Comparison of LLM judgments with human evaluations showed moderate alignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Misuse**: Nonconsensual use

**Demographic Analysis**: The study investigates implicit biases related to demographic information across various axes including race, gender, age, and disability.

**Potential Harm**: ['Discriminatory outcomes in sensitive applications due to embedded biases.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
