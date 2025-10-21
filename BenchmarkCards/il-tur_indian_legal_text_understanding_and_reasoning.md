# IL-TUR (Indian Legal Text Understanding and Reasoning)

## 📊 Benchmark Details

**Name**: IL-TUR (Indian Legal Text Understanding and Reasoning)

**Overview**: IL-TUR is a benchmark for Indian Legal Text Understanding and Reasoning, containing monolingual (English, Hindi) and multilingual (9 Indian languages) domain-specific tasks focused on understanding and reasoning over Indian legal documents.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Similar Benchmarks**:
- LexGLUE
- LEXTREME
- LEGALBENCH

**Resources**:
- [Resource](https://exploration-lab.github.io/IL-TUR/)

## 🎯 Purpose and Intended Users

**Goal**: To foster research in the Legal-NLP domain and provide a comprehensive benchmark for evaluating NLP models on legal tasks.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Model Developers

**Tasks**:
- Legal Named Entity Recognition
- Rhetorical Role Prediction
- Court Judgment Prediction with Explanation
- Bail Prediction
- Legal Statute Identification
- Prior Case Retrieval
- Summarization
- Legal Machine Translation

**Limitations**: IL-TUR is the first step towards creating a comprehensive benchmark for the Indian legal domain and does not cover all legal subdomains.

## 💾 Data

**Source**: Legal documents scrapped from IndianKanoon and other open legal datasets.

**Size**: 105 documents for L-NER, 21,184 sentences for RR, 34,000 legal judgment documents for CJPE, 176,000 documents for BAIL, 65,000 case documents for LSI, 7,070 documents for PCR, 7,130 summaries for SUMM, 17,853 document pairs for L-MT.

**Format**: JSON

**Annotation**: Annotated by legal experts and students following defined legal terminologies and criteria.

## 🔬 Methodology

**Methods**:
- BERT-based models
- Multi-Task Learning methods
- Hierarchical models

**Metrics**:
- Macro F1 Score
- ROUGE-L
- BLEU Score

**Calculation**: Metrics such as macro-averaged precision, recall, and F1 scores are calculated for task evaluations.

**Interpretation**: Higher scores indicate better model performance in legal document understanding and task execution.

**Validation**: Cross-validation across multiple tasks with publicly available datasets and continuous updates planned for future tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Legal Compliance
- Explainability

**Atlas Risks**:
- **Fairness**: Data bias
- **Legal Compliance**: Model usage rights restrictions
- **Explainability**: Unexplainable output

**Demographic Analysis**: Future versions of IL-TUR will aim to include demographic analysis to ensure fair representation in legal NLP.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Named entities in datasets have been anonymized to mitigate potential biases.

**Data Licensing**: Released under Creative Common Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
