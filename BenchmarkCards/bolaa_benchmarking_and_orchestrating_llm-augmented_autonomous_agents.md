# BOLAA (Benchmarking and Orchestrating LLM-augmented Autonomous Agents)

## 📊 Benchmark Details

**Name**: BOLAA (Benchmarking and Orchestrating LLM-augmented Autonomous Agents)

**Overview**: BOLAA is a new benchmark that systematically evaluates LLM-augmented Autonomous Agents (LAAs) across various agent architectures and LLM backbones. It aims to address the gaps in understanding and orchestrating multiple LAAs for handling complex tasks in simulated environments.

**Data Type**: task-based interactions

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench

**Resources**:
- [GitHub Repository](https://github.com/salesforce/BOLAA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive comparison and benchmark for LLM-augmented Autonomous Agents (LAAs) in complex task environments.

**Target Audience**:
- ML Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Multi-agent coordination
- Task complexity evaluation
- Decision-making
- Knowledge reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Simulated environments including WebShop and HotPotQA.

**Size**: 900 tasks for WebShop, 300 questions for HotPotQA

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Average reward score
- Recall performance

**Calculation**: Metrics based on the reward score defined as the attribute overlapping ratio and F1 score grading.

**Interpretation**: Higher average reward scores and recall values indicate better performance of the LAAs.

**Validation**: Performed through extensive experiments in both decision-making and multi-step reasoning environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
