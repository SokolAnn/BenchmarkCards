# DoCo (Document Coverage)

## 📊 Benchmark Details

**Name**: DoCo (Document Coverage)

**Overview**: This paper presents a new task of predicting the coverage of a text document for relation extraction (RE), along with a dataset of 31,366 diverse documents for 520 entities. The dataset includes annotations for document coverage and is designed to support experimental comparisons for relation extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://www.mpi-inf.mpg.de/document-coverage-prediction)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a systematic approach for analyzing and predicting document coverage for relation extraction.

**Target Audience**:
- ML Researchers
- Knowledge Engineers

**Tasks**:
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Collection of 31,366 web documents for 520 distinct entities, utilizing search engine queries and web scraping methods.

**Size**: 31,366 documents

**Format**: N/A

**Annotation**: Automated extractions and coverage labels generated via relation extraction APIs.

## 🔬 Methodology

**Methods**:
- Classification using features and pre-trained language models
- Logistic Regression
- HERB (Heuristics with BERT)

**Metrics**:
- F1 Score

**Calculation**: F1 scores calculated based on the model predictions for document coverage.

**Interpretation**: A higher F1 score indicates better model performance in predicting document coverage.

**Baseline Results**: F1 score of up to 46% for the HERB model.

**Validation**: Evaluated against state-of-the-art baselines and with different ground truth variants.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
