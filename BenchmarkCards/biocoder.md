# BioCoder

## 📊 Benchmark Details

**Name**: BioCoder

**Overview**: BioCoder is a benchmark developed to evaluate LLMs in generating bioinformatics-specific code, covering a variety of coding problems in bioinformatics such as class declarations, global variables, and cross-file dependencies.

**Data Type**: Python functions and Java methods

**Domains**:
- Bioinformatics

**Languages**:
- English

**Similar Benchmarks**:
- Prior coding benchmarks like HumanEval, MBPP, and DS1000

**Resources**:
- [GitHub Repository](https://github.com/gersteinlab/biocoder)
- [Resource](https://biocoder-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in generating code specific to bioinformatics tasks.

**Target Audience**:
- ML Researchers
- Bioinformaticians
- Model Developers

**Tasks**:
- Code Generation
- Function Completion

**Limitations**: N/A

## 💾 Data

**Source**: 1,720 bioinformatics repositories processed to curate biocoding tasks and functions.

**Size**: 2,269 coding problems (1,026 Python functions and 1,243 Java methods)

**Format**: N/A

**Annotation**: Manual filtering and parsing from GitHub repositories with bioinformatics context.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Pass@K - measuring functional accuracy of generated code.

**Calculation**: The Pass@K metric quantifies the likelihood of the model solving a programming problem when generating K candidate solutions. A problem is considered solved if at least one generated solution passes all test cases.

**Interpretation**: A higher Pass@K score indicates better functional accuracy and a greater likelihood of the model generating correct code.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
