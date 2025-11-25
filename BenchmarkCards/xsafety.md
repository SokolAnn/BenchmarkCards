# XSAFETY

## 📊 Benchmark Details

**Name**: XSAFETY

**Overview**: The first multilingual safety benchmark for LLMs covering 14 commonly used safety issues across ten languages spanning several language families.

**Data Type**: Annotated instances

**Domains**:
- Safety Assessment
- Multilingual Evaluation

**Languages**:
- English
- Chinese
- Spanish
- French
- Bengali
- Arabic
- Hindi
- Russian
- Japanese
- German

**Similar Benchmarks**:
- Commonsense Safety
- Toxicity datasets
- Bias measurement datasets

**Resources**:
- [GitHub Repository](https://github.com/Jarviswang94/Multilingual_safety_benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multilingual safety performance of large language models (LLMs) and develop safety alignment strategies for non-English languages.

**Target Audience**:
- Researchers
- Developers
- Policymakers

**Tasks**:
- Safety evaluation
- Data collection
- Methodological development

**Limitations**: None

**Out of Scope Uses**:
- Uses outside of LLM safety evaluation

## 💾 Data

**Source**: Multiple safety benchmarks, translated and adapted for multilingual contexts

**Size**: 2,800 instances across 10 languages resulting in 28,000 annotated instances

**Format**: Text

**Annotation**: Manually annotated and translated by professional translators

## 🔬 Methodology

**Methods**:
- Safety evaluation through LLM responses
- Prompting method to improve safety alignment

**Metrics**:
- Unsafe response ratio
- Annotation accuracy

**Calculation**: Unsafe ratios calculated by evaluating LLM responses to translated prompts

**Interpretation**: Lower unsafe response ratios indicate better safety alignment

**Baseline Results**: N/A

**Validation**: Involves human annotation to verify automatic evaluation accuracy

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety alignment
- Cultural bias
- Model evaluation

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack

**Potential Harm**: Higher unsafe response ratios for non-English queries

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data licensed for research use

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
