# CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents

## 📊 Benchmark Details

**Name**: CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents

**Overview**: CRAB is the first cross-environment agent benchmark framework, incorporating a graph-based fine-grained evaluation method and an efficient task generation method, designed to evaluate advanced Multimodal Language Models (MLMs) across various interactive environments.

**Data Type**: task-action pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/camel-ai/crab)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for evaluating multimodal language model agents in cross-environment tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Benchmark Designers

**Tasks**:
- Task Completion
- Task Planning
- Multi-Agent Coordination

**Limitations**: N/A

## 💾 Data

**Source**: CRAB Benchmark-v0 dataset comprising 120 tasks across Android and Ubuntu environments.

**Size**: 120 tasks

**Format**: JSON

**Annotation**: Automated task generation and evaluation methodologies.

## 🔬 Methodology

**Methods**:
- Graph-based evaluation
- Task decomposition and composition
- Multi-agent evaluation

**Metrics**:
- Completion Ratio (CR)
- Execution Efficiency (EE)
- Cost Efficiency (CE)

**Calculation**: Metrics are calculated based on task completions and actions performed during the evaluation.

**Interpretation**: Higher completion ratios and efficiencies indicate better agent performance across tasks.

**Baseline Results**: GPT-4o achieved a completion ratio of 38.01% in the evaluation.

**Validation**: Tasks were verified by field experts for accuracy and relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be open-sourced under Apache 2.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
