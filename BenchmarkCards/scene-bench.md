# Scene-Bench

## 📊 Benchmark Details

**Name**: Scene-Bench

**Overview**: Scene-Bench is a comprehensive benchmark for evaluating factual consistency in natural scene generation from scene graphs. It includes MegaSG, a dataset with one million images annotated with scene graphs, and SGScore, a novel evaluation metric that assesses accuracy of object presence and relationships.

**Data Type**: image-scene graph pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Visual Genome
- COCO-Stuff

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance factual consistency in natural scene generation from scene graphs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Images collected from COCO, Object365, and Open Images v6, annotated with scene graphs.

**Size**: 1,000,000 images

**Format**: N/A

**Annotation**: Manually annotated using multimodal large language models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- SGScore
- F1 Score

**Calculation**: SGScore evaluates the overall quality of the scene graph based on object and relationship recall.

**Interpretation**: Higher SGScore indicates better factual consistency between generated images and intended scene graphs.

**Validation**: Extensive experiments demonstrating improved factual consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
