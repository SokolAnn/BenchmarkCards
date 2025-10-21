# VIR-Bench

## 📊 Benchmark Details

**Name**: VIR-Bench

**Overview**: VIR-Bench is a novel benchmark consisting of 200 travel videos that frames itinerary reconstruction as a challenging task designed to evaluate and push forward MLLMs’ geospatial-temporal intelligence.

**Data Type**: video

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Japanese

**Similar Benchmarks**:
- Ego4D
- HourVideo
- CityGuessr

**Resources**:
- [GitHub Repository](https://github.com/nlp-waseda/VIR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate long-range geospatial-temporal understanding via itinerary reconstruction from travel vlog videos.

**Target Audience**:
- Research Community
- Machine Learning Practitioners

**Tasks**:
- Node Prediction
- Edge Prediction

**Limitations**: N/A

## 💾 Data

**Source**: 200 travel videos filmed across Japan, each paired with a corresponding visiting order graph.

**Size**: 200 videos

**Format**: JSON

**Annotation**: Manually annotated and double-reviewed visiting order graphs.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Macro-averaged precision, recall, and F1 across both node and edge prediction.

**Interpretation**: Performance is assessed based on the exact matching of predicted locations and edges to the ground truth.

**Baseline Results**: N/A

**Validation**: Evaluated on state-of-the-art open-weight and proprietary MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['N/A']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is released strictly for research purposes and commercial use is prohibited.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
