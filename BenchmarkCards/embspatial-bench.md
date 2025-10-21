# EmbSpatial-Bench

## 📊 Benchmark Details

**Name**: EmbSpatial-Bench

**Overview**: EmbSpatial-Bench is a benchmark for evaluating embodied spatial understanding of Large Vision-Language Models (LVLMs), constructed from 3D environments to assess their capabilities in interpreting spatial relationships from an egocentric perspective.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mengfeidu/EmbSpatial-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the embodied spatial understanding capabilities of LVLMs in a manner that reflects their application in real-life scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spatial Relationship Identification

**Limitations**: The benchmark and findings are limited to English language and may not be suitable for outdoor environments.

## 💾 Data

**Source**: Constructed from three widely used indoor embodied datasets: Matterport3D, ScanNet, and AI2-THOR.

**Size**: 3,640 question-answering pairs

**Format**: N/A

**Annotation**: Automatically derived from annotated 3D environments and verified by humans.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of LVLMs in identifying spatial relationships.

**Interpretation**: Higher accuracy indicates better performance in embodied spatial understanding.

**Baseline Results**: Current LVLMs' best performance reached only up to 49.11% accuracy, while human performance was around 90.33%.

**Validation**: Evaluation was conducted using zero-shot performance assessment.

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

**Privacy And Anonymity**: The benchmark is built from publicly available datasets containing no personal data or offensive content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
