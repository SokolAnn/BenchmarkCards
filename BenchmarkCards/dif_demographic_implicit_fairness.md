# DIF (Demographic Implicit Fairness)

## 📊 Benchmark Details

**Name**: DIF (Demographic Implicit Fairness)

**Overview**: DIF is a framework developed for benchmarking and verifying implicit bias in Large Language Models (LLMs) by evaluating their performance on math problems across varied sociodemographic personas.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BBQ (Bias Benchmark for QA)

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a method for calculating and benchmarking implicit bias in LLMs using sociodemographic personas on preexisting datasets.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Bias Evaluation

**Limitations**: The study is limited to specific representative LLMs and uses a narrow subset of implicit bias.

## 💾 Data

**Source**: GSM-MC math problems dataset

**Size**: 1,000 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Statistical validation
- Mean Absolute Percentage Deviation (MAPD)

**Metrics**:
- Implicit bias score
- Accuracy

**Calculation**: Bias is calculated using the MAPD between demographic persona accuracies and baseline persona accuracy.

**Interpretation**: Higher DIF scores indicate less implicit bias with a scale from 0 (most biased) to 100 (least biased).

**Baseline Results**: Evaluation across major LLMs including Meta-Llama-3, Mistral, and Phi.

**Validation**: Statistical significance testing (e.g., t-tests) to validate observed biases across models and personas.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark integrates analysis across 22 sociodemographic groups considered protected in the U.S.

**Potential Harm**: Potential for reinforcing stereotypes and generating biased outputs in LLM interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
