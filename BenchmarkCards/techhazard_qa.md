# TECHHAZARD QA

## 📊 Benchmark Details

**Name**: TECHHAZARD QA

**Overview**: TECHHAZARD QA is a benchmark dataset containing complex queries designed to elicit responses in both text and instruction-centric formats to evaluate the potential for generating harmful or unethical content by LLMs.

**Data Type**: text and pseudocode

**Domains**:
- Computer Security
- Biotechnology
- Biological Science
- Nuclear Technology
- Finance
- Social Media
- Public Health

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench
- NicheHazard QA

**Resources**:
- [GitHub Repository](https://github.com/NeuralSentinel/TechHazardQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess how LLMs respond to instruction-centric prompts and to evaluate the risks associated with generating unethical content.

**Target Audience**:
- ML Researchers
- Ethicists
- AI Developers
- Policy Makers

**Tasks**:
- Text Generation
- Code Generation
- Ethics Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset of complex queries crafted to expose vulnerabilities in large language models.

**Size**: 7,745 examples

**Format**: N/A

**Annotation**: Manually curated and moderated for harmful content

## 🔬 Methodology

**Methods**:
- GPT-4 assessment
- Human evaluation
- Quantitative analysis of harmful responses

**Metrics**:
- Harmfulness score

**Calculation**: Evaluation against responses categorized as harmful or non-harmful based on GPT-4 and human assessments.

**Interpretation**: A higher harmfulness score indicates a greater likelihood of unethical output generation.

**Validation**: Tested on multiple LLMs including Llama-2 and Mistral models across various settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Increased risk of generating harmful or unethical outputs via instruction-centric prompts.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
