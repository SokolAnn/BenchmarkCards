# WACK

## 📊 Benchmark Details

**Name**: WACK

**Overview**: WACK is a framework for assessing white-box hallucination mitigation techniques in open-book and closed-book contexts for large language models (LLMs). It categorizes examples based on the model’s prior knowledge and creates model-specific hallucination datasets (including HK+ and HK-), enabling effective intervention strategies and further analysis of different hallucination types.

**Data Type**: N/A

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/technion-cs-nlp/hallucination-mitigation)
  - This repository includes two works:
    1. Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs
    2. Distinguishing Ignorance from Error in LLM Hallucinations (with model-specific hallucination datasets HK+ and HK-)

## 🎯 Purpose and Intended Users

**Goal**: To improve the reliability of large language models (LLMs) by mitigating hallucinations through effective intervention strategies and distinguishing ignorance from error.

**Target Audience**:
- Researchers in AI and Natural Language Processing
- Developers of language model technologies

**Tasks**:
- Benchmarking intervention strategies for LLMs
- Investigating hallucination mitigation techniques
- Creating and analyzing model-specific hallucination datasets for various models

**Limitations**: None

**Out of Scope Uses**:
- Any use of the data for malicious purposes such as increasing hallucinations

## 💾 Data

**Source**: Automated dataset generation based on model knowledge types from selected examples in DisentQA and TriviaQA datasets.  
Includes model-specific hallucination datasets (HK+, HK-) for analysis.

**Size**: Approximately 4,000 examples for each of the datasets created.

**Format**: JSON

**Annotation**: Labeled for hallucination (errors) and grounded (correct) outputs, with additional annotation for hallucination type (HK+, HK-).

## 🔬 Methodology

**Methods**:
- Dataset construction through automated classification of model knowledge
- Intervention via modification of model activations
- Creation of model-specific hallucination datasets
- Framework for constructing similar datasets for other models

**Metrics**:
- Classification accuracy
- Generation accuracy
- Perplexity

**Calculation**: Metrics are calculated by comparing model outputs against labeled datasets for hallucination and grounded responses.

**Interpretation**: Higher accuracy indicates better performance for mitigating hallucinations without compromising the model's overall capabilities.

**Validation**: Experimental validation through multiple model settings and evaluation on both open and closed-book settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Interventions and evaluations must be conducted carefully to avoid exacerbating hallucinations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets were created for research purposes and are publicly available without explicit licensing restrictions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The benchmarks were designed to comply with general ethical standards in AI research.
