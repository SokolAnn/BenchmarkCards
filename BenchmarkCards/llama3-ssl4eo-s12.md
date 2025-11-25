# Llama3-SSL4EO-S12

## 📊 Benchmark Details

**Name**: Llama3-SSL4EO-S12

**Overview**: The largest multispectral image-caption dataset for Earth Observation, consisting of one million Sentinel-2 samples with corresponding textual descriptions generated for contrastive learning.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChatEarthNet
- SkyScript
- BLIP-2

**Resources**:
- [GitHub Repository](https://github.com/IBM/MS-CLIP)
- [Resource](https://huggingface.co/datasets/ibm-esa-geospatial/Llama3-SSL4EO-S12-v1.1-captions)

## 🎯 Purpose and Intended Users

**Goal**: To create a large-scale dataset of multispectral imagery with captions for improving vision-language models in Earth observation.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Zero-shot Classification
- Text-to-Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Multispectral imagery from Sentinel-2 satellites with generated captions.

**Size**: 1,000,000 samples

**Format**: N/A

**Annotation**: Automated captioning using a multimodal large language model.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Mean Average Precision (mAP)

**Calculation**: Calculated similarity scores between images and class labels for classification, and average precision for text-to-image retrieval.

**Interpretation**: Higher accuracy and mAP indicate better performance of the model.

**Baseline Results**: Llama3-MS-CLIP achieves a top-1 accuracy of 58.54% and mAP@100 of 42.79%.

**Validation**: Studied using zero-shot evaluation across three different datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Permissive license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
