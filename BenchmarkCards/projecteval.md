# ProjectEval

## 📊 Benchmark Details

**Name**: ProjectEval

**Overview**: ProjectEval is a new benchmark for LLM agents project-level code generation's automated evaluation by simulating user interaction. It features automated evaluation tests, diverse input levels, and aims to enhance explainability and usability from a user perspective.

**Data Type**: test cases for code generation projects

**Domains**:
- Natural Language Processing

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- SoftwareDev
- ProjectDev

**Resources**:
- [GitHub Repository](https://github.com/RyanLoil/ProjectEval/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the programming ability of LLM agents in generating project-level code through user interaction simulation.

**Target Audience**:
- ML Researchers
- Software Engineers
- AI Developers

**Tasks**:
- Code Generation
- Automated Testing

**Limitations**: Some projects may not align with Django design patterns; currently only supports Python.

## 💾 Data

**Source**: Constructed using LLM with human reviewing and editing.

**Size**: 20 tasks with a total of 284 test cases

**Format**: JSON

**Annotation**: Manual and semi-automated with revisions from human reviewers.

## 🔬 Methodology

**Methods**:
- User interaction simulation
- Automated metrics
- Human reviewing

**Metrics**:
- Pass@K
- CodeBLEU

**Calculation**: Metrics calculated based on pass rates and similarity evaluations.

**Interpretation**: Higher scores indicate better capability of LLM agents in generating functional code.

**Baseline Results**: Results from existing benchmarks like DevBench for comparative analysis.

**Validation**: Benchmark validated against existing benchmarks to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential introduction of harmful code during automated evaluations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
