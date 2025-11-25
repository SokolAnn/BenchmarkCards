# MedFact

## 📊 Benchmark Details

**Name**: MedFact

**Overview**: MedFact is a new benchmark for evaluating the fact-checking capabilities of large language models on Chinese medical texts. It includes 2,116 expert-annotated instances covering 13 medical specialties and aims to assess the models' performance on veracity classification and error localization.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- VeriFact
- MEDEC

**Resources**:
- [GitHub Repository](https://github.com/ivy3h/MedFact.extraction)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the factual reliability of large language models in the domain of Chinese medical texts.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Veracity Classification
- Error Localization

**Limitations**: N/A

## 💾 Data

**Source**: Curated from diverse real-world texts including medical encyclopedias and consultation websites.

**Size**: 2,116 examples

**Format**: N/A

**Annotation**: Annotated by licensed medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on model predictions compared to expert annotations.

**Interpretation**: High scores represent accurate veracity classification and successful identification of error spans.

**Baseline Results**: Human experts provide baseline performance metrics.

**Validation**: Performance validated against a human expert baseline.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
