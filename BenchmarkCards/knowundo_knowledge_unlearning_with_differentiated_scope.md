# KnowUnDo (Knowledge Unlearning with Differentiated Scope)

## 📊 Benchmark Details

**Name**: KnowUnDo (Knowledge Unlearning with Differentiated Scope)

**Overview**: KnowUnDo is a benchmark for evaluating knowledge unlearning methods in Large Language Models (LLMs), focusing on sensitive information like copyrighted content and user privacy. It categorizes knowledge instances into 'Unlearn Scope' and 'Retention Scope' to assess the precision of unlearning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TOFU
- RWKU

**Resources**:
- [GitHub Repository](https://github.com/zjunlp/KnowUnDo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for knowledge unlearning methods, aiming to enhance privacy and copyright compliance in LLMs.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Knowledge Unlearning Evaluation

**Limitations**: The current scope does not include all types of copyrighted content and user privacy scenarios.

## 💾 Data

**Source**: Constructed from publicly available copyright materials and fictitious privacy data.

**Size**: 2,649 examples

**Format**: JSON

**Annotation**: Manually verified and generated using GPT models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Unlearn Success
- Retention Success
- Perplexity
- ROUGE-L

**Calculation**: Metrics are calculated based on the model's accuracy in predicting within the defined Unlearn and Retention scopes.

**Interpretation**: Higher Unlearn Success indicates effective forgetting of sensitive knowledge, while higher Retention Success signifies maintained performance in permissible knowledge.

**Validation**: Benchmarked against existing unlearning methods to assess performance improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Inadequate protection of user privacy', 'Excessive unlearning leading to loss of general knowledge']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User privacy is protected by employing fictitious data and ensuring sensitive information is categorized correctly.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to GDPR and CCPA guidelines for data protection.
