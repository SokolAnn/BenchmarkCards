# PromptBench

## 📊 Benchmark Details

**Name**: PromptBench

**Overview**: A unified library to evaluate large language models (LLMs) that includes prompt construction, adversarial prompt attacks, dynamic evaluation protocols, and analysis tools.

**Data Type**: Various (text, datasets)

**Domains**:
- Natural Language Processing
- Multimodal Understanding
- Mathematical Reasoning

**Similar Benchmarks**:
- OpenAI Evals
- OpenCompass
- LM Evaluation Harness

**Resources**:
- [GitHub Repository](https://github.com/microsoft/promptbench)
- [Resource](https://promptbench.readthedocs.io/en/latest/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for evaluating LLMs and facilitating research in benchmark creation and prompt engineering.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Evaluation of LLM performance
- Benchmark creation
- Prompt engineering

**Limitations**: Not all evaluation scenarios covered, potential for metric insufficiencies.

## 💾 Data

**Source**: Various public datasets including GLUE, MMLU, SQuAD V2, and more.

**Size**: 22 public datasets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Prompt construction
- Adversarial attacks
- Dynamic evaluations

**Metrics**:
- Accuracy
- Performance metrics through benchmark results

**Calculation**: Results analyzed using dynamic evaluation protocols.

**Interpretation**: Benchmark results provide insights into LLM capabilities.

**Validation**: Through various evaluation protocols and datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Adversarial robustness
- Prompt engineering effectiveness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack, Extraction attack, Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
