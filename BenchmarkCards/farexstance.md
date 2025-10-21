# FarExStance

## 📊 Benchmark Details

**Name**: FarExStance

**Overview**: FAREXSTANCE is the first dataset for explainable stance detection in Farsi, consisting of claims, stance labels, and extractive explanations as evidence for the stance labels.

**Data Type**: stance detection pairs with extractive explanations

**Domains**:
- Natural Language Processing

**Languages**:
- Farsi

**Similar Benchmarks**:
- Persian Stance Classification
- ParsFEVER
- Persian Tweets Stance Detection

**Resources**:
- [GitHub Repository](https://github.com/Zarharan/FarExStance)
- [GitHub Repository](https://github.com/Dadmatech/FarExStance)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for stance detection and explainable NLP in the Farsi language, contributing to efforts in misinformation detection and automated claim verification.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Domain Experts

**Tasks**:
- Stance Detection
- Evidence Retrieval

**Limitations**: Dataset includes claims in Farsi, which may limit applicability to other languages.

## 💾 Data

**Source**: Claims generated from headlines and news summaries collected from over 100 Farsi news agency websites.

**Size**: 26,307 instances

**Format**: CSV

**Annotation**: Manual annotation by native Farsi speakers.

## 🔬 Methodology

**Methods**:
- Evaluation of stance classification performance using various multilingual language models.
- Human evaluation of generated explanations.

**Metrics**:
- Accuracy
- Macro Precision
- Macro Recall
- Macro F1 Score

**Calculation**: Metrics calculated using standard classification evaluation techniques across training, validation, and test splits.

**Interpretation**: Higher scores indicate better model performance on stance detection and explanation generation.

**Baseline Results**: The highest stance detection accuracy achieved by various models ranged from 44.6% to 79.8%, with human performance estimated at 79.2%.

**Validation**: Cross-validation performed with annotated instances to achieve agreement rates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Dataset includes a diverse range of perspectives from Farsi news sources and social media.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User content anonymized; only post identifiers were used in the dataset.

**Data Licensing**: Licensed under N/A; dataset is publicly available for academic purposes.

**Consent Procedures**: Data collected follows ethical guidelines involving user privacy and data protection.

**Compliance With Regulations**: Research adheres to ethical standards but specific compliance details regarding regulations like GDPR and CCPA were not discussed.
