# ComplexCodeEval

## 📊 Benchmark Details

**Name**: ComplexCodeEval

**Overview**: ComplexCodeEval is a benchmark designed to evaluate the performance of large code models (LCMs) in various development scenarios, including code generation, code completion, API recommendation, and test case generation, by utilizing real-world samples from high-star GitHub repositories.

**Data Type**: function samples

**Domains**:
- Software Engineering
- Natural Language Processing

**Languages**:
- Java
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- CrossCodeEval
- CoderEval

**Resources**:
- [GitHub Repository](https://github.com/ComplexCodeEval/ComplexCodeEval)
- [Resource](https://doi.org/10.1145/3691620.3695552)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of large code models across multiple tasks and conditions reflective of complex software development scenarios, avoiding data leakage.

**Target Audience**:
- ML Researchers
- Software Developers
- Benchmark Developers

**Tasks**:
- Code Generation
- Code Completion
- API Recommendation
- Test Case Generation

**Limitations**: N/A

## 💾 Data

**Source**: 3,897 Java samples from 1,055 high-star GitHub repositories and 7,184 Python samples from 2,107 high-star repositories.

**Size**: 11,081 function samples

**Format**: JSON

**Annotation**: Includes annotations such as function signatures, docstrings, reference APIs, test cases, and multiple timestamps.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Contextual performance analysis

**Metrics**:
- CodeBLEU
- BLEU
- F1 Score
- Edit Similarity (ES)

**Calculation**: Metrics are calculated based on the similarity of generated outputs to reference implementations, using n-grams and structural comparisons.

**Interpretation**: Higher scores indicate better performance in generating, completing, and recommending code.

**Baseline Results**: N/A

**Validation**: Evaluated using different timestamps to assess the impact of data leakage and contextual information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
