# REFCHECKER

## 📊 Benchmark Details

**Name**: REFCHECKER

**Overview**: REFCHECKER is a framework that introduces claim-triplets to represent claims in LLM responses, aiming to detect fine-grained hallucinations.

**Data Type**: Annotated claim-triplets

**Domains**:
- Natural Language Processing
- Information Extraction
- Closed Question Answering
- Summarization

**Languages**:
- English

**Similar Benchmarks**:
- SelfCheckGPT
- FActScore
- FacTool

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/RefChecker)

## 🎯 Purpose and Intended Users

**Goal**: To provide an automated framework for detecting hallucinations in outputs generated by large language models.

**Target Audience**:
- NLP researchers
- AI developers
- Data scientists

**Tasks**:
- Hallucination detection
- Evaluation of LLM outputs
- Benchmarking LLM performance

**Limitations**: N/A

**Out of Scope Uses**:
- Real-time hallucination detection in production systems
- Non-text data handling

## 💾 Data

**Source**: Natural Questions, MS MARCO, databricks-dolly-15k

**Size**: 11,000 claim-triplets from 2,100 responses

**Format**: Annotated claim-triplets

**Annotation**: 95% Inter-Annotator Agreement

## 🔬 Methodology

**Methods**:
- Extractor for claim-triplets
- Checker for evaluating claims against references

**Metrics**:
- Accuracy
- Macro F1
- Human alignment scores

**Calculation**: Calculated based on the ratio of claims per response classified as Entailment, Neutral, or Contradiction.

**Interpretation**: Higher scores indicate better hallucination detection performance.

**Validation**: Conducted using human evaluation against responses from seven different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Factual hallucinations
- Non-factual claims

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Possibility of misleading users with hallucinated content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured through use of publicly accessible datasets and compliance with licensing.

**Data Licensing**: Data from NQ, MS MARCO, and databricks-dolly-15k are used which are under Creative Commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
