# ImgEdit: A Unified Image Editing Dataset and Benchmark

## 📊 Benchmark Details

**Name**: ImgEdit: A Unified Image Editing Dataset and Benchmark

**Overview**: ImgEdit introduces a large-scale, high-quality image-editing dataset comprising 1.2 million carefully curated edit pairs for both single-turn and complex multi-turn editing tasks. It includes a benchmark designed to evaluate image editing performance across various dimensions, significantly advancing the capabilities of open-source image-editing models.

**Data Type**: image-editing pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PKU-YuanGroup/ImgEdit)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive, high-quality dataset and benchmark for evaluating image editing models, facilitating advancements in the field by overcoming limitations found in existing datasets.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Image Editing
- Multi-Turn Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various high-quality image datasets using advanced data generation pipelines.

**Size**: 1.2 million image-editing pairs

**Format**: N/A

**Annotation**: Carefully curated and verified using a multi-stage pipeline integrating vision-language models, segmentation models, and human-assisted evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Instruction adherence
- Image-editing quality
- Detail preservation

**Calculation**: Metrics are calculated based on ratings assigned by a vision-language model (GPT-4o), which assesses adherence to instructions and the quality of the edited images.

**Interpretation**: Scores are interpreted based on adherence to prompts and quality of edits, with a higher score indicating better performance.

**Validation**: Validation was conducted through comparative analysis of outputs from various models against the key metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
