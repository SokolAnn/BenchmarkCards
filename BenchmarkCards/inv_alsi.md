# INV ALSI

## 📊 Benchmark Details

**Name**: INV ALSI

**Overview**: This paper introduces the INV ALSI benchmark, adapted for automated evaluation of language models, providing a structured evaluation framework using a set of well-established assessments designed to measure educational competencies across Italy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Italian

**Resources**:
- [Resource](https://huggingface.co/spaces/Crisp-Unimib/INV_ALSIbenchmark)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for assessing large language models using the INV ALSI framework.

**Target Audience**:
- ML Researchers
- Education Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from public sources including the Gestinv database which contains tests from the Italian national evaluations.

**Size**: 2114 questions and 2808 unique items across multiple tests

**Format**: JSON

**Annotation**: Manual inspection and adaptation of questions to improve alignment for LLM evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BERTScore

**Calculation**: Responses are assessed for correctness using pattern matching and regular expressions, alongside semantic comparisons via BERTScore.

**Interpretation**: Text comprehension accuracy reflects the model's understanding and generation proficiency, while scores indicate varying success across educational levels.

**Baseline Results**: N/A

**Validation**: Benchmarks are validated by comparing model performance against human benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
