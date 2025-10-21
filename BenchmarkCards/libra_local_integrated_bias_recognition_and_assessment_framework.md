# LIBRA (Local Integrated Bias Recognition and Assessment Framework)

## 📊 Benchmark Details

**Name**: LIBRA (Local Integrated Bias Recognition and Assessment Framework)

**Overview**: The LIBRA framework measures bias in large language models (LLMs) specifically within local contexts, tackling the challenges of inherent biases in LLMs when deployed in diverse cultural settings. It emphasizes the use of datasets sourced from local corpora, avoiding crowdsourcing, to evaluate and improve the sensitivity of LLMs to cultural diversity.

**Data Type**: test cases

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Māori

**Resources**:
- [GitHub Repository](https://github.com/ipangbo/LIBRA)

## 🎯 Purpose and Intended Users

**Goal**: To measure bias of large language models in local contexts by leveraging local datasets and providing a robust evaluation framework.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Bias Measurement

**Limitations**: N/A

## 💾 Data

**Source**: New Zealand local media articles comprising over 360,000 articles collected for bias evaluation.

**Size**: 360,000 articles

**Format**: not specified

**Annotation**: Manually annotated by local cultural experts.

## 🔬 Methodology

**Methods**:
- Dataset creation using local corpora
- Bias evaluation using Enhanced Idealized CAT Score (EiCAT)

**Metrics**:
- Enhanced Idealized CAT Score (EiCAT)
- Jensen-Shannon Divergence (JSD)

**Calculation**: The EiCAT score is computed using the distribution of logits associated with stereotypical and anti-stereotypical predicted outcomes normalized by knowledge boundary scoring.

**Interpretation**: Higher EiCAT scores indicate reduced bias and better handling of local vocabulary by the model.

**Baseline Results**: N/A

**Validation**: The pipeline utilizes both qualitative and quantitative measures through expert reviews and statistical comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes demographic groups relevant to New Zealand's cultural context.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
