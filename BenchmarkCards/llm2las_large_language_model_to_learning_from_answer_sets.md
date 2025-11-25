# LLM2LAS (Large Language Model to Learning from Answer Sets)

## 📊 Benchmark Details

**Name**: LLM2LAS (Large Language Model to Learning from Answer Sets)

**Overview**: LLM2LAS is a hybrid system that combines the natural language understanding capabilities of large language models with the rule induction power of Learning from Answer Sets (LAS) and the formal reasoning strengths of Answer Set Programming (ASP) to improve question answering capabilities by automatically learning from examples.

**Data Type**: question-answering pairs

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- bAbI

**Resources**:
- [GitHub Repository](https://github.com/IrfanKareem/llm2las/tree/journal)
- [Resource](https://arxiv.org/abs/2509.16590)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of LLM2LAS is to automate the learning of commonsense knowledge and reasoning capabilities from examples in story-based question answering tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Logic Programming Researchers
- Natural Language Processing Researchers

**Tasks**:
- Commonsense Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: bAbI dataset from Facebook Research

**Size**: Varies by task, up to 20 tasks

**Format**: Text

**Annotation**: Automatically generated symbolic representations from narrative texts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Learning from Answer Sets

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured as the ratio of correct answers in comparison to total questions answered.

**Interpretation**: A higher accuracy indicates a more effective learning and reasoning process by the LLM2LAS system.

**Baseline Results**: Compared against existing logic programming approaches, achieving similar accuracy levels.

**Validation**: Empirical validation conducted on various tasks within the bAbI dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
