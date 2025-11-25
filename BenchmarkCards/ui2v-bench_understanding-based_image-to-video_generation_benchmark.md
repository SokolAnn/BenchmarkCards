# UI2V-Bench (Understanding-based Image-to-Video Generation Benchmark)

## 📊 Benchmark Details

**Name**: UI2V-Bench (Understanding-based Image-to-Video Generation Benchmark)

**Overview**: UI2V-Bench is a benchmark for evaluating image-to-video (I2V) generation models, focusing on semantic understanding and reasoning abilities across four primary evaluation dimensions: spatial understanding, attribute binding, category understanding, and reasoning. It introduces new metrics and methods for assessing these capabilities.

**Data Type**: text-image pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- AIGCBench
- AnimateBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and reliable framework for evaluating image-to-video models, emphasizing semantic comprehension and logical reasoning.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Image-to-Video Generation

**Limitations**: The benchmark currently only includes typical and common evaluation dimensions, lacking cases for complex spatial arrangements.

## 💾 Data

**Source**: Approximately 500 carefully constructed text-image pairs sourced from open-access websites such as Unsplash and Pexels.

**Size**: 500 pairs

**Format**: N/A

**Annotation**: Human evaluations along with automated MLLM-based metrics.

## 🔬 Methodology

**Methods**:
- Instance-level evaluation based on semantic understanding
- Feedback-based evaluation for reasoning capabilities

**Metrics**:
- Spatial Understanding
- Attribute Binding
- Category Understanding
- Reasoning

**Calculation**: Metrics are calculated based on the alignment of generated videos with input prompts and expected outcomes.

**Interpretation**: High scores indicate better semantic alignment and reasoning capabilities, as assessed by MLLMs and human evaluators.

**Validation**: Human evaluations show strong alignment with the proposed metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
