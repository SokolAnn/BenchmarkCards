# Rendezvous (RVS)

## 📊 Benchmark Details

**Name**: Rendezvous (RVS)

**Overview**: The RVS task and dataset present a new focus on understanding geospatial instructions based on survey knowledge of urban environments, requiring models to handle allocentric spatial relations and multiple references simultaneously.

**Data Type**: geospatial instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RUN
- TOUCHDOWN
- RXR

**Resources**:
- [GitHub Repository](https://github.com/OnlpLab/RVS)

## 🎯 Purpose and Intended Users

**Goal**: To advance systems that can interpret high-level survey knowledge-based navigation instructions based on urban environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Geolocation
- Spatial reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced instructions for navigation based on a map representation of urban environments.

**Size**: 10,404 examples

**Format**: N/A

**Annotation**: Crowdsourced, validated instructions with a two-task process involving instruction writing and validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- 100m accuracy
- 250m accuracy
- Mean distance error
- Median distance error
- Max distance error
- Area under the curve (AUC) distance error

**Calculation**: Metrics are calculated based on the distance from predicted geolocation to actual location.

**Interpretation**: A task is considered successful if the predicted goal is within a specified distance of the actual goal.

**Validation**: Validation involved multiple participants assessing agreement on the correctness of instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
