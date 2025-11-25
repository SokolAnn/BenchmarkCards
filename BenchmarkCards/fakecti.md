# FakeCTI

## 📊 Benchmark Details

**Name**: FakeCTI

**Overview**: FakeCTI is the first dataset that systematically links fake news articles to known disinformation campaigns and threat actors, consisting of 12,155 articles from 43 distinct campaigns, each annotated with metadata specifying the associated campaign, threat actor, and dissemination medium.

**Data Type**: text

**Domains**:
- Cybersecurity
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured foundation for attribution studies in disinformation analysis.

**Target Audience**:
- Research Community
- Cybersecurity Analysts

**Tasks**:
- Fake News Attribution
- Disinformation Campaign Analysis

**Limitations**: Dataset reflects only the accessible portion of the content of the campaigns due to the removal of false content after reporting.

## 💾 Data

**Source**: Data collected from archives of fake news reports linked by Wikipedia.

**Size**: 12,155 articles

**Format**: CSV

**Annotation**: Manually labeled based on association with specific disinformation campaigns and threat actors.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Measured accuracy of various attribution techniques including lexical and semantic similarity methods.

**Interpretation**: Accuracy in fake news attribution techniques evaluated up to 94%, highlighting the effectiveness of the methodologies employed.

**Baseline Results**: Achieved attribution accuracy up to 94% using fine-tuned LLMs.

**Validation**: Experimental analysis of attribution techniques assessed using the FakeCTI dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
