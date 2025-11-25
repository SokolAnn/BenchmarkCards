# VLKEB (Large Vision-Language Model Knowledge Editing Benchmark)

## 📊 Benchmark Details

**Name**: VLKEB (Large Vision-Language Model Knowledge Editing Benchmark)

**Overview**: A benchmark designed to assess and improve the capabilities of knowledge editing methods in the field of LVLMs, featuring more reliable data collection methods and an extended Portability metric.

**Data Type**: editing cases with image and text inputs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMEdit

**Resources**:
- [GitHub Repository](https://github.com/VLKEB/VLKEB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve knowledge editing methods for LVLMs.

**Target Audience**:
- ML Researchers
- Practitioners

**Tasks**:
- Knowledge Editing
- Question Answering
- Image Recognition

**Limitations**: N/A

## 💾 Data

**Source**: MMKG (Multi-modal Knowledge Graph)

**Size**: 8174 editing cases with 18434 images

**Format**: JSON along with images sorted by entity IDs

**Annotation**: Manually constructed using GPT for question generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Reliability
- Generality
- Locality
- Portability

**Calculation**: Evaluation metrics are calculated based on the proportion of correct answers produced by edited models across different inputs.

**Interpretation**: High scores indicate effective editing and retention of knowledge integrity, while low scores highlight performance deficiencies.

**Baseline Results**: N/A

**Validation**: Evaluation conducted on five different LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
