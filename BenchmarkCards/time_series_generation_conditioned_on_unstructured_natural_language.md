# Time Series Generation Conditioned on Unstructured Natural Language

## 📊 Benchmark Details

**Name**: Time Series Generation Conditioned on Unstructured Natural Language

**Overview**: The paper introduces a method for generating time series based on unstructured natural language descriptions and a novel dataset consisting of 63,010 time series-description pairs.

**Data Type**: time-series-description pairs

**Domains**:
- Finance
- Climate

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uchidalab/ts-generation)

## 🎯 Purpose and Intended Users

**Goal**: To generate time series data conditioned on natural language descriptions using a diffusion model.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Time Series Generation
- Data Augmentation

**Limitations**: The dataset may contain ambiguous descriptions, and the model has limitations in generating time series of varying lengths.

## 💾 Data

**Source**: Constructed from various datasets including stock data, UCR Time Series Classification Archive, and synthetic data.

**Size**: 63,010 time series-description pairs

**Format**: CSV

**Annotation**: Descriptions generated using GPT-4o for the time series data.

## 🔬 Methodology

**Methods**:
- Diffusion Model
- Denoising U-Net

**Metrics**:
- Euclidean Distance
- Dynamic Time Warping

**Calculation**: Metrics are calculated as pair-wise distances between generated time series and ground truth.

**Interpretation**: Lower distances indicate better alignment between generated time series and prompts.

**Validation**: The model's performance is evaluated based on the quality of generated time series with various prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
