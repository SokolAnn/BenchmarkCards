# PlanBench

## 📊 Benchmark Details

**Name**: PlanBench

**Overview**: A benchmark suite for evaluating language models on various planning and scheduling tasks, featuring established benchmarks and extending them for more complex planning problems.

**Data Type**: task-specific problem instances

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- ALFworld
- BEHAVIOR
- kitchen environments

**Resources**:
- [Resource](https://arxiv.org/abs/2410.02162)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the planning and scheduling capabilities of language models, specifically the new Large Reasoning Models (LRM).

**Target Audience**:
- AI Researchers
- Model Developers

**Tasks**:
- Planning
- Scheduling

**Limitations**: N/A

## 💾 Data

**Source**: Static test sets from IPC planning problems (e.g., Blocksworld, Logistics, Sokoban)

**Size**: 600 planning instances

**Format**: PDDL

**Annotation**: Automatically generated problem representations with conditions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the proportion of correctly solved instances on the defined benchmarks.

**Interpretation**: Higher accuracy indicates better reasoning capability of the language models on planning tasks.

**Baseline Results**: Need for further refinement; specific models and their results vary across benchmarks.

**Validation**: Compared against classical planning methods and previous state-of-the-art results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
