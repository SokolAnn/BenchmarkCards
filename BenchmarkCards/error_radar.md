# ERROR RADAR

## 📊 Benchmark Details

**Name**: ERROR RADAR

**Overview**: ERROR RADAR is the first benchmark designed to assess Multimodal Large Language Models' capabilities in multimodal error detection tasks, focusing on error step identification and error categorization within complex mathematical reasoning scenarios.

**Data Type**: multimodal mathematical problems

**Domains**:
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- MathVista

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the complex mathematical reasoning capabilities of Multimodal Large Language Models in error detection settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Error Step Identification
- Error Categorization

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is sourced from a global educational organization's question bank, specifically designed for K-12 mathematics.

**Size**: 2,500 multimodal questions

**Format**: N/A

**Annotation**: Manual annotation by educational experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Model performance is evaluated based on accuracy metrics for both identifying the first erroneous step and categorizing the error.

**Interpretation**: Accuracy indicates the model's ability to correctly identify error steps and categorize them based on predefined error types.

**Baseline Results**: Human evaluation accuracy is significantly higher than MLLMs, with 69.8% for step identification and 60.7% for categorization.

**Validation**: Extensive experiments were conducted to benchmark MLLMs against educational expert evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
