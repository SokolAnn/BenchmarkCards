# Latent Jailbreak Benchmark

## 📊 Benchmark Details

**Name**: Latent Jailbreak Benchmark

**Overview**: A benchmark for evaluating the text safety and output robustness of large language models (LLMs), focusing on both safety and robustness in the context of latent jailbreak prompts.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- AI Safety

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- Jailbreak Detection Benchmarks

**Resources**:
- [GitHub Repository](https://github.com/qiuhuachuan/latent-jailbreak)

## 🎯 Purpose and Intended Users

**Goal**: To assess and evaluate the safety and robustness of large language models against latent jailbreak prompts.

**Target Audience**:
- Researchers
- AI Developers
- Safety Engineers

**Tasks**:
- Evaluate LLM responses to latent jailbreak prompts
- Analyze text safety and output robustness

**Limitations**: None

**Out of Scope Uses**:
- Non-malicious task evaluation
- General-purpose language model evaluations

## 💾 Data

**Source**: Generated latent jailbreak prompt dataset

**Size**: 416 prompts

**Format**: Text

**Annotation**: Hierarchical annotation framework for evaluating text safety and output robustness

## 🔬 Methodology

**Methods**:
- Latent Jailbreak Prompt Generation
- Safety and Robustness Evaluation Framework
- Automated Labeling with RoBERTa

**Metrics**:
- Jailbreak Success Rate
- Trustworthiness Metric

**Calculation**: Jailbreak Success Rate = (Number of Unsafe Outputs) / (Total Outputs)

**Interpretation**: Higher success rates indicate lower robustness and safety.

**Validation**: Human validation of outputs alongside automated labeling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in prompt
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Vulnerability of outputs across different protected groups.

**Potential Harm**: Potential generation of harmful or toxic content through jailbreak prompts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes implicit malicious instructions, requiring strict ethical considerations regarding privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
