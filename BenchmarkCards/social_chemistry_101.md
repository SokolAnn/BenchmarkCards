# SOCIAL CHEMISTRY 101

## 📊 Benchmark Details

**Name**: SOCIAL CHEMISTRY 101

**Overview**: SOCIAL-CHEM-101 is a large-scale corpus that catalogs 292k rules-of-thumb related to social and moral norms, along with comprehensive annotations on judgments, cultural pressures, and legality across various real-life situations.

**Data Type**: rules-of-thumb with structured annotations

**Domains**:
- Natural Language Processing
- Ethics

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://arxiv.org/abs/2011.00620)

## 🎯 Purpose and Intended Users

**Goal**: To provide a formalism and resource for studying grounded social, moral, and ethical norms through crowdsourced rules-of-thumb (RoTs).

**Target Audience**:
- ML Researchers
- Ethicists
- Social Scientists

**Tasks**:
- Moral Reasoning
- Cultural Norm Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced annotations from reddit subreddits and other online sources including r/amitheasshole, r/confessions, ROCStories, and Dear Abby advice column.

**Size**: 292,000 rules-of-thumb

**Format**: JSON

**Annotation**: Crowdsourced by workers following structured guidelines for social norms.

## 🔬 Methodology

**Methods**:
- Neural modeling
- Crowdsourcing

**Metrics**:
- Micro-F1
- Accuracy

**Calculation**: Metrics calculated based on adherence of generated rules-of-thumb to the expected norms and judgments.

**Interpretation**: Model performance on generating relevant RoTs evaluated through human assessment and automated classification metrics.

**Validation**: Cross-validation with divided train/dev/test partitions ensuring diverse examples across various scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis included demographic factors of participants contributing to annotations capturing varied social expectations and judgments.

**Potential Harm**: ['Misjudgment in cultural norms leading to potential societal biases.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants' identities are anonymized throughout the data collection process.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
