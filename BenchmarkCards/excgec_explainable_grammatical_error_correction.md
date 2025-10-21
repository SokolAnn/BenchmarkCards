# EXCGEC (Explainable Grammatical Error Correction)

## 📊 Benchmark Details

**Name**: EXCGEC (Explainable Grammatical Error Correction)

**Overview**: This paper introduces the task of EXplainable GEC (EXGEC), focusing on the correction and explanation of grammatical errors in Chinese texts. It establishes the EXCGEC benchmark consisting of 8,216 explanation-augmented samples designed for this task.

**Data Type**: explanation-augmented samples

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/THUKElab/EXCGEC)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for explainable grammatical error correction in Chinese and evaluate various large language models.

**Target Audience**:
- ML Researchers
- Education Practitioners
- Model Developers

**Tasks**:
- Grammatical Error Correction
- Explainable AI

**Limitations**: N/A

## 💾 Data

**Source**: Annotated and generated from existing datasets, utilizing synthetic data generation for efficiency.

**Size**: 8,216 samples

**Format**: JSON

**Annotation**: Manual filtering and verification by experienced annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- METEOR
- ROUGE

**Calculation**: Metrics calculated based on predictions compared to ground truth explanations.

**Interpretation**: Higher scores indicate better performance in correcting grammatical errors and providing accurate explanations.

**Validation**: Benchmark validated through human evaluation and correlation with automatic metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
