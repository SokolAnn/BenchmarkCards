# SF2Bench (South Florida Flood Benchmark)

## 📊 Benchmark Details

**Name**: SF2Bench (South Florida Flood Benchmark)

**Overview**: SF2Bench is a comprehensive time series dataset on compound floods in South Florida, integrating factors such as tide, rainfall, groundwater, and human management activities. It aims to enhance flood forecasting and evaluation of various modeling paradigms.

**Data Type**: time-series

**Domains**:
- Natural Language Processing
- Environmental Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AslanDing/SFBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for the systematic analysis of compound floods in South Florida, driving advancements in modeling and forecasting methodologies.

**Target Audience**:
- ML Researchers
- Environmental Scientists
- Model Developers

**Tasks**:
- Time Series Forecasting

**Limitations**: While SF2Bench covers crucial driving factors, it currently lacks explicit topological linkage information between monitoring stations.

## 💾 Data

**Source**: Compiled from 2,452 monitoring stations across South Florida, sourced from the South Florida Water Management District.

**Size**: Data spans from 1985 to 2024, consisting of various time series relating to water levels, rainfall, groundwater, and human control activities.

**Format**: CSV

**Annotation**: Data was processed through interpolation and standardized for time series analysis.

## 🔬 Methodology

**Methods**:
- Multilayer Perceptrons (MLP)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- Graph Neural Networks (GNN)
- Transformers
- Large Language Models

**Metrics**:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Symmetric Extremal Dependence Index (SEDI)

**Calculation**: Metrics are calculated based on standard time series forecasting practices.

**Interpretation**: Lower MAE and MSE values indicate better performance, while higher SEDI values reflect better predictions of extreme flood events.

**Baseline Results**: Various architectures were evaluated with specific performance metrics detailed within the experimental setups.

**Validation**: Cross-validation was employed using data splits from the collected time series.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**

**Demographic Analysis**: Analysis provides insights into flood dynamics and performance across different regions in South Florida.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
