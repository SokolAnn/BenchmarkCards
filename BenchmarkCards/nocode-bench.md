# NoCode-bench

## 📊 Benchmark Details

**Name**: NoCode-bench

**Overview**: NoCode-bench is a benchmark designed to evaluate LLMs on real-world NL-driven feature addition tasks. It consists of 634 tasks across 10 projects involving about 114k code changes in total, each of which pairs a user-facing documentation change and the corresponding code implementation that can be validated against developer-written test cases.

**Data Type**: feature addition tasks

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- SWE-bench

**Resources**:
- [GitHub Repository](https://github.com/NoCode-bench/NoCode-bench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capabilities of LLMs in no-code feature addition, simulating real-world development scenarios.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Feature Addition

**Limitations**: N/A

## 💾 Data

**Source**: Collected from developer-maintained release notes of high-quality open-source projects on GitHub.

**Size**: 634 tasks

**Format**: N/A

**Annotation**: Manually validated by experts to ensure clarity and evaluation accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate
- Patch Application Rate
- File Matched Rate
- Regression Tests Pass Rate
- Feature Validation

**Calculation**: Metrics calculated based on task success comparison against ground truth patches and test outcomes.

**Interpretation**: Higher success rates indicate better model performance in generating correct feature additions.

**Baseline Results**: The best performing model achieved a success rate of 28.07% on the verified subset.

**Validation**: Manual verification of task quality and evaluating clarity and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
