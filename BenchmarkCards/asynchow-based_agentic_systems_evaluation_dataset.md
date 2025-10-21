# AsyncHow-Based Agentic Systems Evaluation Dataset

## 📊 Benchmark Details

**Name**: AsyncHow-Based Agentic Systems Evaluation Dataset

**Overview**: The dataset is designed to evaluate the agentic behavior of LLM-driven systems across various domains and tasks, focusing on task graph generation, tool selection, and system performance analysis.

**Data Type**: task graphs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- VisualAgentBench
- TASKBENCH
- AgentQuest

**Resources**:
- [Resource](https://example.com/AsyncHow-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate agentic frameworks in generating task graphs, selecting tools, and executing tasks in complex scenarios.

**Target Audience**:
- ML Researchers
- AI Practitioners
- System Designers

**Tasks**:
- Task Graph Generation
- Tool Selection
- Task Execution

**Limitations**: The dataset does not support multi-agent communication, which may limit its usability in collaborative scenarios.

## 💾 Data

**Source**: Based on the AsyncHow dataset, designed to cover parallel and sequential task graphs.

**Size**: 50 task scenarios

**Format**: JSON

**Annotation**: Synthetic Python functions generated to mimic real-world tools.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Node F1 Score
- Tool F1 Score
- Structural Similarity Index (SSI)

**Calculation**: Calculated using precision, recall, and F1 Score metrics for nodes and tools.

**Interpretation**: Higher scores indicate better performance in task decomposition and tool selection accuracy.

**Validation**: Validation performed through empirical analysis and statistical testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
