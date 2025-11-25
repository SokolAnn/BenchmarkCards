# COBIAS (Context-Oriented Bias Indicator and Assessment Score)

## 📊 Benchmark Details

**Name**: COBIAS (Context-Oriented Bias Indicator and Assessment Score)

**Overview**: COBIAS evaluates model robustness to biased statements by considering various contexts, aiming to improve bias benchmarks for language models.

**Data Type**: stereotyped statements with contextual annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CrowS-Pairs
- StereoSet
- WinoGender
- RedditBias
- WinoBias

**Resources**:
- [GitHub Repository](https://github.com/priyanshul-govil/COBIAS)

## 🎯 Purpose and Intended Users

**Goal**: To assess the contextual reliability of bias benchmarks and improve their quality.

**Target Audience**:
- ML Researchers
- Bias Mitigation Practitioners

**Tasks**:
- Bias Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Augmented dataset created from CrowS-Pairs and StereoSet with contextual annotations.

**Size**: 2,291 statements

**Format**: JSON

**Annotation**: Human verified with a majority vote of three annotators for context-addition points.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Spearman's correlation
- COBIAS score

**Calculation**: COBIAS is calculated by averaging the context-variance scores of statements.

**Interpretation**: A higher COBIAS score indicates better contextual reliability.

**Baseline Results**: N/A

**Validation**: Validated against human judgment with high correlation (Spearman’s 𝜌=0.65).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
