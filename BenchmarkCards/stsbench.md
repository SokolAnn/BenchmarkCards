# STSBench

## 📊 Benchmark Details

**Name**: STSBench

**Overview**: STSBench is a scenario-based framework to benchmark the holistic understanding of vision-language models (VLMs) for autonomous driving. It evaluates spatio-temporal reasoning capabilities of VLMs through generated multiple-choice questions from pre-defined traffic scenarios using datasets such as NuScenes.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- DriveMLLM
- NuScenes-MQA
- NuScenes-QA

**Resources**:
- [GitHub Repository](https://github.com/LRP-IVC/STSBench)
- [Resource](https://huggingface.co/datasets/ivc-lrp/STSBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the spatio-temporal reasoning capabilities of vision-language models in the context of autonomous driving.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The NuScenes dataset; pre-defined scenarios are mined and human-verified for validity.

**Size**: 971 questions

**Format**: N/A

**Annotation**: Human verification of scenarios

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correctly answered multiple-choice questions, reported as a weighted mean across all scenarios.

**Interpretation**: Higher accuracy indicates better model performance in spatio-temporal reasoning under various driving scenarios.

**Baseline Results**: Various models including LLMs and VLMs evaluated by accuracy on specific scenarios.

**Validation**: Scenarios mined from the dataset undergo human verification to ensure accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
