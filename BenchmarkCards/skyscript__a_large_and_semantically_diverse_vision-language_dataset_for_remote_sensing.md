# SkyScript: A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing

## 📊 Benchmark Details

**Name**: SkyScript: A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing

**Overview**: SkyScript is a comprehensive vision-language dataset for remote sensing images, comprising 2.6 million image-text pairs covering 29K distinct semantic tags, aimed at advancing Vision Language Models (VLMs) in remote sensing tasks.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wangzhecheng/SkyScript)

## 🎯 Purpose and Intended Users

**Goal**: To create a large-scale, semantically diverse vision-language dataset for remote sensing images that facilitates the development of VLMs for various multi-modal tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Open-vocabulary Classification
- Cross-modal Retrieval
- Image Captioning
- Text-to-Image Generation

**Limitations**: SkyScript may have inherent bias due to the geographic coverage being limited to regions where high-resolution images are available, mainly the U.S. and Europe.

## 💾 Data

**Source**: Images are sourced from Google Earth Engine (GEE), which provides open access to large-scale remote sensing image collections, and semantic tags are obtained from OpenStreetMap (OSM).

**Size**: 2.6 million image-text pairs

**Format**: N/A

**Annotation**: Tags are derived from OSM and connected to images using geo-coordinates, with a tagging process involving semi-automated procedures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on performance across various downstream tasks using a continually pre-trained Vision Language Model (SkyCLIP).

**Interpretation**: Performance is interpreted based on average accuracy gains in zero-shot classifications compared to baseline models.

**Baseline Results**: SkyCLIP achieves a 6.2% average accuracy gain over baseline models.

**Validation**: SkyScript has been validated through testing on seven benchmark datasets for scene classification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: SkyScript's geographic coverage might underrepresent remote sensing imagery in developing countries.

**Potential Harm**: Potential bias from limited geographic representation in high-resolution images.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
