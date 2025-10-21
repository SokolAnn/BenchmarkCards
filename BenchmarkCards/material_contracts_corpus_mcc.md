# Material Contracts Corpus (MCC)

## 📊 Benchmark Details

**Name**: Material Contracts Corpus (MCC)

**Overview**: The Material Contracts Corpus (MCC) is a publicly available dataset comprising over one million contracts filed by public companies with the U.S. Securities and Exchange Commission (SEC) between 2000 and 2023. The MCC facilitates empirical research on contract design and legal language, and supports the development of AI-based legal tools.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Resources**:
- [Resource](https://mcc.law.stanford.edu)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and publicly available dataset of over one million unique contracts filed with the SEC for empirical studies and the development of AI-based legal tools.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Academics

**Tasks**:
- Contract Analysis
- Legal Document Classification

**Limitations**: N/A

## 💾 Data

**Source**: U.S. Securities and Exchange Commission (SEC) EDGAR Database.

**Size**: 1,038,766 unique contracts

**Format**: HTM, TXT

**Annotation**: Contracts were hand-labeled based on agreement types and classified using a fine-tuned LLaMA-2 model.

## 🔬 Methodology

**Methods**:
- Machine Learning
- Natural Language Processing

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated using five-fold cross-validation.

**Interpretation**: An accuracy of 95% and a weighted F1 score of 0.95 indicates strong classification performance.

**Validation**: Five-fold cross-validation was used to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
