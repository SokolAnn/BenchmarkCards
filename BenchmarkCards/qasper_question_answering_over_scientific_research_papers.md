# QASPER (Question Answering over Scientific Research Papers)

## 📊 Benchmark Details

**Name**: QASPER (Question Answering over Scientific Research Papers)

**Overview**: QASPER is an information-seeking QA dataset over academic research papers, containing 5,049 questions over 1,585 NLP papers. Each question is written by practitioners after reading only the title and abstract, and seeks information found in the full text, requiring complex reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://allenai.org/project/qasper)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging dataset that evaluates question answering systems on document-grounded tasks with real-world information-seeking questions.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Practitioners

**Tasks**:
- Question Answering
- Evidence Selection

**Limitations**: N/A

## 💾 Data

**Source**: S2ORC dataset containing open-access NLP research papers.

**Size**: 5,049 questions

**Format**: JSON

**Annotation**: Questions are written and answered by NLP practitioners.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Answer-F1
- Evidence-F1

**Calculation**: Metrics are calculated based on the correctness of the predicted answers and the selected evidence paragraphs.

**Interpretation**: Higher metrics indicate better performance in answering questions and selecting appropriate evidence.

**Baseline Results**: LED-base model achieved an overall Answer-F1 score of 44.96 on the test set.

**Validation**: Split the dataset into train, validation, and test sets, with paper overlap ensured.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading information retrieval from papers']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All papers used are under the CC-BY-* license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
