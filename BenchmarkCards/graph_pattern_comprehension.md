# GRAPH PATTERN COMPREHENSION

## 📊 Benchmark Details

**Name**: GRAPH PATTERN COMPREHENSION

**Overview**: This work introduces a comprehensive benchmark to assess LLMs' capabilities in graph pattern tasks. It evaluates whether LLMs can understand graph patterns based on either terminological or topological descriptions, and tests their capacity to autonomously discover graph patterns from data.

**Data Type**: synthetic and real datasets

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/DDigimon/GraphPattern)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate LLMs' understanding of graph patterns in synthetic and real-world applications.

**Target Audience**:
- Researchers in Natural Language Processing
- Graph Theory
- Artificial Intelligence

**Tasks**:
- Pattern Translation
- Graph Modification
- Pattern Detection
- Isomorphic Mapping
- Frequent Subgraph Extraction
- Discriminative Pattern Learning

**Limitations**: N/A

## 💾 Data

**Source**: Both synthetic datasets generated for various tasks and real-world datasets including molecular graphs, social networks, and biological networks.

**Size**: 1,893 undirected graphs and 1,313 directed graphs in total; diverse sizes for different tasks.

**Format**: Adjacency List (A.L.) and Edge List (E.L.)

**Annotation**: Graphs and patterns are generated based on predefined structures, with labeled graphs utilized in real-world datasets.

## 🔬 Methodology

**Methods**:
- Evaluation on various LLMs through tasks structured to assess graph pattern comprehension.

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the correct identification of graph patterns, comparison of generated patterns with expected patterns.

**Interpretation**: Higher scores indicate better understanding and generation of graph patterns by LLMs.

**Baseline Results**: Reported results across various models indicate performance varying significantly across tasks and patterns.

**Validation**: Results are validated through comparative analysis with known benchmarks in graph theory.

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

**Potential Harm**: ['Potential bias in understanding graph patterns based on underlying data used for training.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
