# PRIMATE

## 📊 Benchmark Details

**Name**: PRIMATE

**Overview**: This study introduces refinements to the PRIMATE dataset annotations for detecting anhedonia in social media posts, specifically by addressing the validity of annotations and providing more nuanced labeling by a mental health professional.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/501Good/primate-anhedonia)

## 🎯 Purpose and Intended Users

**Goal**: To improve the quality of annotations in the PRIMATE dataset for better depression estimation, focusing on the symptom of anhedonia.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Text Classification

**Limitations**: The reannotation was performed by only one mental health professional, which limits inter-annotator agreement analysis.

## 💾 Data

**Source**: PRIMATE dataset based on Reddit posts from the r/depression_help subreddit

**Size**: 2003 posts

**Format**: N/A

**Annotation**: Reannotated by a mental health professional with additional evidence-based labeling.

## 🔬 Methodology

**Methods**:
- Baseline testing with pre-trained language models such as DistilBERT, BERT-Base, RoBERTa-Base, RoBERTa-Large, DeBERTa-Base, and DeBERTa-Large.

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Metrics calculated based on predictions against the refined annotations.

**Interpretation**: Interpretation of results focuses on model predictions' accuracy in detecting anhedonia symptoms.

**Baseline Results**: DistilBERT shows competitive performance compared to larger models.

**Validation**: Random sampling of posts for validation and testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Concerns regarding false positives in symptom detection due to annotation validity issues.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used from public social media posts, no identifiable user information.

**Data Licensing**: Annotations released under a Data Use Agreement.

**Consent Procedures**: Data collected in accordance with user-generated content guidelines.

**Compliance With Regulations**: Not Applicable
