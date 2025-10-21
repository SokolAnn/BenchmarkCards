# EEE-Bench (Electrical and Electronics Engineering Benchmark)

## 📊 Benchmark Details

**Name**: EEE-Bench (Electrical and Electronics Engineering Benchmark)

**Overview**: EEE-Bench is a pioneering multimodal benchmark designed for assessing the reasoning abilities of Large Multimodal Models (LMMs) in electrical and electronics engineering (EEE) problems. It consists of 2860 samples spanning 10 essential subjects, featuring a diverse range of visual contexts such as electric and digital circuits, system diagrams, and more.

**Data Type**: multiple-choice and free-form questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2411.01492)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the abilities of LLMs and LMMs in their capability to tackle rigorous engineering reasoning tasks and to highlight limitations of current foundation models in solving EEE problems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Problem Solving
- Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Collection of problems from official EEE exams and verified online resources.

**Size**: 2,860 questions

**Format**: JSON

**Annotation**: Manual curation and selection of high-quality questions with visual aspects.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluations

**Metrics**:
- Accuracy

**Calculation**: The accuracy of models was calculated as the proportion of correctly answered questions out of the total.

**Interpretation**: An accuracy of 50% or above indicates satisfactory performance, while anything below suggests significant room for improvement.

**Validation**: Extensive experiments carried out using various models to cross-validate results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
