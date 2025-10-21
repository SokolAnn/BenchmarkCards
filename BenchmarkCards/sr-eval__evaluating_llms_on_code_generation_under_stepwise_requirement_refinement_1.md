# SR-Eval: Evaluating LLMs on Code Generation under Stepwise Requirement Refinement

## 📊 Benchmark Details

**Name**: SR-Eval: Evaluating LLMs on Code Generation under Stepwise Requirement Refinement

**Overview**: SR-Eval is a benchmark specifically designed to evaluate LLMs on iterative code generation under stepwise requirement refinement, covering function-level and repository-level tasks in Python and Java.

**Data Type**: programming tasks with multi-turn interactions

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java

**Similar Benchmarks**:
- HumanEval
- MBPP
- LiveCodeBench
- DevEval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs for iterative code generation under progressive requirement refinement.

**Target Audience**:
- ML Researchers
- Software Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from existing single-turn code generation datasets like BigCodeBench and DevEval.

**Size**: 443 multi-turn tasks across Python and Java

**Format**: N/A

**Annotation**: Multi-agent approach for requirement and test case generation.

## 🔬 Methodology

**Methods**:
- Multi-agent based evaluation
- Semantic-aware discriminative test case generation

**Metrics**:
- Accuracy
- Completion Rate

**Calculation**: Performance measured based on task success in iterative scenarios.

**Interpretation**: Higher accuracy and completion rates indicate better model performance in handling iterative developments.

**Baseline Results**: Evaluated across 11 LLMs with varying performances.

**Validation**: Rigorous pipeline for evaluating multi-turn interaction quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
