# GOBench (Geometric Optics Generation and Understanding Benchmark)

## 📊 Benchmark Details

**Name**: GOBench (Geometric Optics Generation and Understanding Benchmark)

**Overview**: GOBench is the first benchmark to systematically evaluate MLLMs’ ability across two tasks: 1) Generating Optically Authentic Imagery and 2) Understanding Underlying Optical Phenomena.

**Data Type**: image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/aiben-ch/GOBench)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate Multi-modal Large Language Models’ (MLLMs) abilities in geometric optical generation and understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Optical Generation
- Optical Understanding

**Limitations**: N/A

## 💾 Data

**Source**: GOBench-Gen-1K, a dataset of 1k images focusing on geometric optics scenarios.

**Size**: 1,000 images

**Format**: image files

**Annotation**: Manually filtered and graded by human experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Optical Authenticity
- Aesthetic Quality
- Instruction Fidelity

**Calculation**: Scores are calculated based on human ratings on a scale for authenticity, aesthetics, and fidelity.

**Interpretation**: Higher scores indicate better adherence to optical principles.

**Baseline Results**: Optical Authenticity scores up to 4.09 for GPT-4o-Image.

**Validation**: Results are validated by comparing model scores against human expert consensus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
