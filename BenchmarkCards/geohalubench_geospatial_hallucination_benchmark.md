# GEOHALUBENCH (Geospatial Hallucination Benchmark)

## 📊 Benchmark Details

**Name**: GEOHALUBENCH (Geospatial Hallucination Benchmark)

**Overview**: GEOHALUBENCH is a comprehensive evaluation framework aimed at systematically assessing and mitigating geospatial hallucinations in large language models (LLMs) through structured questions derived from geospatial knowledge graphs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA

**Resources**:
- [Resource](https://anonymous.4open.science/r/GeospatialHallucination-823A/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and mitigate geospatial hallucinations in large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Geospatial Knowledge Assessment
- Hallucination Detection
- Hallucination Mitigation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from OpenStreetMap and Foursquare's Open Source Places.

**Size**: 2,100 instances across various city regions.

**Format**: Multiple choice questions

**Annotation**: Automatically generated based on factual knowledge and hallucination patterns.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation metrics based on macro-averaged accuracy across geospatial tasks.

**Interpretation**: Higher accuracy indicates better performance in correctly identifying factual information versus hallucinations.

**Validation**: Evaluated across 20 advanced LLMs with detailed error analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All data is sourced from publicly available databases under respective licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
