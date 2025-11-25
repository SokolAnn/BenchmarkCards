# SR-Eval: Evaluating LLMs on Code Generation under Stepwise Requirement Refinement

## 📊 Benchmark Details

**Name**: SR-Eval: Evaluating LLMs on Code Generation under Stepwise Requirement Refinement

**Overview**: SR-Eval is a benchmark specifically designed to assess LLMs on iterative code generation under stepwise requirement refinement, encompassing both function-level and repository-level tasks in Python and Java.

**Data Type**: multi-turn programming tasks

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
- [Resource](https://doi.org/XXXXXXX.XXXXXXX)
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs for iterative code generation under progressive requirement refinement.

**Target Audience**:
- Research Community
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation
- Multi-Turn Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Seed datasets from BigCodeBench-Hard, AutoCodeBench, DevEval, and MRGBench.

**Size**: 443 tasks

**Format**: JSON

**Annotation**: Semi-automated with human verification

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Semantic-aware test case generation

**Metrics**:
- Per-turn Accuracy
- Average Accuracy
- Complete Task Rate

**Calculation**: Metrics are computed based on the success rate at each turn and overall completion of tasks.

**Interpretation**: Higher accuracy and completion rates indicate better model performance.

**Baseline Results**: N/A

**Validation**: Validation procedures include correctness validation, distinctiveness validation, and semantic alignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
