# AccessEval (Accessibility Evaluation)

## 📊 Benchmark Details

**Name**: AccessEval (Accessibility Evaluation)

**Overview**: AccessEval is a benchmark evaluating 21 closed- and open-source LLMs across 6 real-world domains and 9 disability types using paired Neutral and Disability-Aware Queries to systematically investigate disability bias in large language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Finance
- Healthcare
- Hospitality
- Media
- Technology

**Languages**:
- English

**Similar Benchmarks**:
- AUTALIC
- BITS

**Resources**:
- [Resource](https://huggingface.co/datasets/Srikant86/AccessEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate disability bias in large language models and promote more inclusive AI applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Bias Assessment
- Quality Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset of paired queries comprising Neutral Queries and Disability-Aware Queries.

**Size**: 2,340 queries

**Format**: CSV

**Annotation**: Manual validation combined with automated generation processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- VADER Score
- Regard Score
- LLM Judge

**Calculation**: Performance degradation is calculated by comparing scores of responses to Neutral Queries versus Disability-Aware Queries.

**Interpretation**: Lower scores on Disability-Aware Queries indicate potential bias in model responses.

**Baseline Results**: N/A

**Validation**: Statistical correlation with human annotations was performed to validate automated metric scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation leading to inadequate support for disabled users']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
