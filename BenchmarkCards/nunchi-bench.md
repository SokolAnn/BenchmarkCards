# Nunchi-Bench

## 📊 Benchmark Details

**Name**: Nunchi-Bench

**Overview**: Nunchi-Bench is a benchmark designed to evaluate LLMs’ cultural understanding, focusing on Korean superstitions through 247 questions across 31 topics that assess factual knowledge, culturally appropriate advice, and situational interpretation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean
- English

**Similar Benchmarks**:
- CLIcK
- KorNAT

**Resources**:
- [GitHub Repository](https://github.com/koreankiwi99/Nunchi-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cultural sensitivity and reasoning capabilities of large language models with a focus on Korean cultural contexts.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Cultural Reasoning
- Question Answering

**Limitations**: The dataset focuses specifically on Korean superstitions, which may limit broader applicability.

## 💾 Data

**Source**: Selected cultural superstitions gathered from books and news articles related to Korean culture.

**Size**: 247 questions

**Format**: JSON

**Annotation**: Questions assessed for relevance and accuracy by Korean experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores are calculated based on the model’s alignment with culturally appropriate responses and factual accuracy.

**Interpretation**: Scores reflect both the factual correctness of answers and the cultural appropriateness of responses.

**Validation**: Multi-phase alignment study comparing LLM outputs to human ratings shows alignment improved to 90% for cultural sensitivity evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of responses reveals performance variances based on cultural background specification in questions.

**Potential Harm**: Risk of reinforcing stereotypes or cultural misunderstandings if models fail to interpret nuances correctly.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
