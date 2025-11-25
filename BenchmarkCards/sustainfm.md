# SustainFM

## 📊 Benchmark Details

**Name**: SustainFM

**Overview**: SustainFM is a comprehensive benchmarking framework grounded in the 17 Sustainable Development Goals that assesses geospatial foundation models across diverse tasks ranging from asset wealth prediction to environmental hazard detection, enabling systematic evaluation of performance, generalization, and energy efficiency.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/HZDR-FWGEL)
- [GitHub Repository](https://github.com/AI4RS/SustainFM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for monitoring 16 SDGs using Earth Observation data and to evaluate foundation models in alignment with global sustainability objectives.

**Target Audience**:
- ML Researchers
- Domain Experts
- AI Practitioners

**Tasks**:
- Regression
- Change Detection
- Segmentation
- Classification

**Limitations**: N/A

## 💾 Data

**Source**: Multiple Earth Observation sources including Landsat, Sentinel-1/2, VIIRS, Google Earth, and PlanetScope.

**Size**: 723,555 image patches

**Format**: Multispectral images

**Annotation**: Pixel-level annotations for various geospatial tasks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Mean F1 Score
- Root Mean Square Error (RMSE)

**Calculation**: Metrics are calculated based on regression and classification tasks as described in the methodology.

**Interpretation**: Higher Mean F1 Score and lower RMSE indicate better model performance across tasks.

**Baseline Results**: Performance compared to traditional models like ViT and ResNet-50.

**Validation**: Performance is validated against the tasks aligned with the Sustainable Development Goals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Energy Efficiency
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: ['Environmental impact from model training']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
