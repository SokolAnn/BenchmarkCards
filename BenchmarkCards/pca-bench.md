# PCA-Bench

## 📊 Benchmark Details

**Name**: PCA-Bench

**Overview**: PCA-Bench is a multimodal decision-making benchmark designed for evaluating the integrated capabilities of Multimodal Large Language Models (MLLMs) across scenarios such as autonomous driving, domestic robotics, and open-world games, emphasizing error localization and integrated task performance.

**Data Type**: image-question-action pairs

**Domains**:
- Natural Language Processing
- Robotics
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMMU
- MathVista

**Resources**:
- [GitHub Repository](https://github.com/username/repo)
- [Resource](https://arxiv.org/abs/2402.15527)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate integrated decision-making capabilities of MLLMs in multimodal contexts with a focus on error localization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Decision Making
- Image Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Instances are derived from environments related to autonomous driving, domestic robotics, and open-world gaming, including datasets like TT100K and ALFRED.

**Size**: 7,510 training samples

**Format**: N/A

**Annotation**: Annotated by human experts with a tuple: <image, question, action candidates, answer, reason, key concept>.

## 🔬 Methodology

**Methods**:
- Automatic evaluation using PCA-Eval
- Human evaluation

**Metrics**:
- Perception Score
- Cognition Score
- Action Score

**Calculation**: Scores based on model outputs compared to ground truth answers.

**Interpretation**: Scores are binary, indicating whether the model's outputs match expected outcomes.

**Baseline Results**: N/A

**Validation**: Tests the performance of 10 prevalent MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
