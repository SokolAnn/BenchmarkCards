# GeoSense

## 📊 Benchmark Details

**Name**: GeoSense

**Overview**: GeoSense is the first comprehensive bilingual benchmark designed to systematically evaluate the geometric reasoning abilities of multimodal large language models (MLLMs) through the lens of geometric principles.

**Data Type**: geometric math problems

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GeoQA
- Geometry3K
- MATH

**Resources**:
- [Resource](https://doi.org/10.18653/v1/D15-1171)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the reasoning abilities of MLLMs with a focus on identifying and applying geometric principles.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Geometry Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset of geometric math problems sourced from existing benchmarks and educational websites.

**Size**: 1,789 problems

**Format**: N/A

**Annotation**: Annotated by 23 experts using a semi-automated pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Geometric Principles Identification (GPI)
- Geometric Principles Application (GPA)
- Answer accuracy (ACC)

**Calculation**: GPI and GPA scores reflect the model's performance in identifying and applying geometric principles within the visual context.

**Interpretation**: Higher GPI and GPA scores indicate better reasoning capabilities in geometric problem-solving.

**Baseline Results**: Gemini-2.0-pro-flash achieved an overall score of 65.3.

**Validation**: Models evaluated under zero-shot conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
