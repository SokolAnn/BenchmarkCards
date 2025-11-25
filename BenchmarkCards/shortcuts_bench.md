# SHORTCUTS BENCH

## 📊 Benchmark Details

**Name**: SHORTCUTS BENCH

**Overview**: SHORTCUTS BENCH is a large-scale benchmark for the comprehensive evaluation of API-based agents in solving real-world complex tasks, featuring real APIs, user queries, human-annotated action sequences, and detailed parameter filling.

**Data Type**: user queries and action sequences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- API-Bank
- ToolLLM

**Resources**:
- [GitHub Repository](https://github.com/EachSheep/ShortcutsBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive set of tasks to evaluate API-based agents and their ability to handle complex queries efficiently.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- API Selection
- Parameter Filling
- Requesting User Input

**Limitations**: N/A

## 💾 Data

**Source**: Data is extracted from existing Digital Automation Platforms (DAPs) and includes real APIs and user-generated shortcuts from Apple Shortcuts.

**Size**: 7627 queries and 1414 APIs

**Format**: JSON

**Annotation**: Human-annotated action sequences

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- API Selection Accuracy
- Parameter Fill Rate
- Recognition of Need for Input

**Calculation**: Metrics are calculated based on the number of correct actions predicted by the API-based agents.

**Interpretation**: Higher accuracy indicates better performance of agents in handling API calls, filling parameters, and recognizing when input is needed.

**Baseline Results**: Evaluated against 10 advanced LLM-based agents, results show significant limitations in existing API-based agents in fulfilling complex queries.

**Validation**: Exhaustive evaluation across various intelligence levels of LLMs on all task types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
