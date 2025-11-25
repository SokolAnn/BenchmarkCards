# SimCopilot

## 📊 Benchmark Details

**Name**: SimCopilot

**Overview**: SimCopilot is a benchmark designed to evaluate the ability of large language models (LLMs) to perform code completion and infill tasks in a Copilot-style interactive environment. It comprises two sub-benchmarks for Java and Python, focusing on real-world coding scenarios.

**Data Type**: code completion and infilling tasks

**Domains**:
- Computer Science

**Languages**:
- Java
- Python

**Resources**:
- [GitHub Repository](https://github.com/mj33rice/Sim-CoPilot)
- [Resource](https://huggingface.co/datasets/mj33/SimCoPilot)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models as interactive coding assistants in realistic programming scenarios.

**Target Audience**:
- ML Researchers
- Software Developers

**Tasks**:
- Code Completion
- Code Infill

**Limitations**: May not accurately reflect user satisfaction with AI-generated code, as it strictly evaluates correctness based on predefined test cases.

## 💾 Data

**Source**: Collected from private Java and Python code repositories with contributions from faculty and students.

**Size**: 1,163 programming tasks

**Format**: JSON

**Annotation**: Human-annotated with a systematic two-stage pipeline to ensure task relevance and integrity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pass rate

**Calculation**: Models are tested on various programming tasks, with results calculated based on the percentage of tasks passing the defined test cases.

**Interpretation**: The results are interpreted as the fraction of correct codes produced by models based on success in passing test cases.

**Validation**: Evaluated against a suite of test cases encompassing diverse scenarios and programming constructs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-ND 4.0 for data; MIT License for code

**Consent Procedures**: Informed consent was obtained from contributors of private code repositories.

**Compliance With Regulations**: Not Applicable
