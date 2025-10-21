# Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language towards Vulnerable Communities

## 📊 Benchmark Details

**Name**: Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language towards Vulnerable Communities

**Overview**: This paper introduces the Don’t Patronize Me! dataset aimed at supporting the development of NLP models to identify and categorize language that is patronizing or condescending towards vulnerable communities like refugees, homeless people, and poor families.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Talkdown

**Resources**:
- [GitHub Repository](https://github.com/Perez-AlmendrosC/dontpatronizeme)

## 🎯 Purpose and Intended Users

**Goal**: To encourage more research on detecting patronizing and condescending language (PCL) towards vulnerable communities.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Social Scientists

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Paragraphs extracted from news stories in the News on Web (NoW) corpus.

**Size**: 10,637 paragraphs

**Format**: N/A

**Annotation**: Annotated by three expert annotators, using a two-step annotation process.

## 🔬 Methodology

**Methods**:
- SVM
- BiLSTM
- BERT
- RoBERTa
- DistilBERT

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using standard evaluation methods for binary and multi-label classification tasks.

**Interpretation**: Higher scores indicate better detection and categorization of PCL.

**Baseline Results**: BERT-based approaches outperformed simpler methods, achieving significant improvements over random guessing.

**Validation**: 10-fold cross-validation used to validate methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International Licence

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
