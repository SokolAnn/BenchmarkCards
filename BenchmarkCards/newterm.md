# NewTerm

## 📊 Benchmark Details

**Name**: NewTerm

**Overview**: NewTerm is an adaptive benchmark for real-time evaluation of new terms in large language models (LLMs), allowing for annual updates. It focuses on LLM performance related to new words, phrases, and meanings, and seeks to address the challenges faced by LLMs due to knowledge cutoffs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/hexuandeng/NewTerm)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to understand and integrate new terms into their language processing capabilities over time.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Collected new terms from online dictionaries such as Cambridge, Collins, and Oxford.

**Size**: 744 questions for NewTerm 2022, 715 questions for NewTerm 2023, covering 600 new terms.

**Format**: JSON

**Annotation**: Automatically generated with human filtering for quality assurance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured based on model performance in identifying correct answers to benchmark questions.

**Interpretation**: Higher accuracy indicates better understanding and integration of new terms by LLMs.

**Baseline Results**: N/A

**Validation**: Questions were filtered through a combination of automated methods and human verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International license (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
