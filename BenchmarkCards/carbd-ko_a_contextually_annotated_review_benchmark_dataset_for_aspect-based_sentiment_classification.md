# CARBD-Ko (A Contextually Annotated Review Benchmark Dataset for Aspect-Based Sentiment Classification in Korean)

## 📊 Benchmark Details

**Name**: CARBD-Ko (A Contextually Annotated Review Benchmark Dataset for Aspect-Based Sentiment Classification in Korean)

**Overview**: CARBD-Ko is a benchmark dataset designed for aspect-based sentiment classification in Korean, incorporating aspects and dual-tagged polarities to improve sentiment classification accuracy.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Resources**:
- [GitHub Repository](https://github.com/e9t/nsmc)

## 🎯 Purpose and Intended Users

**Goal**: To improve aspect-based sentiment classification (ABSC) models by providing a dataset with dual-tagged aspect polarities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Aspect-based Sentiment Classification

**Limitations**: N/A

## 💾 Data

**Source**: Comments collected from users across various domains, including movies and shopping.

**Size**: 10,586 instances for training, nearly 3,000 for validation

**Format**: N/A

**Annotation**: Manual annotation by a team of annotators assigning aspect-agnostic polarity, aspect polarity, and intensity of aspect polarity.

## 🔬 Methodology

**Methods**:
- Siamese Network

**Metrics**:
- Accuracy

**Calculation**: The accuracy for predicting aspect polarity and aspect-agnostic polarity is calculated using performance evaluation metrics relevant to sentiment analysis.

**Interpretation**: Performance is measured by predicting the sentiment of aspects and their contextual relevance.

**Baseline Results**: N/A

**Validation**: The model's performance was evaluated against pre-existing sentiment classification benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data obtained from publicly available sources with personally identifiable information removed.

**Data Licensing**: Available for research purposes only, adhering to ethical guidelines.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
