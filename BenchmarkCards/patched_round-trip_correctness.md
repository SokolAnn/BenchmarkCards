# Patched Round-Trip Correctness

## 📊 Benchmark Details

**Name**: Patched Round-Trip Correctness

**Overview**: This paper introduces Patched Round-Trip Correctness (Patched RTC), a novel evaluation technique for Large Language Models (LLMs) applied to diverse software development tasks, particularly focusing on outer loop activities such as bug fixing, code review, and documentation updates.

**Data Type**: text

**Domains**:
- Software Development

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/codelion/optillm)
- [Resource](https://patchwork.patched.codes/evaluate/v1)
- [Resource](https://patchwork.patched.codes/v1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a self-evaluating framework for measuring consistency and robustness of LLM responses in software development tasks.

**Target Audience**:
- ML Researchers
- Software Developers
- Industry Practitioners

**Tasks**:
- Bug Fixing
- Code Review
- Documentation Updates

**Limitations**: N/A

## 💾 Data

**Source**: Open-source implementation available for various software development tasks.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Patched RTC score

**Calculation**: Comparison of generated responses using similarity scores to determine correctness.

**Interpretation**: A similarity score above a threshold indicates that the model's response is considered correct.

**Baseline Results**: N/A

**Validation**: Evaluation compares performance against established benchmarks like Arena-Hard-Auto.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
