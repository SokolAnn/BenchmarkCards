# Driving QA Dataset

## 📊 Benchmark Details

**Name**: Driving QA Dataset

**Overview**: The paper introduces a dataset of 160,000 question-answering pairs derived from 10,000 driving scenarios, designed to improve context understanding in driving situations using a multimodal LLM architecture that merges vectorized numeric modalities with a pre-trained LLM.

**Data Type**: question-answering pairs

**Domains**:
- Autonomous Driving
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wayveai/Driving-with-LLMs)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to facilitate advancements in the field of autonomous driving by enabling question-answering capabilities relevant to driving scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of question-answer pairs generated using a structured language generator from a custom-built 2D simulator and an RL agent.

**Size**: 160,000 pairs

**Format**: JSON

**Annotation**: Automatically generated using a language model (GPT-3.5) acting as a professional driving instructor.

## 🔬 Methodology

**Methods**:
- Automatic annotation using GPT
- Evaluation using expert LLM grader

**Metrics**:
- Mean Absolute Error
- Accuracy

**Calculation**: Metrics are calculated based on evaluation of driving QA tasks and action prediction tasks.

**Interpretation**: Performance in driving tasks is evaluated based on the number of cars/pedestrians detected and the accuracy of action predictions.

**Baseline Results**: The benchmark provides initial evaluation results using a separate evaluation set.

**Validation**: The driving QA outputs and predictions are validated using both automated grading and human grading.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
