# MMSafeAware (Multimodal Safety Awareness Benchmark)

## 📊 Benchmark Details

**Name**: MMSafeAware (Multimodal Safety Awareness Benchmark)

**Overview**: MMSafeAware is a comprehensive multimodal safety awareness benchmark designed to evaluate Multimodal Large Language Models (MLLMs) across 29 safety scenarios with 1,500 carefully curated image-prompt pairs. It includes both unsafe and over-safety subsets to assess the models' abilities to correctly identify unsafe content and avoid over-sensitivity.

**Data Type**: image-prompt pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MM-Safety
- MossBench

**Resources**:
- [GitHub Repository](https://github.com/Jarviswang94/MMSafetyAwareness)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety awareness of Multimodal Large Language Models and to highlight shortcomings in their ability to identify unsafe content while avoiding over-sensitivity.

**Target Audience**:
- ML Researchers
- AI Safety Researchers
- Model Developers

**Tasks**:
- Safety Awareness Evaluation

**Limitations**: Current methods to improve safety awareness do not fully address the challenges posed by the benchmark.

## 💾 Data

**Source**: Carefully curated image-prompt pairs constructed from safety scenarios.

**Size**: 1,500 image-prompt pairs

**Format**: N/A

**Annotation**: All data have been manually checked by human annotators to ensure quality.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed based on the models' ability to correctly classify each image-prompt pair as safe or unsafe.

**Interpretation**: Higher accuracy indicates that the evaluated MLLM has better safety awareness.

**Baseline Results**: Accuracy of evaluated MLLMs ranges from 1.1% to 100.0% on different safety scenarios.

**Validation**: Validation was conducted through extensive testing on multiple models across various safety scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark includes toxic images, but it does not aim to generate such images, rather to raise awareness of the safety issues in MLLMs.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
