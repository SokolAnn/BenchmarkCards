# RealKIE

## 📊 Benchmark Details

**Name**: RealKIE

**Overview**: We introduce RealKIE, a benchmark of five challenging datasets aimed at advancing key information extraction methods, with an emphasis on enterprise applications. The datasets include a diverse range of documents including SEC S1 Filings, US Non-disclosure Agreements, UK Charity Reports, FCC Invoices, and Resource Contracts.

**Data Type**: Document-level key information extraction datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://indicodatasolutions.github.io/RealKIE/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development of NLP models capable of handling practical challenges and support further research into information extraction technologies applicable to industry-specific problems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Key Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Five unique enterprise document sources including SEC S1 Filings, US Non-disclosure Agreements, UK Charity Reports, FCC Invoices, and Resource Contracts.

**Size**: N/A

**Format**: PDF

**Annotation**: Manually annotated text spans referenced against OCR outputs.

## 🔬 Methodology

**Methods**:
- Token Classification
- Hyperband Bayesian Hyper-parameter Search

**Metrics**:
- F1 Score
- Macro F1

**Calculation**: Models are fine-tuned and evaluated based on the best validation set F1 scores.

**Interpretation**: Higher F1 scores indicate better performance on key information extraction tasks.

**Baseline Results**: Results vary per dataset with detailed performance metrics available for models like RoBERTa, DeBERTa, LayoutLM, and Longformer.

**Validation**: Models validated against training and held-out test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
