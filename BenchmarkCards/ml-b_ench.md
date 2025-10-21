# ML-B ENCH

## 📊 Benchmark Details

**Name**: ML-B ENCH

**Overview**: ML-B ENCH is a benchmark that evaluates Large Language Models (LLMs) and AI agents on repository-level code understanding and executable code generation tasks using real-world programming applications drawn from existing code repositories.

**Data Type**: annotated coding examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- APPS

**Resources**:
- [GitHub Repository](https://github.com/gersteinlab/ML-bench)
- [Resource](https://hf.co/datasets/super-dainiu/ml-bench)
- [Resource](https://ml-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs and AI agents on their ability to understand and generate code within the context of repository-level tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Software Engineers

**Tasks**:
- Text-to-Code Generation
- Executable Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: 18 GitHub repositories containing diverse programming tasks and examples.

**Size**: 9,641 examples

**Format**: N/A

**Annotation**: Annotated by computer science graduate students with proficiency in programming.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pass@5

**Calculation**: Pass@5 measures the likelihood of the model producing at least one correct code execution in five attempts.

**Interpretation**: Higher Pass@5 scores indicate better model performance in generating executable code.

**Baseline Results**: GPT-4o achieved a Pass@5 rate over 50%.

**Validation**: Evaluated using annotated examples across various tasks from 18 GitHub repositories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
