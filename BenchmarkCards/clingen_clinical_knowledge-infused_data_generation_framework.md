# CLINGEN (Clinical Knowledge-Infused Data Generation Framework)

## 📊 Benchmark Details

**Name**: CLINGEN (Clinical Knowledge-Infused Data Generation Framework)

**Overview**: CLINGEN is a clinical knowledge-infused framework for synthetic clinical text data generation utilizing knowledge extraction from clinical knowledge graphs and large language models (LLMs). It enhances the alignment of synthetic data with real data distributions and improves task performance across various clinical NLP applications.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ritaranx/ClinGen)

## 🎯 Purpose and Intended Users

**Goal**: To generate high-quality synthetic clinical text data for training machine learning models in healthcare and clinical NLP tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering
- Natural Language Inference
- Relation Extraction
- Fact Verification
- Sentence Similarity
- Attribute Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using LLMs guided by clinical knowledge graphs.

**Size**: 5000 examples

**Format**: N/A

**Annotation**: Automatically generated; utilizes knowledge extraction techniques.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Scores calculated using standard evaluation metrics on benchmark datasets.

**Interpretation**: Higher scores indicate better performance in generalizing onto real-world clinical data.

**Baseline Results**: Base results against multiple existing data generation methods.

**Validation**: Performance validated through exhaustive empirical studies across multiple tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured by selecting few-shot examples without Protected Health Information (PHI).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with data protection regulations.
