# LLM Stereotype Index (LSI)

## 📊 Benchmark Details

**Name**: LLM Stereotype Index (LSI)

**Overview**: An extensible benchmark for evaluating stereotypes and bias in Large Language Models, grounded on the Social Progress Index.

**Data Type**: N/A

**Domains**:
- N/A

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Avenge-PRC777/Uncovering_Stereotypes_In_LLM_A_Task_Complexity_Approach)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate bias in language models across various demographic categories and social dimensions.

**Target Audience**:
- Researchers
- AI practitioners
- Policymakers

**Tasks**:
- Evaluate bias in language generation
- Measure stereotype representation

**Limitations**: The work tries to cover many demographics but is not comprehensive.

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: 157k generations from evaluated LLMs

**Size**: 157k

**Format**: Generated text data

**Annotation**: Labeled for positive/negative stereotypes

## 🔬 Methodology

**Methods**:
- Task complexity assessment
- Bias detection through generative tasks

**Metrics**:
- Choice Refusal Percentage (CRP)
- Stereotype Polarity (SP)

**Calculation**: CRP is the percentage of tasks where the model refused to make a choice. SP measures the fraction of positive stereotypes chosen.

**Interpretation**: Higher CRP indicates better awareness of harmful choices. Lower SP for certain demographics indicates systemic bias.

**Baseline Results**: N/A

**Validation**: Experiments validated by generating and analyzing 157k outputs

## ⚠️ Targeted Risks

**Risk Categories**:
- Societal Impact
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias, Output bias
- **Societal Impact**: Impact on cultural diversity, Impact on Jobs, Impact on education: bypassing learning

**Demographic Analysis**: Bias evaluated across nationality, gender, race, and religion.

**Potential Harm**: Stereotypical biases observed leading to systemic harm, especially for underrepresented groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Generic data used, no unique identifiers.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Warnings provided for potentially offensive content.
