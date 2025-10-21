# 4KPro

## 📊 Benchmark Details

**Name**: 4KPro

**Overview**: 4KPro is a benchmark that evaluates visual perception at 4K resolution in four professional use cases including autonomous vehicle, household, gaming, and UI understanding, consisting of image QA pairs that are only solvable at 4K resolution.

**Data Type**: image QA pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TextVQA
- ChartQA
- DocVQA
- InfoVQA
- V*Bench
- RealWorldQA

**Resources**:
- [Resource](https://nvlabs.github.io/PS3)

## 🎯 Purpose and Intended Users

**Goal**: To effectively evaluate 4K-resolution perception in real-world tasks, providing a new benchmark for high-resolution visual understanding in multimodal systems.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collection of 75M high-resolution images with 282M pairs of local bounding boxes and detailed captions about salient regions, gathered from various datasets including DataComp and IDL.

**Size**: 75,000,000 images

**Format**: N/A

**Annotation**: Generated using a pipeline that involves detecting salient regions and captioning them with an MLLM.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the correct answers to QA pairs.

**Interpretation**: Higher accuracy indicates better performance in answering questions requiring 4K resolution visual understanding.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
