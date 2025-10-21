# INDIC-BIAS

## 📊 Benchmark Details

**Name**: INDIC-BIAS

**Overview**: INDIC-BIAS is a comprehensive India-centric benchmark designed to evaluate fairness of LLMs across 85 identity groups encompassing diverse castes, religions, regions, and tribes. It consists of 20,000 real-world scenario templates generated to probe biases and stereotypes in language models.

**Data Type**: scenario templates

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/AI4Bharat/indic-bias)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the INDIC-BIAS benchmark is to evaluate the fairness of large language models (LLMs) in the Indian context by examining biases and stereotypes associated with different identity groups.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Bias Evaluation
- Fairness Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Generated from curations and expert consultations focusing on socio-cultural topics relevant to Indian identity groups.

**Size**: 20,000 scenario templates

**Format**: JSON

**Annotation**: Manually validated by a team of experts based on socio-cultural relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Stereotype Association Rate (SAR)
- ELO Ratings

**Calculation**: Using a logistic regression-based Maximum Likelihood Estimate (MLE) method for computing ELO ratings to quantify bias based on the model's choices.

**Interpretation**: ELO ratings provide a ranking of identities based on which are selected more frequently in positive versus negative scenarios.

**Baseline Results**: N/A

**Validation**: Manual validation of 20,000 scenarios ensuring quality through a human-in-the-loop approach.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis throughout various identity groups across caste, religion, region, and tribe.

**Potential Harm**: ['Reinforcement of stereotypes in outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators provided consent and were informed about the nature of the tasks. No sensitive personal information was included.

**Data Licensing**: Resources are released under permissible licenses for open access to support further research.

**Consent Procedures**: Explicit consent was obtained from all participants involved in the data collection and annotation process.

**Compliance With Regulations**: Not Applicable
