# VOILA

## 📊 Benchmark Details

**Name**: VOILA

**Overview**: VOILA is a large-scale, open-ended benchmark designed to evaluate MLLMs’ perceptual understanding and abstract relational reasoning through an analogical mapping approach in the visual domain.

**Data Type**: visual analogy questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VISALOGY
- V ASR

**Resources**:
- [GitHub Repository](https://github.com/nlylmz/Voila)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual understanding and analogical reasoning capabilities of state-of-the-art MLLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Reasoning
- Analogy Completion

**Limitations**: N/A

## 💾 Data

**Source**: Generated using SDXL text-to-image model with various prompts.

**Size**: Over 6.4M distinct visual analogy scenarios

**Format**: JSON

**Annotation**: Images generated manually filtered to ensure alignment with text prompts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Least-to-Most prompting

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on correct property prediction across four reasoning steps.

**Interpretation**: Higher accuracy indicates better performance in understanding visual relationships.

**Baseline Results**: Human performance averages 70% accuracy as opposed to the best MLLM performance of 29%.

**Validation**: Evaluated through extensive testing on multiple MLLMs and comparison with human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
