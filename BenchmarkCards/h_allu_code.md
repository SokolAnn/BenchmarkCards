# H ALLU CODE

## 📊 Benchmark Details

**Name**: H ALLU CODE

**Overview**: H ALLU CODE is a benchmark for evaluating the performance of code LLMs in recognizing hallucinations in generated code, comprising 5,663 Python code generation tasks, reference solutions, and their corresponding hallucinated counterparts.

**Data Type**: code snippets

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- DS-1000

**Resources**:
- [GitHub Repository](https://github.com/sahil280114/codealpaca)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of code LLMs in recognizing hallucinations and develop effective techniques for their detection and mitigation.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Code Generation
- Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: Generated from the Code Alpaca dataset, which contains instruction-following data for code generation.

**Size**: 5,663 code generation tasks

**Format**: JSON

**Annotation**: Manually analyzed by annotators with programming experience to identify hallucinations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy of Hallucination Existence Recognition
- Accuracy of Hallucination Type Recognition
- Accuracy of Hallucination Mitigation

**Calculation**: Metrics calculated based on the percentage of correctly identified hallucinations and their types in the generated code.

**Interpretation**: Higher rates indicate better performance in recognizing and mitigating hallucinations.

**Baseline Results**: ChatGPT achieved a hallucination recognition accuracy of over 89%.

**Validation**: Validated through experiments with various state-of-the-art code LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Functional errors in generated code due to hallucinations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
