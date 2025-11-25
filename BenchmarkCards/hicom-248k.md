# HICom-248K

## 📊 Benchmark Details

**Name**: HICom-248K

**Overview**: HICom-248K is a dataset designed for conditional pre-training in multi-modal large language models (MLLMs), consisting of 248K video clips annotated with instruction-followed descriptions to improve video understanding in MLLMs.

**Data Type**: instruction-followed descriptions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/lntzm/HICom)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the efficiency and effectiveness of video understanding in multi-modal large language models via conditional pre-training using HICom-248K.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Video Understanding
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Panda-70M and Ego4D datasets

**Size**: 248,000 video clips

**Format**: N/A

**Annotation**: Generated instruction-followed descriptions using Qwen2-VL-72B-Instruct.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- A/B testing

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated by comparing the performance of models using HICom-248K against established benchmarks.

**Interpretation**: Higher performance indicates better instruction-followed comprehension and efficiency in video understanding.

**Baseline Results**: Comparative performance increases of 2.43% average across three multiple-choice QA benchmarks vs existing models.

**Validation**: Evaluated through performance benchmarks in video understanding tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Preserving instruction-relevant visual content while reducing tokens can mitigate the risk of overlooking vital information.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
