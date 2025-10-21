# GSR-B ENCH (Grounded Spatial Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: GSR-B ENCH (Grounded Spatial Reasoning Benchmark)

**Overview**: A novel comprehensive evaluation for spatial relationship understanding that highlights the strengths and weaknesses of Multimodal LLMs, extending the What’sUp dataset with additional annotations.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- What’sUp
- MMBench

**Resources**:
- [Resource](https://arxiv.org/abs/2406.13246)

## 🎯 Purpose and Intended Users

**Goal**: To provide a carefully curated benchmark for spatial relationship understanding evaluation in a controlled setting.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spatial Relationship Understanding
- Image-Text Matching

**Limitations**: The dataset is smaller than existing benchmarks related to spatial reasoning and confined to basic spatial clauses.

## 💾 Data

**Source**: Extended What’sUp dataset with additional annotations.

**Size**: 4,958 images

**Format**: N/A

**Annotation**: Annotated with bounding box coordinates, segmentation masks, and depth maps.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Template-based generation

**Metrics**:
- Accuracy
- Intersection over Union (IoU)

**Calculation**: Metrics calculated using CircularEval and IoU thresholds for localization accuracy.

**Interpretation**: A prediction is considered correct if it meets the accuracy or IoU criteria specified.

**Validation**: The benchmark was validated through comparisons with existing VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
