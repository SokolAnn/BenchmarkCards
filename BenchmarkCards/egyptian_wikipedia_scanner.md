# Egyptian Wikipedia Scanner

## 📊 Benchmark Details

**Name**: Egyptian Wikipedia Scanner

**Overview**: The Egyptian Wikipedia Scanner is an online application developed to identify template-translated articles in the Egyptian Arabic Wikipedia using metadata and machine learning classifiers.

**Data Type**: filtered and labeled datasets

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/SaiedAlshahrani/Egyptian-Wikipedia-Scanner)
- [Resource](https://egyptian-wikipedia-scanner.streamlit.app)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate the problem of low-quality content produced by template-based translations in the Egyptian Arabic Wikipedia by providing a detection system for researchers and practitioners.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Wikipedia Contributors

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Articles from the Egyptian Arabic Wikipedia, filtered for quality and metadata-based classification.

**Size**: 736,107 articles

**Format**: N/A

**Annotation**: Data labeled manually based on the analysis of articles' metadata.

## 🔬 Methodology

**Methods**:
- Multivariate Classification
- Machine Learning

**Metrics**:
- Accuracy
- ROC-AUC

**Calculation**: Metrics calculated using stratified K-Folds cross-validation on training and testing splits.

**Interpretation**: High accuracy rates indicate effective identification of template-translated articles.

**Baseline Results**: Classifiers achieve performance accuracy ranging from 90% to 100%.

**Validation**: Performance evaluated through cross-validation techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The model might misrepresent Egyptian culture by relying heavily on template-translated content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
