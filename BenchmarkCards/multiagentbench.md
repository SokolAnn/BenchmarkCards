# MultiAgentBench

## 📊 Benchmark Details

**Name**: MultiAgentBench

**Overview**: MultiAgentBench is a comprehensive benchmark designed to evaluate LLM-based multi-agent systems across diverse, interactive scenarios, focusing on collaboration, competition, and coordination.

**Data Type**: task completion metrics, communication scores

**Domains**:
- Natural Language Processing
- Gaming

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- VisualAgentBench
- GAIA
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/MultiagentBench/MARBLE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM-based multi-agent collaboration and competition in various scenarios.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Multi-Agent Coordination
- Task Completion
- Social Simulation

**Limitations**: N/A

## 💾 Data

**Source**: Curated multi-agent tasks adapted from existing workloads and LLM-generated tasks with human verification.

**Size**: 100 test cases per task across 6 diverse scenarios.

**Format**: JSON, CSV

**Annotation**: Manually annotated and automatically verified by agents.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Key Performance Indicator (KPI)
- Coordination Score
- Task Score

**Calculation**: Metrics computed based on agent interactions and task completion rates.

**Interpretation**: Scores indicate effectiveness in collaboration and task completion.

**Validation**: Model performances compared against traditional benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
