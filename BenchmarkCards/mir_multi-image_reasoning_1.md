# MIR (Multi-Image Reasoning)

## 📊 Benchmark Details

**Name**: MIR (Multi-Image Reasoning)

**Overview**: MIR is designed for multi-image interleaved reasoning, requiring joint reasoning over multiple images along with interleaved textual contexts. It features a structured five-stage reasoning process to guide models in understanding the relationships between images and texts.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- NaturalBench
- MMIU
- MIRBENCH
- BLINK
- MUIRBench

**Resources**:
- [GitHub Repository](https://github.com/Shelly-coder239/MIRBench)

## 🎯 Purpose and Intended Users

**Goal**: To enhance MLLMs' reasoning capabilities and facilitate advancements in multi-image interleaved reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Original recordings, publicly accessible content, and educational resources.

**Size**: 138,277 images and 22,257 multiple-choice questions

**Format**: multiple-choice questions

**Annotation**: Semi-automated with human validation

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Stage-wise curriculum learning

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the number of correct answers out of total questions.

**Interpretation**: A higher accuracy indicates better performance in inter-image reasoning.

**Baseline Results**: N/A

**Validation**: Extensive experiments benchmarking multiple MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
