# SAR-TEXT

## 📊 Benchmark Details

**Name**: SAR-TEXT

**Overview**: The SAR-TEXT dataset is a large-scale dataset consisting of over 130,000 SAR image-text pairs designed for effective semantic understanding of SAR imagery, facilitating subsequent tasks like image-text retrieval, image captioning, and visual question answering.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenSARShip
- FUSAR-Map
- SSDD
- MSAR
- SADD
- SAR-AIRcraft
- SIVED
- SARDet-100k
- BRIGHT
- OpenEarthMap-SAR

**Resources**:
- [GitHub Repository](https://github.com/YiguoHe/SAR-TEXT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for advancing the understanding and interpretation of SAR imagery through automated description generation.

**Target Audience**:
- ML Researchers
- Remote Sensing Experts
- Model Developers

**Tasks**:
- Image Captioning
- Image-Text Retrieval
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The SAR-TEXT dataset is constructed using multiple publicly available SAR datasets including those for object detection, semantic segmentation, and SAR-optical pairing.

**Size**: 136,584 images

**Format**: N/A

**Annotation**: Automatically generated using the SAR-Narrator framework which integrates object detection and semantic segmentation outputs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation for generated captions

**Metrics**:
- BLEU Score
- CIDEr
- ROUGE-L
- Mean Recall

**Calculation**: Metrics are calculated based on the alignment between generated captions and reference texts or through retrieval performance on specified datasets.

**Interpretation**: Higher scores in BLEU, CIDEr, and ROUGE-L indicate better performance in generating semantically rich and accurate captions.

**Baseline Results**: N/A

**Validation**: Expansive testing against other established datasets like HRSID and OS-dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
