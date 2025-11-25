# WorkArena

## 📊 Benchmark Details

**Name**: WorkArena

**Overview**: WorkArena is a remote-hosted benchmark of 33 tasks based on the widely-used ServiceNow platform, designed to evaluate the performance of web agents in automating common knowledge work tasks.

**Data Type**: task instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MiniWoB
- WebArena

**Resources**:
- [GitHub Repository](https://github.com/ServiceNow/WorkArena)
- [GitHub Repository](https://github.com/ServiceNow/BrowserGym)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate web agents on tasks inspired by the daily workflow of knowledge workers in the ServiceNow platform.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Task Execution

**Limitations**: N/A

## 💾 Data

**Source**: ServiceNow platform tasks

**Size**: 19,912 unique instances

**Format**: N/A

**Annotation**: Automatically generated from human-designed templates.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Success rate

**Calculation**: Success rates calculated based on performance across various tasks.

**Interpretation**: Success rates reflect the ability of agents to perform various workplace tasks.

**Validation**: Tasks validated through oracle functions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in prompt
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
