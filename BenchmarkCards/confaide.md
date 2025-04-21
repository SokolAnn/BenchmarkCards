# CONFAIDE

## 📊 Benchmark Details

**Name**: CONFAIDE

**Overview**: A benchmark designed to test the privacy implications of language models through the lens of contextual integrity theory. It evaluates the ability of models to appropriately manage the flow of sensitive information in interactive settings.

**Data Type**: N/A

**Domains**:
- privacy
- social reasoning
- language models

**Resources**:
- [Resource](https://confaide.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the contextual privacy reasoning capabilities of language models.

**Target Audience**:
- researchers
- benchmark developers
- AI ethics practitioners

**Tasks**:
- assess privacy reasoning capabilities
- evaluate contextual integrity

**Limitations**: N/A

## 💾 Data

**Source**: Madden, 2014; Martin & Nissenbaum, 2016; GPT-4 generated text

**Size**: N/A

**Format**: N/A

**Annotation**: Human annotations were collected using Amazon Mechanical Turk.

## 🔬 Methodology

**Methods**:
- Information type sensitivity assessment
- Vignette surveys based on contextual factors
- Scenario generation involving theory of mind

**Metrics**:
- Sensitivity Score
- Leakage Rate
- Binary Control Question Error Rate
- Omitting Public Information Rate

**Calculation**: Measures are calculated based on model responses and compared against human annotations.

**Interpretation**: Higher sensitivity scores indicate less willingness to share information; lower leakage rates indicate better privacy preservation.

**Validation**: Results validated through comparison with human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy breaches
- Misuse of information
- Lack of appropriate contextual responses

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment, Reidentification
- **Robustness**: Prompt leaking, Data poisoning

**Potential Harm**: ['Privacy violations in sensitive contexts', 'Exposing personal information', 'Inappropriately managing information flow']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark assesses privacy expectations based on contextual integrity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study is exempt under US federal regulation 45 CFR 46.
