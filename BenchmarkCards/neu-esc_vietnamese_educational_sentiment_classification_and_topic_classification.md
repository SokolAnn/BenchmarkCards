# NEU-ESC (Vietnamese Educational Sentiment Classification and Topic Classification)

## 📊 Benchmark Details

**Name**: NEU-ESC (Vietnamese Educational Sentiment Classification and Topic Classification)

**Overview**: NEU-ESC is a new Vietnamese dataset for Educational Sentiment Classification and Topic Classification, curated from university forums that offers more samples, richer class diversity, longer texts, and broader vocabulary.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Similar Benchmarks**:
- UIT-VSFC
- ViHSD
- ViCTSD

**Resources**:
- [Resource](https://huggingface.co/datasets/hung20gg/NEU-ESC)

## 🎯 Purpose and Intended Users

**Goal**: To create a new dataset from NEU students on social media platforms and demonstrate its utility for sentiment analysis and topic classification tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Educators
- Data Scientists

**Tasks**:
- Sentiment Analysis
- Topic Classification

**Limitations**: The dataset is currently imbalanced, with a predominant focus on 'Other' and 'Academic' topics, which may limit generalization.

## 💾 Data

**Source**: Collected from university-related Facebook groups and community forums in Vietnam.

**Size**: 33,000 samples

**Format**: N/A

**Annotation**: Manually curated with preprocessing to clean text and identify meaningful content.

## 🔬 Methodology

**Methods**:
- Single-task learning
- Multitask learning
- Fine-tuning
- Evaluation against Large Language Models

**Metrics**:
- Accuracy
- Mean F1 Score
- Weighted F1 Score

**Calculation**: Metrics calculated based on model predictions against ground truth labels in validation and test datasets.

**Interpretation**: Higher metrics indicate better performance in classifying sentiment and topics accurately.

**Baseline Results**: Previous datasets UIT-VSFC, ViHSD, and ViCTSD.

**Validation**: Data was split into training, validation, and test sets with specific ratios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Demographic factors related to the student population engaging in discussions were noted but not deeply analyzed.

**Potential Harm**: ['Misclassification of sentiment and topic categories may lead to misunderstandings in educational contexts.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available social media comments; no explicit privacy measures were discussed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
