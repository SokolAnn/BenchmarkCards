# LCTG Bench (LLM Controlled Text Generation Benchmark)

## 📊 Benchmark Details

**Name**: LCTG Bench (LLM Controlled Text Generation Benchmark)

**Overview**: LCTG Bench is the first Japanese benchmark for evaluating the controllability of large language models (LLMs). It provides a unified framework for assessing control performance across diverse tasks, focusing on summarization, ad text generation, and pros & cons generation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- FollowEval
- CELLO

**Resources**:
- [GitHub Repository](https://github.com/CyberAgentAILab/LCTG-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To assist developers in selecting appropriate models for various use cases in real-world scenarios concerning controllability.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Summarization
- Ad Text Generation
- Pros & Cons Generation

**Limitations**: N/A

## 💾 Data

**Source**: Based on publicly available datasets and data disclosed by the organization, including articles from media sites and predefined prompts.

**Size**: N/A

**Format**: N/A

**Annotation**: Crowdsourced collection of condition templates and manual text generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Quality of Generation
- Controllability Performance

**Calculation**: Metrics are calculated based on models' adherence to task-specific requirements regarding format, character counts, keywords, and prohibited words.

**Interpretation**: Higher scores indicate better controllability and quality of text generation.

**Baseline Results**: Evaluation results show performance gaps between Japanese and multilingual models like GPT-4.

**Validation**: Evaluation procedures included checking outputs for adherence to requirements through multiple trials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
