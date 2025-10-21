# BanStereoSet

## 📊 Benchmark Details

**Name**: BanStereoSet

**Overview**: BanStereoSet is a dataset designed to evaluate stereotypical social biases in multilingual LLMs for the Bangla language, focusing on biases in categories such as race, profession, gender, ageism, beauty, caste, and religion.

**Data Type**: fill-in-the-blank sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- StereoSet
- IndiBias
- GenAssocBias

**Resources**:
- [GitHub Repository](https://github.com/kamruzzaman15/BanStereoSet)

## 🎯 Purpose and Intended Users

**Goal**: To measure stereotypical biases in multilingual LLMs, particularly focusing on the Bangla language.

**Target Audience**:
- ML Researchers
- Ethics and Bias Experts
- Language Technology Developers

**Tasks**:
- Bias Measurement

**Limitations**: The dataset focuses solely on the Bangladesh context, potentially overlooking biases present in other Bangla-speaking populations. It is also limited to binary gender representation and may not cover all forms of bias comprehensively.

## 💾 Data

**Source**: Localized content from StereoSet, IndiBias, and GenAssocBias datasets curated specifically for the Bangla language.

**Size**: 1,194 sentences

**Format**: N/A

**Annotation**: Translated and annotated by native Bangla speakers.

## 🔬 Methodology

**Methods**:
- Evaluation on multilingual LLMs
- Bias analysis through percentage of stereotypical responses

**Metrics**:
- Percentage of stereotypical engagement

**Calculation**: Calculated as the percentage of responses that align with stereotypical judgments excluding unrelated engagements.

**Interpretation**: Lower percentages are desired for stereotypical engagement, especially in categories derived from StereoSet due to the presence of negative stereotypes.

**Baseline Results**: Not provided

**Validation**: Validated through consensus among annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Analysis focuses primarily on stereotypes affecting the Bangla-speaking community, without a comprehensive breakdown of intersectional identities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
