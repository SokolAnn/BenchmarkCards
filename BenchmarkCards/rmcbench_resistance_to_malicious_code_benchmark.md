# RMCBench (Resistance to Malicious Code Benchmark)

## 📊 Benchmark Details

**Name**: RMCBench (Resistance to Malicious Code Benchmark)

**Overview**: RMCBench is the first benchmark specifically developed to evaluate the ability of large language models (LLMs) to resist malicious code generation. It comprises 473 prompts designed for two scenarios: a text-to-code scenario where LLMs generate code based on descriptions, and a code-to-code scenario where LLMs complete or translate existing malicious code.

**Data Type**: prompts for text-to-code and code-to-code scenarios

**Domains**:
- Computer Security

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/qing-yuan233/RMCBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs' ability to resist the generation of malicious code.

**Target Audience**:
- Researchers in A.I. Safety
- Developers of Large Language Models
- Cybersecurity Professionals

**Tasks**:
- Text-to-Code Generation
- Code Completion
- Code Translation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed prompts based on examples of malicious code and descriptions of their functionality from GitHub repositories.

**Size**: 473 prompts

**Format**: text

**Annotation**: Manually constructed and reviewed based on guidelines for malicious aspect recognition.

## 🔬 Methodology

**Methods**:
- Empirical Analysis
- Automated Labeling via ChatGPT-4

**Metrics**:
- Refusal Rate

**Calculation**: Refusal rate is calculated as the percentage of responses classified as non-malicious (GOOD) over all responses.

**Interpretation**: Higher refusal rates indicate better abilities of LLMs to resist generating malicious content.

**Baseline Results**: N/A

**Validation**: Responses were manually reviewed for classification accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Malicious Code Generation

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for generating malicious code']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
