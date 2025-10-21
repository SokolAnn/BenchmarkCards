# Chinese Named Entity Recognition in Financial News

## 📊 Benchmark Details

**Name**: Chinese Named Entity Recognition in Financial News

**Overview**: This paper presents a strategy for improving named entity recognition (NER) in the financial domain, particularly focusing on company names found in Chinese financial news. It introduces a multi-stage learning strategy and knowledge distillation techniques to enhance the performance of lightweight models on sparse datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Hanlard/Electra-CRF-NER)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of named entity recognition in financial news with minimal annotation costs by leveraging machine-annotated data and pre-training methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Built from financial news corpus and annotated datasets.

**Size**: 1.62 million financial news, 350,000 machine-annotated sentences, 65,000 manually annotated sentences, 200 financial news for testing

**Format**: N/A

**Annotation**: Combination of machine annotation and manual verification.

## 🔬 Methodology

**Methods**:
- Multi-stage learning strategy
- Knowledge distillation

**Metrics**:
- Recall
- Precision

**Calculation**: Metrics are calculated based on the predictions made on the test dataset compared to manually annotated references.

**Interpretation**: Higher recall and precision indicate better performance in identifying relevant named entities in financial news.

**Baseline Results**: Comparison is made against BERT-CRF model for speed and accuracy improvements.

**Validation**: The model's effectiveness was validated by cross-validation on a manually annotated test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
