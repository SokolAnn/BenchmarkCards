# SIMCODE

## 📊 Benchmark Details

**Name**: SIMCODE

**Overview**: SIMCODE is introduced as the first benchmark to evaluate LLMs’ ability to generate executable ns-3 simulation code from natural language. It includes 400 tasks across introductory, intermediate, and advanced levels, each with a prompt, verified C++ solution, and test cases.

**Data Type**: triplet of natural language prompt, C++ solution, and test cases

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- MojoBench
- mHumanEval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to generate correct and executable ns-3 simulation code from natural language prompts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated simulation tasks from various sources, including university-level networking coursework and the official ns-3 example repository.

**Size**: 400 tasks

**Format**: N/A

**Annotation**: Each solution was verified to run correctly in the ns-3 environment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Execution Accuracy
- CodeBLEU
- CodeBERTScore
- Pass@1

**Calculation**: Execution accuracy measures the proportion of generated code samples that successfully compile and execute. CodeBLEU and CodeBERTScore assess syntactic structure and semantic correctness.

**Interpretation**: Higher execution accuracy indicates better capability of the LLM in generating correct code.

**Baseline Results**: GPT-4.1 achieved up to 30.6% execution accuracy.

**Validation**: Evaluation of models was conducted across six prompt techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
