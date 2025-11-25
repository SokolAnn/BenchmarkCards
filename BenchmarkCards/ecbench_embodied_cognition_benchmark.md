# ECBench (Embodied Cognition Benchmark)

## 📊 Benchmark Details

**Name**: ECBench (Embodied Cognition Benchmark)

**Overview**: ECBench is a high-quality benchmark designed to systematically evaluate the embodied cognitive abilities of large vision-language models (LVLMs) using egocentric videos. It features diverse scene video sources, varied question formats, and 30 dimensions of embodied cognition.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ScanQA
- SQA3D
- OpenEQA

**Resources**:
- [GitHub Repository](https://github.com/Rh-Dang/ECBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for the embodied cognitive abilities of large vision-language models in egocentric contexts.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Due to budget constraints, not all proprietary models were tested. The evaluation is limited to under five minutes of video inputs.

## 💾 Data

**Source**: 386 RGB-D videos from ScanNet, MultiScan, HM3D, and self-collected scenes.

**Size**: 4,324 question-answering pairs

**Format**: N/A

**Annotation**: Class-independent meticulous human annotation with multi-round question screening.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores are generated based on a multi-level evaluation framework integrating binary scoring for closed questions and continuous scoring for open-ended responses.

**Interpretation**: Scores provide insights into the performance of LVLMs in both static and dynamic scenarios, as well as hallucination issues.

**Baseline Results**: Scores from various LVLMs, including GPT-4o.

**Validation**: Cross-validation on all questions to ensure QA pair accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
