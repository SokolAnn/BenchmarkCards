# MATHSTICKS

## 📊 Benchmark Details

**Name**: MATHSTICKS

**Overview**: MATHSTICKS is a benchmark for Visual Symbolic Compositional Reasoning (VSCR) that unifies visual perception, symbolic manipulation, and arithmetic consistency through matchstick puzzles. Models must correct invalid matchstick equations by moving one or two sticks while maintaining stick conservation.

**Data Type**: text

**Domains**:
- Computer Vision
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- CLEVR
- MathVista

**Resources**:
- [GitHub Repository](https://github.com/Yuheng2000/MathSticks)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous testbed for advancing compositional reasoning across vision and symbols.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Symbolic Reasoning
- Visual Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Generated matchstick instances with a two-stage generation pipeline ensuring mathematical solvability and visual fidelity.

**Size**: 1,411,388 instances

**Format**: N/A

**Annotation**: Automatically generated via symbolic enumeration and visual rendering, with diagnostic labels for complexity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on model correctness against a ground-truth set of matchstick configurations.

**Interpretation**: Higher accuracy reflects better reasoning and visual-symbolic manipulation capabilities.

**Validation**: Validated through experiments with 14 vision-language models and human participants.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
