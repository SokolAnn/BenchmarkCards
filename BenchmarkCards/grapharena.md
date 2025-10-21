# GraphArena

## 📊 Benchmark Details

**Name**: GraphArena

**Overview**: GraphArena is a benchmarking tool designed to evaluate large language models on real-world graph computational problems, featuring a suite of four polynomial-time tasks and six NP-complete challenges, with a rigorous evaluation framework.

**Data Type**: graph problems

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- NLGraph
- GraphQA
- MAGMA

**Resources**:
- [GitHub Repository](https://github.com/squareRoot3/GraphArena)

## 🎯 Purpose and Intended Users

**Goal**: To assess the reasoning capabilities of large language models on graph computational problems.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Graph Computation
- Algorithmic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Real-world graphs including academic collaboration networks, social networks, knowledge graphs, airport networks, and molecular graphs.

**Size**: 10,000 graph problems

**Format**: N/A

**Annotation**: Tasks are generated and evaluated using ground-truth algorithms.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Path-based evaluation

**Metrics**:
- Accuracy
- Feasibility
- Hallucination

**Calculation**: Metrics are calculated based on response correctness, feasibility of proposed solutions, and hallucination rates based on output categorization.

**Interpretation**: Higher accuracy and feasibility indicate better model performance, while lower hallucination rates suggest more reliable outputs.

**Baseline Results**: Comparative analysis was done against various LLMs and traditional algorithms.

**Validation**: Evaluation is conducted across small and large graphs of varying complexity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Various sources have appropriate licenses (CC0, CC BY, DBCL v1.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
