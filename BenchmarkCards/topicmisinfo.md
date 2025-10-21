# TopicMisinfo

## 📊 Benchmark Details

**Name**: TopicMisinfo

**Overview**: The TopicMisinfo dataset contains 160 fact-checked claims supplemented by nearly 1600 human annotations with subjective perceptions and annotator demographics, aimed at analyzing the implications of using large language models for claim prioritization in the context of misinformation.

**Data Type**: fact-checked claims with human annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

## 🎯 Purpose and Intended Users

**Goal**: To investigate whether large language models can reflect diverse opinions regarding the harms of misinformation based on gendered perceptions.

**Target Audience**:
- Fact-checkers
- AI Researchers
- Model Developers

**Tasks**:
- Claim Prioritization
- Fact-Checking

**Limitations**: The study is limited as it only includes data from men and women without non-binary perspectives, which may not capture the full diversity of opinions.

## 💾 Data

**Source**: Claims sourced from the Google Fact-Check API covering a wide range of topics with human annotations provided via Amazon Mechanical Turk.

**Size**: 160 claims

**Format**: N/A

**Annotation**: Crowdsourced human annotations using a Likert scale for assessing subjective perceptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Rate of perceived harm
- Alignment with human assessments

**Calculation**: Z-score transformation of annotations for normalization.

**Interpretation**: Higher scores indicate higher perceived harm and alignment towards gendered opinions, particularly focusing on claim prioritization.

**Validation**: Data validated through attention checks and criteria established prior to annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Annotations predominantly from men (69%) and women (31%).

**Potential Harm**: ['Potential misinformation amplification based on gendered biases in LLM responses.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained via demographic surveys.

**Compliance With Regulations**: Not Applicable
