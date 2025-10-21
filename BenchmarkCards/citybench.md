# CityBench

## 📊 Benchmark Details

**Name**: CityBench

**Overview**: CityBench is a comprehensive evaluation benchmark for assessing the capabilities of large language models (LLMs) and vision-language models (VLMs) on diverse urban tasks through multi-modal data and interactive simulations.

**Data Type**: text, image

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/tsinghua-fib-lab/CityBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CityBench is to systematically evaluate the capabilities of LLMs and VLMs for various urban tasks.

**Target Audience**:
- ML Researchers
- Urban Planners
- Data Scientists

**Tasks**:
- Image Geolocalization
- Geospatial Prediction
- Infrastructure Inference
- GeoQA for City Elements
- Mobility Prediction
- Urban Exploration
- Outdoor Navigation
- Traffic Signal Control

**Limitations**: Current data quality varies, which may affect evaluation results.

## 💾 Data

**Source**: CityData collected from multiple urban data sources, including OpenStreetMap and Google Maps.

**Size**: 100,000 images

**Format**: N/A

**Annotation**: Manually curated and automatically generated annotations through LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall
- F1 Score
- Success Rate
- Queue Length
- Throughput

**Calculation**: Metrics are calculated based on predictions made by models in various urban tasks against ground truth.

**Interpretation**: Results are evaluated based on the ability of LLMs and VLMs to understand and process urban scenarios.

**Baseline Results**: Model performance across various urban tasks reported in comparisons with traditional methods.

**Validation**: Cross-validation methods using datasets from 13 cities to ensure representative performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Performance varies significantly across different geographical areas, indicating potential bias.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized to protect individual privacy.

**Data Licensing**: Data usage follows standard open data licenses.

**Consent Procedures**: Data collection adhered to ethical standards with respect to consent.

**Compliance With Regulations**: Not Applicable
