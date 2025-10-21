# LongBench-T2I

## 📊 Benchmark Details

**Name**: LongBench-T2I

**Overview**: LongBench-T2I is a comprehensive benchmark designed to evaluate text-to-image models under complex instructions, featuring 500 intricately designed prompts spanning nine visual evaluation dimensions.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- DrawBench
- T2I-CompBench
- DPG-Bench

**Resources**:
- [GitHub Repository](https://github.com/yczhou001/LongBench-T2I)

## 🎯 Purpose and Intended Users

**Goal**: To provide a holistic benchmark for text-to-image generation under complex instructions and propose an agent framework for effective image generation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a multi-stage pipeline using LLMs and human oversight.

**Size**: 500 prompts

**Format**: N/A

**Annotation**: Human-reviewed and generated using Large Language Models (LLMs).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Image fidelity to verbal instructions
- Nine visual elements

**Calculation**: Generated images are assessed against nine predefined visual evaluation dimensions.

**Interpretation**: Higher scores indicate better adherence to complex instructions in image generation.

**Baseline Results**: Comparison with existing benchmarks like DrawBench and T2I-CompBench.

**Validation**: Utilization of LLMs for evaluating prompt adherence and visual coherence.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
