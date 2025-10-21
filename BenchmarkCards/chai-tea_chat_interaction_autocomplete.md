# ChaI-TeA (Chat Interaction Autocomplete)

## 📊 Benchmark Details

**Name**: ChaI-TeA (Chat Interaction Autocomplete)

**Overview**: A framework for evaluating autocomplete solutions for LLM-based chatbot interactions, included with a formal definition of the task, suitable datasets, and metrics.

**Data Type**: user-chatbot interaction completions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/ChaiTea-chat-interaction-autocomplete)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the autocomplete solutions in LLM-based chatbot interactions.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Autocomplete suggestion generation

**Limitations**: N/A

## 💾 Data

**Source**: Open Assistant (OASST) and ShareGPT datasets

**Size**: 90,675 conversations

**Format**: JSON

**Annotation**: Human-annotated interactions

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- saved@k
- latency

**Calculation**: Metrics are computed using exact match comparisons and proportion of text completed by the AC solutions.

**Interpretation**: Higher saved@k indicates better performance in reducing user typing effort.

**Baseline Results**: Results benchmarked across multiple LLMs including Mistral-7B and Gemma-7B.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
