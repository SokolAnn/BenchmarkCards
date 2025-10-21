# GPT-WritingPrompts Dataset

## 📊 Benchmark Details

**Name**: GPT-WritingPrompts Dataset

**Overview**: The GPT-WritingPrompts dataset pairs short stories written by Reddit users in response to 97,219 prompts with comparable generations from GPT-3.5, analyzing differences in emotional and descriptive features along six dimensions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/KristinHuangg/gpt-writing-prompts)

## 🎯 Purpose and Intended Users

**Goal**: To compare generative and human models of language production in response to the same prompts, and to analyze biases in storytelling.

**Target Audience**:
- ML Researchers
- Social Scientists
- Writers

**Tasks**:
- Text Generation
- Bias Analysis

**Limitations**: The dataset has a gap in the number of stories per prompt between GPT-generated and human-written subsets, limiting comparability.

## 💾 Data

**Source**: Reddit WritingPrompts dataset.

**Size**: 97,219 prompts with corresponding human and machine-generated responses.

**Format**: N/A

**Annotation**: Stories are generated using GPT-3.5 and paired with human-written responses to the same prompts.

## 🔬 Methodology

**Methods**:
- Lexical Analysis
- Statistical Comparison

**Metrics**:
- Valence
- Arousal
- Dominance
- Appearance Bias
- Intellect Bias
- Power Bias

**Calculation**: Scores calculated using methods such as average lexical score and average embedding similarity.

**Interpretation**: Higher scores indicate more positive, powerful portrayals; biases are quantified based on character portrayal dimensions.

**Baseline Results**: N/A

**Validation**: Comparison of human-written and GPT-generated stories to establish differences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis conducted on biases in character portrayal across gender lines.

**Potential Harm**: ['Reinforcing stereotypes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
