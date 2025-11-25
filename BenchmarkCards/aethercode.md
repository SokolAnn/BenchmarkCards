# AetherCode

## 📊 Benchmark Details

**Name**: AetherCode

**Overview**: AetherCode is a new benchmark that draws problems from premier programming competitions such as IOI and ICPC, offering broader coverage and higher difficulty. It incorporates comprehensive, expert-validated test suites built through a hybrid of automated generation and human curation.

**Data Type**: problem statements with test cases

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- CodeContests
- LiveCodeBench
- CodeELO

**Resources**:
- [Resource](https://huggingface.co/datasets/m-a-p/AetherCode)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more faithful measure of LLM capabilities and set a new standard for future research in code reasoning.

**Target Audience**:
- ML Researchers
- Competitive Programming Practitioners

**Tasks**:
- Code Generation
- Algorithmic Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Problems sourced from premier programming competitions worldwide, including the Olympiad in Informatics (OI) and the International Collegiate Programming Contest (ICPC).

**Size**: 456 problems

**Format**: Markdown+LaTeX

**Annotation**: Problems annotated by a team of competitive programming experts.

## 🔬 Methodology

**Methods**:
- Automated test case generation
- Expert curation

**Metrics**:
- True Positive Rate (TPR)
- True Negative Rate (TNR)

**Calculation**: The TPR and TNR are calculated by validating test cases against a large corpus of collected solutions.

**Interpretation**: A high TPR and TNR indicates that the benchmark's test cases effectively discriminate between correct and incorrect solutions.

**Baseline Results**: N/A

**Validation**: Validated against a dataset of over 30,000 human submissions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
