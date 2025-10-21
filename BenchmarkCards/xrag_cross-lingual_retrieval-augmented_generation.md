# XRAG (Cross-lingual Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: XRAG (Cross-lingual Retrieval-Augmented Generation)

**Overview**: XRAG is designed to evaluate the generation abilities of LLMs in cross-lingual Retrieval-Augmented Generation settings where the user language does not match the retrieval results, focusing on complex reasoning and the integration of multilingual information.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Chinese
- German
- Spanish
- English

**Similar Benchmarks**:
- XQA
- XOR QA

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating LLMs' performance in cross-lingual RAG scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: News articles from News Crawl between June 1, 2024 and November 30, 2024

**Size**: 2,950 Q&A pairs verified

**Format**: N/A

**Annotation**: Manual annotation by a professional multilingual annotation team

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM judge panel evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the majority vote from an LLM judge panel.

**Interpretation**: Higher accuracy reflects better performance of LLMs in cross-lingual reasoning and retrieval settings.

**Baseline Results**: GPT-4o achieved 62.4% accuracy in the XRAG evaluation.

**Validation**: The benchmark is validated by comparing LLM responses to human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
