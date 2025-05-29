# advCoU

## 📊 Benchmark Details

**Name**: advCoU - Open-source LLM Trustworthiness Assessment

**Overview**: This work conducts a comprehensive assessment of open-source LLMs across eight aspects of trustworthiness including toxicity, stereotypes, ethics, hallucination, fairness, sycophancy, privacy, and robustness against adversarial demonstrations using an adversarial prompting strategy called advCoU.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Adversarial Attacks

**Languages**:
- English

**Similar Benchmarks**:
- DecodingTrust

**Resources**:
- [GitHub Repository](https://github.com/OSU-NLP-Group/Eval-LLM-Trust)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the trustworthiness of open-source LLMs using adversarial assessments.

**Target Audience**:
- Researchers
- Developers
- Policy makers

**Tasks**:
- Assess LLMs across various trustworthiness aspects
- Develop safer LLMs

**Limitations**: The evaluation is limited to English language models, focuses on adversarial assessment, and may not cover all possible threats to trustworthiness. See the original paper for details.

**Out of Scope Uses**:
- General NLP tasks
- Non-adversarial assessments

## 💾 Data

**Source**: Adversarial prompts designed for each aspect of trustworthiness

**Size**: 1.2K toxic prompts, 1,152 stereotypical statements, 1,816 ethical scenarios, 1K multiple-choice questions for hallucination, 100 samples for fairness, 2.5k incorrect addition statements for sycophancy, 1,800 samples for privacy, and 800 counterfactual examples for robustness

**Format**: Various datasets

**Annotation**: Used existing datasets for experiments and evaluation

## 🔬 Methodology

**Methods**:
- Chain of Utterances prompting strategy
- In-context learning
- Adversarial demonstrations

**Metrics**:
- Attack success rate (ASR)
- Toxicity scores

**Calculation**: Average ASR scores calculated across different aspects

**Interpretation**: Higher ASR indicates lower trustworthiness

**Baseline Results**: DECODING TRUST

**Validation**: Comparison with baseline yields insights on model vulnerabilities

## ⚠️ Targeted Risks

**Risk Categories**:
- Toxicity
- Stereotype bias
- Ethics violations
- Hallucination occurrences
- Fairness issues
- Sycophancy tendencies
- Privacy breaches
- Robustness weaknesses

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning

**Potential Harm**: ['Potentially harmful outputs from LLMs', 'Bias against certain demographic groups']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: This research investigates risks related to privacy-sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
