# Chat2Scenario: Scenario Extraction From Dataset Through Utilization of Large Language Model

## 📊 Benchmark Details

**Name**: Chat2Scenario: Scenario Extraction From Dataset Through Utilization of Large Language Model

**Overview**: Chat2Scenario is a framework leveraging large language models to extract scenarios from naturalistic driving datasets, facilitating scenario validation for automated driving systems.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Automated Driving Systems

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ftgTUGraz/Chat2Scenario)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the efficiency of scenario extraction for validating automated driving systems using large language models.

**Target Audience**:
- Traffic Engineers
- Automated Driving System Developers
- Researchers

**Tasks**:
- Scenario Extraction
- Scenario Validation

**Limitations**: N/A

## 💾 Data

**Source**: highD dataset comprising vehicle trajectories on German highways collected via drones.

**Size**: 60 CSV files

**Format**: CSV

**Annotation**: Manually generated semantic labels through analysis.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the comparison of extracted scenarios against ground truth labels.

**Interpretation**: Higher precision indicates fewer false positives, while recall reflects the model's ability to identify true scenarios.

**Baseline Results**: N/A

**Validation**: Validated through simulations in Esmini and CarMaker.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization procedures are not specified.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
