# MineBench

## 📊 Benchmark Details

**Name**: MineBench

**Overview**: MineBench is a benchmark tailored for multimodal mineral exploration tasks, aiming to evaluate MLLMs in reasoning over domain-specific remote-sensing data.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://data.dea.ga.gov.au/?prefix=ASTER_)
- [Resource](https://map.sarig.sa.gov.au/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate MLLMs in mineral exploration using geological and hyperspectral data.

**Target Audience**:
- ML Researchers
- Domain Experts
- Geoscience Professionals

**Tasks**:
- Text Classification
- Image Classification
- Multimodal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Geoscience Western Australia (GSWA) remote-sensing dataset

**Size**: 73 positive areas and 539 negative areas

**Format**: N/A

**Annotation**: Human-annotated classes based on geological features.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- ROC-AUC
- Matthews Correlation Coefficient (MCC)

**Calculation**: Metrics are calculated based on model outputs compared to human-annotated classifications and ground truth labels.

**Interpretation**: Scores close to 1 indicate high confidence in mineralization presence, while lower scores indicate uncertainty.

**Baseline Results**: Pos.F1 of 34.93% for Random Choice model without MineAgent, with improvements up to 61.20% with MineAgent.

**Validation**: Rigorous review by geoscience experts ensured data quality and classification reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
