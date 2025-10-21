# InfoQuest

## 📊 Benchmark Details

**Name**: InfoQuest

**Overview**: InfoQuest is a multi-turn chat benchmark designed to evaluate how dialogue agents handle hidden context in open-ended user requests, requiring models to engage in information-seeking dialogue through clarifying questions.

**Data Type**: dialogue exchanges

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Multi-Turn Chat
- Dialogue Competency Benchmarks

**Resources**:
- [Resource](https://huggingface.co/datasets/bryanlincoln/infoquest)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate dialogue agents in open-ended conversations

**Target Audience**:
- ML Researchers
- Dialogue System Developers

**Tasks**:
- Dialogue Evaluation
- Information-Seeking Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Generated using LLMs to simulate user requests and various personas

**Size**: 1,000 evaluation scenarios

**Format**: JSON

**Annotation**: Qualitatively assessed by evaluating dialogue agents on their ability to gather context

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation through user simulations

**Metrics**:
- Cumulative reward
- Turn efficiency

**Calculation**: Metrics calculated based on the ability of agents to ask clarifying questions and gather relevant information

**Interpretation**: Higher cumulative rewards indicate better information-seeking behavior in dialogues

**Validation**: Evaluated across multiple dialogue models in varied scenarios

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
