# NavBench

## 📊 Benchmark Details

**Name**: NavBench

**Overview**: NavBench is a benchmark designed to systematically evaluate Multimodal Large Language Models (MLLMs) in embodied navigation under zero-shot settings, decomposing the evaluation into Navigation Comprehension and Navigation Execution, covering various reasoning capabilities and execution tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- R2R
- ObjectNav

**Resources**:
- [Resource](https://arxiv.org/abs/2506.01031)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the embodied navigation capabilities of MLLMs and provide insights into their reasoning and execution performance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Embodied Navigation
- Multi-modal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Matterport3D simulator and existing embodied navigation datasets such as R2R, RxR, GEL-R2R.

**Size**: 3,200 question-answer pairs and 432 navigation episodes across 72 scenes

**Format**: N/A

**Annotation**: Constructed using human evaluation and automatic scoring mechanisms.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Success Rate (SR)
- Success weighted by Path Length (SPL)

**Calculation**: Metrics are calculated based on the model's correct predictions in multiple-choice tasks and evaluation of navigation success.

**Interpretation**: A higher score indicates better performance in navigation comprehension and execution.

**Validation**: Evaluated using both simulation and real-world deployment experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
