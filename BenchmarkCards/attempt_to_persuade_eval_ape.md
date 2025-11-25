# Attempt to Persuade Eval (APE)

## 📊 Benchmark Details

**Name**: Attempt to Persuade Eval (APE)

**Overview**: APE is a benchmark evaluating a model's willingness to generate persuasive attempts across a diverse range of topics, including harmful and controversial content, to understand the risks associated with AI models in persuasive contexts.

**Data Type**: conversational interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AlignmentResearch/AttemptPersuadeEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of APE is to measure the propensity of language models to attempt persuasion, particularly in harmful contexts, to evaluate the effectiveness of safety guardrails.

**Target Audience**:
- AI Researchers
- Safety Engineers
- Policy Makers

**Tasks**:
- Persuasion Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Automated simulations between persuader and persuadee agents in a conversational setting.

**Size**: 600 topics (100 distinct across six categories)

**Format**: JSON

**Annotation**: Automated evaluation based on model interactions.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Persuasion attempt rate

**Calculation**: Persuasion attempts are assessed through multi-turn dialogues, classifying interactions as attempts or refusals.

**Interpretation**: Interpretation focuses on the degree to which models attempt to persuade across different contexts and topics.

**Baseline Results**: Various AI models attempted persuasion significantly for harmful topics.

**Validation**: Validation includes automated assessments aligned with human judgment on persuasion attempts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Ethics

**Atlas Risks**:
- **Fairness**: Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: Models may attempt persuasive behaviors in harmful contexts, raising ethical concerns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
