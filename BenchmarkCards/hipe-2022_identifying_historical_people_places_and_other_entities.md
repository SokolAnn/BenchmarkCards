# HIPE-2022 (Identifying Historical People, Places and other Entities)

## 📊 Benchmark Details

**Name**: HIPE-2022 (Identifying Historical People, Places and other Entities)

**Overview**: This study explores the feasibility of applying large language models (LLMs) to Named Entity Recognition (NER) in historical documents using zero-shot and few-shot prompting strategies.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Digital Humanities

**Languages**:
- German
- French
- English
- Swedish
- Finnish

**Resources**:
- [GitHub Repository](https://github.com/hipe-eval/HIPE-scorer)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of LLMs for performing NER on historical texts in various languages and to analyze their performance.

**Target Audience**:
- ML Researchers
- Digital Humanists
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: A collection of datasets for NER in historical documents, manually annotated with entity information.

**Size**: N/A

**Format**: N/A

**Annotation**: Manually annotated by experts

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Few-shot prompting

**Metrics**:
- Micro Fuzzy F1 Score
- Micro Strict F1 Score

**Calculation**: Mean and confidence intervals of evaluation metrics under both strict and fuzzy evaluation.

**Interpretation**: Higher F1 scores indicate better performance in identifying and classifying named entities.

**Validation**: Experiments were repeated three times to account for variability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
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
