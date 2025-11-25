# SweEval: Do LLMs Really Swear? A Safety Benchmark for Testing Limits for Enterprise Use

## 📊 Benchmark Details

**Name**: SweEval: Do LLMs Really Swear? A Safety Benchmark for Testing Limits for Enterprise Use

**Overview**: SweEval is a benchmark that evaluates LLMs' ability to handle swearing under different contexts and tones, focusing on the ethical and contextual reasoning capabilities of these models in enterprise environments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- French
- German
- Hindi
- Marathi
- Bengali
- Gujarati

**Similar Benchmarks**:
- PKU-SafeRLHF
- ToxicChat
- HarmBench
- SALAD-Bench
- SafetyBench
- Toxigen

**Resources**:
- [GitHub Repository](https://github.com/amitbcp/multilingual_profanity)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs' compliance with ethical frameworks and cultural nuances when handling sensitive language, specifically swearing.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Enterprise Users

**Tasks**:
- Text Classification
- Ethical Evaluation
- Safety Assessment

**Limitations**: The current benchmark does not include swear words from all underrepresented languages.

## 💾 Data

**Source**: Manually created dataset of instruction prompts relevant to enterprise and casual contexts, including swear words in varied linguistic and cultural contexts.

**Size**: 2,725 prompts per language

**Format**: N/A

**Annotation**: Manually reviewed for prompt creation and classification of unsafe responses.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Automated metrics

**Metrics**:
- Harmful Rate

**Calculation**: Harmful Rate is calculated as #Harmful / (#Harmless + #Harmful).

**Interpretation**: A lower Harmful Rate indicates better performance in resisting harmful outputs.

**Baseline Results**: Evaluation included various models such as Mistral and Llama for comparative analysis.

**Validation**: Validation procedures involved manual review and classification of model responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**
- **Societal Impact**

**Demographic Analysis**: The benchmark includes analyses of model responses across different demographics.

**Potential Harm**: The benchmark aims to identify safety flaws and instances of harmful output across various contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is released under an open-source license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
