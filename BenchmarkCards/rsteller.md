# RSTeller

## 📊 Benchmark Details

**Name**: RSTeller

**Overview**: RSTeller is a multimodal dataset comprising over 1.3 million remote sensing images, each accompanied by two descriptive captions, generated through a workflow that leverages large language models to create semantically rich captions from OpenStreetMap data.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SkyScript

**Resources**:
- [GitHub Repository](https://github.com/SlytherinGe/RSTeller)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, well-annotated multimodal dataset for training vision language models in remote sensing.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Captioning
- Zero-shot Classification
- Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: National Agriculture Imagery Program (NAIP) and OpenStreetMap (OSM)

**Size**: 1,309,926 images

**Format**: tar files

**Annotation**: Generated using large language models from OpenStreetMap data.

## 🔬 Methodology

**Methods**:
- LLM-based caption generation
- Image pre-processing

**Metrics**:
- MTLD

**Calculation**: MTLD score is calculated based on the Type-Token Ratio (TTR) of generated captions to assess linguistic diversity.

**Interpretation**: Higher MTLD scores indicate greater lexical diversity, reflecting richer vocabulary usage across captions.

**Baseline Results**: N/A

**Validation**: Model performance analyzed through continual pre-training and evaluations on benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
