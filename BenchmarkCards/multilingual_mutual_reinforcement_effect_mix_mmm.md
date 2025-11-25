# Multilingual Mutual Reinforcement Effect Mix (MMM)

## 📊 Benchmark Details

**Name**: Multilingual Mutual Reinforcement Effect Mix (MMM)

**Overview**: The Multilingual MRE mix dataset (MMM) encompasses 21 sub-datasets in English, Japanese, and Chinese to facilitate information extraction research.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Japanese
- Chinese

**Resources**:
- [Resource](https://huggingface.co/datasets/Universal-NER/Pile-NER-type?row=0)

## 🎯 Purpose and Intended Users

**Goal**: To address the limitations of existing MRE datasets by introducing a multilingual dataset for comprehensive exploration in information extraction tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Text Classification
- Relation Extraction
- Event Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Translation of existing MRE datasets from Japanese to English and Chinese, along with the construction of new datasets like TCONER.

**Size**: 180,000 examples

**Format**: N/A

**Annotation**: Manual verification and annotation after LLM-assisted dataset construction.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated based on precision and recall of label-entity pairs.

**Interpretation**: Higher F1 Score indicates better performance in information extraction tasks.

**Validation**: The dataset evaluation involved splitting data into training and test sets with various sample sizes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
