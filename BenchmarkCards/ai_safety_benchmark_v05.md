# AI Safety Benchmark v0.5

## 📊 Benchmark Details

**Name**: AI Safety Benchmark v0.5

**Overview**: The AI Safety Benchmark v0.5 has been designed to assess the safety risks of AI systems that use language models, specifically focusing on an adult chatting to a general-purpose assistant in English across a limited set of personas.

**Data Type**: Text

**Domains**:
- General AI Safety
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HELM
- BIG-bench

**Resources**:
- [GitHub Repository](https://github.com/mlcommons/modelbench)
- [Resource](https://mlcommons.org/aisafety)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and benchmark the safety aspects of systems built on generative Language Models and to identify potential hazards in model responses.

**Target Audience**:
- Model providers
- Model integrators
- AI standards makers and regulators
- Researchers
- Civil society groups

**Tasks**:
- Assessing AI safety risks
- Benchmarking model responses

**Limitations**: Focused on a specific use case and three personas, does not evaluate more sophisticated user interactions.

**Out of Scope Uses**:
- Training the models
- General AI model safety outside specified use cases

## 💾 Data

**Source**: MLCommons AI Safety Working Group

**Size**: 43,090 test items

**Format**: Text prompts

**Annotation**: Each prompt has been annotated based on seven hazard categories.

## 🔬 Methodology

**Methods**:
- Manual prompt creation
- Automated safety evaluation with LlamaGuard

**Metrics**:
- Percentage of unsafe responses
- Grading system on a 5-point scale

**Calculation**: Percentage of unsafe responses calculated from the model outputs assessed against benchmark items.

**Interpretation**: Grades indicate relative safety risk of models based on the percentage of unsafe responses.

**Baseline Results**: N/A

**Validation**: Results were annotated by multiple assessors for consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Violent crimes
- Non-violent crimes
- Sex-related crimes
- Child sexual exploitation
- Indiscriminate weapons
- Suicide & self-harm
- Hate

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Value Alignment**: Toxic output
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: Potential for enabling various safety hazards, including violence, scams, and self-harm.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No individual data is collected; prompts are anonymized.

**Data Licensing**: Released under CC-BY license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Followed ethical guidelines for safety testing.
