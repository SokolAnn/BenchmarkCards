# scDrugMap

## 📊 Benchmark Details

**Name**: scDrugMap

**Overview**: scDrugMap is an integrated framework for drug response prediction that evaluates a wide range of foundation models using large-scale single-cell datasets across diverse tissue types, cancer types, and treatment regimens. This study presents the first comprehensive benchmarking of large-scale foundation models for drug response prediction in single-cell data.

**Data Type**: cell-level drug response data

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://scdrugmap.com)
- [GitHub Repository](https://github.com/QSong-github/scDrugMap)

## 🎯 Purpose and Intended Users

**Goal**: To provide a user-friendly and flexible platform for drug response prediction and to benchmark large-scale foundation models for drug discovery.

**Target Audience**:
- ML Researchers
- Drug Discovery Practitioners

**Tasks**:
- Drug Response Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets from 36 studies comprising drug response information from single-cell RNA sequencing.

**Size**: 345,607 single cells

**Format**: N/A

**Annotation**: Cell-level annotations indicating drug sensitivity/resistance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- AUROC
- Precision
- Recall

**Calculation**: Metrics are computed based on predictions versus ground truth labels for drug sensitivity and resistance.

**Interpretation**: Higher scores in F1, AUROC, precision, and recall indicate better model performance in predicting drug responses.

**Baseline Results**: N/A

**Validation**: Cross-validation performed using pooled and cross-data evaluation strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
