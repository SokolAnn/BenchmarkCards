# EarthDial

## 📊 Benchmark Details

**Name**: EarthDial

**Overview**: EarthDial is a conversational assistant specifically designed for Earth Observation (EO) data, transforming complex, multi-sensory Earth observations into interactive, natural language dialogues. It supports multi-spectral, multi-temporal, and multi-resolution imagery, enabling a wide range of remote sensing tasks including classification, detection, captioning, question answering, visual reasoning, and visual grounding. The exhaustive instruction tuning dataset comprises over 11.11M instruction pairs to improve generalization across various EO tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hiyamdebary/EarthDial)

## 🎯 Purpose and Intended Users

**Goal**: To develop a domain-specialized Vision-Language Model (VLM) that can cohesively process multi-resolution, multi-spectral, and multi-temporal remote sensing imagery to unlock numerous downstream tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Classification
- Object Detection
- Image Captioning
- Visual Question Answering
- Change Detection
- Disaster Assessment
- Tree Species Classification
- Urban Heat Island Detection
- Local Climate Zones Detection

**Limitations**: N/A

## 💾 Data

**Source**: The EarthDial-Instruct dataset consists of images from various remote sensing data sources and comprehensive instructions generated based on these images.

**Size**: 11.11M instruction pairs

**Format**: N/A

**Annotation**: Generated using labels and quality filtering processes to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance of the model across various EO tasks evaluated on different datasets.

**Interpretation**: Higher accuracy indicates better performance in classifying tasks and interpreting EO data.

**Baseline Results**: Compared against other existing models such as GPT-4o and GeoChat.

**Validation**: EarthDial was validated through extensive experiments on 44 downstream datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
