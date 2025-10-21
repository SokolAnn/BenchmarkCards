# ConCodeEval

## 📊 Benchmark Details

**Name**: ConCodeEval

**Overview**: ConCodeEval is a first-of-its-kind benchmark evaluating large language models for handling code constraints in domain-specific languages across various schema formats.

**Data Type**: schema samples

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of large language models in generating and validating code adhering to schema constraints.

**Target Audience**:
- ML Researchers
- Software Engineers
- Domain Experts

**Tasks**:
- Code Generation
- Data Validation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation of schema samples across various formats.

**Size**: 602 schema samples

**Format**: JSON, YAML, XML, Python, Natural Language

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Macro-F1

**Calculation**: Metrics are calculated based on the compliance of generated code with the specified schema constraints.

**Interpretation**: Higher accuracy indicates better compliance with schema constraints in generated code.

**Baseline Results**: LLama3 and Granite models are used as baseline for comparison.

**Validation**: Evaluated through compliance checking against schema validator tools.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
