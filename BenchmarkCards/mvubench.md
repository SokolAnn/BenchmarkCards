# MVUBench

## 📊 Benchmark Details

**Name**: MVUBench

**Overview**: MVUBench is a dataset of model-view-update (MVU) web applications with accompanying unit tests, created to evaluate the effectiveness of contextualization methods in code completion systems using large language models.

**Data Type**: program code with unit tests

**Domains**:
- Software Engineering

**Languages**:
- Hazel
- TypeScript

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.12669479)
- [Resource](https://hazel.org)
- [GitHub Repository](https://github.com/hazelgrove/hazel/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating code completion systems in high-context programming tasks using large language models.

**Target Audience**:
- ML Researchers
- Software Engineers
- AI Researchers

**Tasks**:
- Code Completion
- Program Synthesis

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from scratch to avoid data contamination, featuring MVU applications.

**Size**: 5 applications with unit tests

**Format**: program sketches and unit test files

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Feature ablation study
- Static retrieval
- Error correction

**Metrics**:
- Accuracy

**Calculation**: Performance is evaluated through unit tests created for each MVU application.

**Interpretation**: Higher accuracy indicates better performance in code completion tasks as defined by test cases.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Contamination
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
