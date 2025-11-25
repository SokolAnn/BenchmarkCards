# CP-Bench

## 📊 Benchmark Details

**Name**: CP-Bench

**Overview**: CP-Bench is a novel benchmark that includes a diverse set of well-known combinatorial problems sourced from the CP community, structured explicitly for evaluating LLM-driven constraint modelling.

**Data Type**: combinatorial problem descriptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NL4Opt
- Logic Grid Puzzles

**Resources**:
- [Resource](https://huggingface.co/datasets/kostis-init/CP-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLMs in generating constraint models based on natural language descriptions of combinatorial problems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Constraint Modelling

**Limitations**: N/A

## 💾 Data

**Source**: Diverse combinatorial problem descriptions gathered from distinct sources within the CP community.

**Size**: 101 problems

**Format**: Python files

**Annotation**: Automatically generated runnable CP models

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Solution accuracy

**Calculation**: The solution accuracy measures the correctness of the solution obtained by executing the generated code.

**Interpretation**: A generated solution is considered accurate if it satisfies the constraints of the ground-truth model.

**Baseline Results**: Results show higher performance models achieving up to 70% accuracy across diverse combinatorial problems.

**Validation**: Systematic evaluation of state-of-the-art LLMs using the CP-Bench dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
