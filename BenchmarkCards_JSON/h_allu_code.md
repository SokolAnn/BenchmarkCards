# H ALLU CODE

## 📊 Benchmark Details

**Name**: H ALLU CODE

**Overview**: A benchmark for evaluating the performance of code LLMs in recognizing hallucinations, established based on a comprehensive analysis of hallucination types in generated code.

**Data Type**: Python

**Domains**:
- code generation

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- DS-1000
- MBPP
- APPS

**Resources**:
- [Resource](Code Alpaca dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the recognition and mitigation of hallucinations in code LLMs.

**Target Audience**:
- AI researchers
- Software developers
- Undergraduate and Graduate students in computer science

**Tasks**:
- Evaluate hallucinations in generated code
- Mitigate identified hallucinations

**Limitations**: Focus exclusively on Python code generation tasks.

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: H ALLU CODE

**Size**: 5,663 Python code generation tasks

**Format**: Python code

**Annotation**: Annotated with types of hallucinations present.

## 🔬 Methodology

**Methods**:
- Thematic analysis
- Statistical analysis

**Metrics**:
- Hallucination recognition accuracy
- Mitigation accuracy

**Calculation**: Metrics calculated based on the proportion of correctly identified hallucinations and successful mitigations among generated codes.

**Interpretation**: Recognized hallucinations and effectiveness of mitigation demonstrated through comparative analysis with HumanEval.

**Validation**: Cross-validated with multiple annotators for labeling of hallucination types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Transparency

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Privacy**: Personal information in data
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Generated code does not contain personally identifiable information.

**Data Licensing**: Data used from existing benchmarks is compliant with associated licenses.

**Consent Procedures**: Data sources are publicly available and do not require consent-related issues.

**Compliance With Regulations**: All data used complies with data protection and copyright regulations.
