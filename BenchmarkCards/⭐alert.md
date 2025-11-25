# ALERT

## 📊 Benchmark Details

**Name**: ALERT

**Overview**: ALERT is a large-scale benchmark designed to assess the safety of Large Language Models (LLMs) using red teaming methodologies, comprised of over 45k instructions categorized under a novel fine-grained risk taxonomy.

**Data Type**: Red teaming prompts

**Resources**:
- [GitHub Repository](https://github.com/Babelscape/ALERT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the safety of LLMs through comprehensive risk assessment.

**Target Audience**:
- Researchers
- Developers
- Policymakers

**Tasks**:
- Assess the safety of LLMs
- Identify vulnerabilities in models
- Improve safety mechanisms

**Limitations**: The benchmark focuses exclusively on harmful prompts and may not detect evasive or unhelpful responses to harmless prompts.

**Out of Scope Uses**:
- General language generation tasks not related to safety

## 💾 Data

**Source**: Anthropic red-team-attempts dataset; additional prompts created using templated prompts and LLM rewriting

**Size**: 45k red teaming prompts

**Format**: Text prompts

**Annotation**: Categorized according to a novel safety risk taxonomy

## 🔬 Methodology

**Methods**:
- Red teaming
- Zero-shot classification
- Prompt injection
- Adversarial testing
- Policy evaluation based on safety categories

**Metrics**:
- Safety scores
- Category-specific safety scores
- LlamaGuard safety classifier

**Calculation**: Safety scores are calculated based on the number of safe responses divided by total prompts in each category.

**Interpretation**: Scores indicate model vulnerability and safety levels.

**Validation**: Evaluated against 10 popular LLMs

## ⚠️ Targeted Risks

**Risk Categories**:
- Hate Speech & Discrimination
- Criminal Planning
- Regulated or Controlled Substances
- Sexual Content
- Suicide & Self-Harm
- Guns & Illegal Weapons

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Data Laws**: Data usage restrictions, Data acquisition restrictions, Data transfer restrictions
- **Privacy**: Personal information in data, Reidentification
- **Fairness**: Data bias, Output bias
- **Legal Compliance**: Model usage rights restrictions
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: Identifies model vulnerabilities in generating harmful content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Prompts may elicit sensitive information but are focused on safety assessment.

**Data Licensing**: Data from Anthropic is utilized and follows relevant restrictions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Evaluations can be adjusted according to different legal contexts.
