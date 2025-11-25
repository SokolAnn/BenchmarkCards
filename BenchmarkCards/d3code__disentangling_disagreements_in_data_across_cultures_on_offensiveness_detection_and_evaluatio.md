# D3CODE: Disentangling Disagreements in Data across Cultures on Offensiveness Detection and Evaluation

## 📊 Benchmark Details

**Name**: D3CODE: Disentangling Disagreements in Data across Cultures on Offensiveness Detection and Evaluation

**Overview**: The D3CODE dataset is a large-scale cross-cultural dataset of parallel annotations for offensive language in over 4.5K sentences annotated by a pool of over 4k annotators, balanced across gender and age, from across 21 countries, representing eight geo-cultural regions, capturing annotators’ moral values along six moral foundations.

**Data Type**: offensive language annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Jigsaw Toxic Comments Classification
- Unintended Bias in Toxicity Classification

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To understand cross-cultural variations in perceptions of offensiveness in language.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Offensive Language Detection

**Limitations**: The dataset may not capture all cultural nuances as it is limited to English language data and may introduce sampling biases based on participant access.

## 💾 Data

**Source**: Data collected via online survey from annotators across 21 countries.

**Size**: 4,554 items

**Format**: N/A

**Annotation**: Annotated by over 4,309 participants balanced across gender and age demographics.

## 🔬 Methodology

**Methods**:
- Crowdsourced annotation with control items for reliability

**Metrics**:
- Inter-Rater Reliability (IRR)
- Cross-Replication Reliability (XRR)

**Calculation**: GAI metric provides a measurement of perspective diversities within annotator groups.

**Interpretation**: Higher GAI values indicate better in-group agreement.

**Baseline Results**: N/A

**Validation**: Annotations validated through quality control items and participant consistency checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of variations based on gender, age, and cultural background.

**Potential Harm**: ['Disagreement in perceptions of offensive language']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from participants for use of their responses.

**Compliance With Regulations**: Not Applicable
