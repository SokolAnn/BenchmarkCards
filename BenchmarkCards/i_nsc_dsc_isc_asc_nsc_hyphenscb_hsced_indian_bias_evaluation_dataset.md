# I/n.sc/d.sc/i.sc/a.sc/n.sc/hyphen.scB/h.scED (Indian Bias Evaluation Dataset)

## 📊 Benchmark Details

**Name**: I/n.sc/d.sc/i.sc/a.sc/n.sc/hyphen.scB/h.scED (Indian Bias Evaluation Dataset)

**Overview**: This paper introduces a dataset to quantify stereotypical bias in large language models within the Indian context, focusing on caste and religious biases, and compares them to biases prevalent in Western contexts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/khyatikhandelwal/Indian-LLMs-Bias)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLM bias in application contexts beyond Western countries, specifically in India, and provide insights into caste and religious biases in language models.

**Target Audience**:
- ML Researchers
- Domain Experts
- AI Practitioners

**Tasks**:
- Bias Measurement
- Fairness Evaluation

**Limitations**: The dataset size and nature should be expanded in future work to include more languages and stereotypes.

## 💾 Data

**Source**: Constructed using literature on caste-based and religious stereotypes, as well as qualitative feedback from Indian experts in related fields.

**Size**: 229 examples

**Format**: CSV

**Annotation**: Expert-reviewed and qualitatively validated by scholars on caste and religious studies.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Log-Likelihood
- Conditional Log-Likelihood

**Calculation**: Log-likelihoods of models for stereotypical and anti-stereotypical examples are computed to measure bias propensity.

**Interpretation**: Scores close to 50% indicate balanced perspectives between stereotypical and anti-stereotypical outputs; higher scores reflect stronger bias towards stereotypes.

**Baseline Results**: N/A

**Validation**: Peer-reviewed and validated by experts in the field.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: Analysis based on caste and religious associations among different Indian demographics is included.

**Potential Harm**: ['Representation of harmful stereotypes', 'Potential for reinforcing negative biases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
