# TEET! Tunisian Dataset for Toxic Speech Detection

## 📊 Benchmark Details

**Name**: TEET! Tunisian Dataset for Toxic Speech Detection

**Overview**: The paper introduces a new annotated dataset composed of approximately 10,000 comments for detecting toxic speech in the Tunisian dialect, addressing the urgent need for such datasets in underrepresented languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- T-HSAB

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the efficiency in detecting harmful and abusive content in the Tunisian dialect through a new annotated dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: Evaluation metrics related to inter-agreement have not been performed on the new annotated dataset.

## 💾 Data

**Source**: Collected from various social media platforms using queries containing abusive keywords.

**Size**: 10,000 comments

**Format**: N/A

**Annotation**: Annotated with a 3-way classification: Hate, Abusive, and Normal.

## 🔬 Methodology

**Methods**:
- Machine Learning
- Deep Learning

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics were calculated based on the predictions of various machine learning and deep learning models.

**Interpretation**: Higher F1 scores indicate better performance in classifying toxic speech.

**Baseline Results**: F1 Score of 92.3 for the best results in 3-way classification.

**Validation**: Data was split into 80% for training and 20% for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
