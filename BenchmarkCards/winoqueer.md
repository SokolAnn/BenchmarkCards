# WinoQueer

## 📊 Benchmark Details

**Name**: WinoQueer

**Overview**: WinoQueer is a benchmark specifically designed to measure whether large language models encode biases that are harmful to the LGBTQ+ community, developed through community feedback and input.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Bias Measurement

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-Pairs
- HOLISTIC BIAS

**Resources**:
- [GitHub Repository](https://github.com/katyfelkner/winoqueer)

## 🎯 Purpose and Intended Users

**Goal**: To measure and address anti-LGBTQ+ bias in large language models effectively.

**Target Audience**:
- NLP researchers
- Ethicists
- LGBTQ+ Advocates

**Tasks**:
- Benchmarking the performance of language models on LGBTQ+ bias.
- Identifying biases in text generation.

**Limitations**: While WinoQueer aims to address LGBTQ+ biases, it may not encompass all experiences within the community.

**Out of Scope Uses**:
- Non-LGBTQ+ bias measurement
- General bias measurement not related to LGBTQ+ issues

## 💾 Data

**Source**: Community-driven survey of LGBTQ+ individuals

**Size**: 45540 sentence pairs

**Format**: Text

**Annotation**: Community input regarding harmful stereotypes and biases.

## 🔬 Methodology

**Methods**:
- Community-survey based dataset development
- Fine-tuning language models on QueerNews and QueerTwitter datasets

**Metrics**:
- Pseudo-log-likelihood for bias measurement
- Comparison of likelihood of stereotypical versus counterfactual sentences

**Calculation**: Scores are calculated based on how frequently a model predicts the stereotypical sentence over the counterfactual.

**Interpretation**: Higher scores indicate greater bias towards outputting stereotypical content.

**Baseline Results**: Average WinoQueer bias score across models is 66.50.

**Validation**: Models were evaluated against a baseline of known biases to confirm effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness
- Explainability

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data, Exposing personal information
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The survey data reflects a range of identities within the LGBTQ+ community.

**Potential Harm**: The study addresses tangible biases that have caused psychological harm to LGBTQ+ individuals.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected is anonymized and identifiers are removed to ensure participant confidentiality.

**Data Licensing**: Data collected from community inputs is used under a participation agreement.

**Consent Procedures**: Participants provided informed consent to partake in the survey.

**Compliance With Regulations**: IRB exempt status for the study was established based on participant anonymity and Voluntary participation.
