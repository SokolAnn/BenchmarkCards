# ANDROID LAB

## 📊 Benchmark Details

**Name**: ANDROID LAB

**Overview**: ANDROID LAB provides a systematic Android agent framework, including a reproducible benchmark for evaluating mobile agent capabilities across multiple apps and tasks, featuring both large language models (LLMs) and multimodal models (LMMs). The benchmark includes 138 tasks derived from nine apps that assess the capabilities of autonomous agents in interacting with an Android operating system.

**Data Type**: task-action pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/THUDM/Android-Lab)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and reproducible benchmark framework for training and evaluating Android agents interacting with mobile applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Task Completion
- Query Answering

**Limitations**: N/A

## 💾 Data

**Source**: Tasks designed for common mobile scenarios across nine apps including Bluecoins, Calendar, Contacts, Clock, Maps.me, PiMusic, Settings, and Zoom.

**Size**: 138 tasks

**Format**: N/A

**Annotation**: Manual annotation by experts combining self-exploration and verification steps through an online annotation tool.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Success Rate
- Sub-Goal Success Rate
- Reversed Redundancy Ratio
- Reasonable Operation Ratio

**Calculation**: Metrics are calculated based on the achievement of task goals, monitored through UI state assessment.

**Interpretation**: Higher success rates indicate better performance of the model in executing tasks.

**Baseline Results**: The best overall model performing in XML mode achieved a success rate of 43 tasks out of 138 across various apps, with significant improvements noted after fine-tuning.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Enhancing mobile agent accessibility and performance for diverse user interactions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators are informed of data usage policies and can opt-out if privacy concerns arise.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
