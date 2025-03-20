# LongHalQA

## 📊 Benchmark Details

**Name**: LongHalQA

**Overview**: LongHalQA is an LLM-free hallucination benchmark that comprises 6K long and complex hallucination text, featuring tasks such as hallucination discrimination and hallucination completion to evaluate multi-modal large language models (MLLMs).

**Data Type**: text

**Domains**:
- vision-language

**Languages**:
- N/A

**Similar Benchmarks**:
- POPE
- CIEM
- AMBER
- NOPE
- MME
- PhD
- Hal-Eval

**Resources**:
- [GitHub Repository](https://github.com/hanqiu-hq/LongHalQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the hallucination levels of multi-modal large language models (MLLMs) using long-context data.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- hallucination discrimination
- hallucination completion

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: GPT4V-generated data

**Size**: 6485 multiple-choice questions

**Format**: long-context text

**Annotation**: 12 types of hallucinations

## 🔬 Methodology

**Methods**:
- multiple-choice evaluation
- automated data generation

**Metrics**:
- accuracy
- precision
- yes ratio
- (mc-)accuracy

**Calculation**: Accuracy metrics for hallucination discrimination tasks and multiple-choice accuracy for completion tasks.

**Interpretation**: MLLMs' capabilities are assessed in identifying hallucinations in both image and text contexts.

**Baseline Results**: N/A

**Validation**: Extensive experiments over multiple recent MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
