# Us vs. Them

## 📊 Benchmark Details

**Name**: Us vs. Them

**Overview**: We present the new Us vs. Them dataset, consisting of 6861 Reddit comments annotated for populist attitudes and the first large-scale computational models of this phenomenon.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LittlePea13/UsVsThemarXiv:2101.11956v3)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the relationship between populist mindsets and social groups, as well as a range of emotions typically associated with these.

**Target Audience**:
- ML Researchers
- Social Scientists

**Tasks**:
- Populist Attitude Detection
- Emotion Detection

**Limitations**: N/A

## 💾 Data

**Source**: Comments extracted from Reddit that refer to social groups in response to news articles.

**Size**: 6,861 comments

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk

## 🔬 Methodology

**Methods**:
- Automated metrics
- Multi-task learning

**Metrics**:
- Pearson correlation coefficient

**Calculation**: Mean Squared Error loss for regression task; Cross-Entropy loss for classification.

**Interpretation**: Higher scores indicate a more discriminatory attitude towards the labeled group.

**Baseline Results**: Pearson R of 0.545 as single-task baseline; MTL with emotions achieved 0.570.

**Validation**: Statistical tests including ANOVA and Tukey HSD test for significance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
