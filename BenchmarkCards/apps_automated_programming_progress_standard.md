# APPS (Automated Programming Progress Standard)

## 📊 Benchmark Details

**Name**: APPS (Automated Programming Progress Standard)

**Overview**: APPS is a benchmark for code generation, measuring the ability of models to take an arbitrary natural language specification and generate satisfactory Python code. It evaluates models not only on syntactical correctness but also on their understanding of task descriptions and ability to devise algorithms.

**Data Type**: programming problems and test cases

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- CodeXGLUE

**Resources**:
- [GitHub Repository](https://github.com/hendrycks/apps)

## 🎯 Purpose and Intended Users

**Goal**: To track the progress of code generation models on the task of generating arbitrary Python code from complex natural language specifications.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various open-access coding challenge websites including Codeforces, Kattis, and others.

**Size**: 10,000 problems and 131,777 test cases

**Format**: JSON

**Annotation**: Manually curated and cleaned with automated quality checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Test case evaluation

**Metrics**:
- Test Case Average
- Strict Accuracy

**Calculation**: The average fraction of test cases passed and strict accuracy calculated by determining if the generated code passes all provided test cases.

**Interpretation**: Higher test case averages indicate better model performance in code generation.

**Validation**: Validated through extensive testing against numerous ground-truth solutions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured by removing identifying information from participant-provided solutions.

**Data Licensing**: The APPS dataset is licensed under CC BY-SA 3.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Compliant with GDPR and Fair Use guidelines.
