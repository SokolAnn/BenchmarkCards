# EgoPlan-Bench

## 📊 Benchmark Details

**Name**: EgoPlan-Bench

**Overview**: EgoPlan-Bench is a comprehensive benchmark to evaluate the planning abilities of Multimodal Large Language Models (MLLMs) in real-world scenarios from an egocentric perspective, emphasizing the evaluation of planning capabilities through realistic tasks, diverse action plans, and intricate visual observations.

**Data Type**: multiple-choice questions

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EgoThink
- PCA-Eval

**Resources**:
- [Resource](https://chenyi99.github.io/ego_plan/)
- [GitHub Repository](https://github.com/ChenYi99/EgoPlan)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the planning capabilities of MLLMs in human-level tasks based on multimodal input, including visual observations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Derived from large-scale egocentric videos such as Epic-Kitchens and Ego4D with manual verification.

**Size**: 4,939 questions

**Format**: N/A

**Annotation**: Questions are auto-generated and verified by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metric calculations are based on the proportion of correctly answered questions.

**Interpretation**: Higher accuracy indicates better planning capability of the model.

**Baseline Results**: GPT-4V achieved 37.98% accuracy.

**Validation**: The benchmark data is divided into EgoPlan-Val for validation and EgoPlan-Test for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The personal information in used videos has been meticulously de-identified.

**Data Licensing**: Released under CC BY-NC 4.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
