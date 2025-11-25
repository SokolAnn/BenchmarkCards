# PAPERS PLEASE

## 📊 Benchmark Details

**Name**: PAPERS PLEASE

**Overview**: A benchmark consisting of 3,700 moral dilemmas designed to investigate LLMs’ decision-making in prioritizing various levels of human needs based on the Existence, Relatedness, and Growth (ERG) theory.

**Data Type**: role-playing scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yeonsuuuu28/papers-please)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how LLMs reason about human motivational values and respond to social identity cues.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Ethical Decision Making

**Limitations**: The analysis is limited to six LLMs, which may restrict the generalizability of the findings.

## 💾 Data

**Source**: Manually created scenarios reflecting human motivations based on ERG theory.

**Size**: 3,700 scenarios

**Format**: N/A

**Annotation**: Manually reviewed and refined by the authors.

## 🔬 Methodology

**Methods**:
- Evaluation of decision-making

**Metrics**:
- Acceptance rates

**Calculation**: Measurements of acceptance and denial rates across different motivational categories.

**Interpretation**: Models must balance moral and political factors in their decision-making.

**Validation**: Chi-square tests conducted to assess statistical significance of model decisions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes social identity factors such as race, gender, and religion.

**Potential Harm**: ['Higher denial rates for marginalized identities.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
