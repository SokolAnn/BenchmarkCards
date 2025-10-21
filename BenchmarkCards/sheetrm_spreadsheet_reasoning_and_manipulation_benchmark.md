# SheetRM (Spreadsheet Reasoning and Manipulation Benchmark)

## 📊 Benchmark Details

**Name**: SheetRM (Spreadsheet Reasoning and Manipulation Benchmark)

**Overview**: SheetRM is a benchmark for developing and evaluating LLM-based agents for precise spreadsheet manipulation and advanced reasoning capabilities, featuring long-horizon and multi-category tasks with reasoning-dependent manipulation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SheetCopilot

**Resources**:
- [Resource](https://anonymous.4open.science/r/SheetAgent)

## 🎯 Purpose and Intended Users

**Goal**: To develop and evaluate LLM-based agents for competent spreadsheet manipulation and reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Spreadsheet Manipulation
- Reasoning Over Tables

**Limitations**: N/A

## 💾 Data

**Source**: Real-life Excel exam datasets collected and curated from a public examination question bank.

**Size**: 317 tasks with 1625 subtasks

**Format**: N/A

**Annotation**: Tasks are generated with both human and GPT-4 annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Exec@1
- Pass@1
- SubPass@1
- Accuracy

**Calculation**: Metrics are calculated based on the successful execution of tasks and subtasks as per defined evaluation criteria.

**Interpretation**: Higher scores indicate better performance in task completion and reasoning capabilities, as shown in experimental results.

**Baseline Results**: Compared against SheetCopilot and other existing benchmarks.

**Validation**: The benchmark has been validated through extensive testing of agents on various spreadsheet manipulation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
