# WinoBias

## 📊 Benchmark Details

**Name**: WinoBias

**Overview**: A benchmark for coreference resolution focused on gender bias using Winograd-schema style sentences with entities corresponding to people referred by their occupation.

**Data Type**: Text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Ontonotes
- CoNLL-2011
- CoNLL-2012

**Resources**:
- [Resource](http://winobias.org)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate gender bias in coreference resolution systems.

**Target Audience**:
- Researchers
- Developers in Natural Language Processing

**Tasks**:
- Coreference Resolution
- Bias Evaluation

**Limitations**: None

## 💾 Data

**Source**: WinoBias dataset created by researchers familiar with the project.

**Size**: 3,160 sentences

**Format**: Text

**Annotation**: Sentences created with equal numbers of correct co-reference decisions for all occupations.

## 🔬 Methodology

**Methods**:
- Rule-based
- Feature-rich
- Neural Coreference System

**Metrics**:
- F1 Score

**Calculation**: Average difference in F1 score between pro-stereotyped and anti-stereotyped conditions.

**Interpretation**: Systems must link gendered pronouns to pro-stereotypical and anti-stereotypical occupations equally well.

**Validation**: Demonstrated through comparison with established datasets like OntoNotes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in training data
- Underrepresentation of female entities

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt leaking

**Demographic Analysis**: Underrepresentation of female references in training datasets.

**Potential Harm**: Amplification of gender stereotypes through biased predictions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data includes references to occupations and gendered pronouns, anonymized to mitigate bias.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
