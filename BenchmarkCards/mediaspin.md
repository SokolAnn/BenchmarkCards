# MediaSpin

## 📊 Benchmark Details

**Name**: MediaSpin

**Overview**: The MediaSpin dataset characterizes the bias in how prominent news outlets editorialize news headlines after publication. It includes 78,910 pairs of headlines annotated with 13 distinct types of media bias, using human-supervised LLM labeling.

**Data Type**: headline pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/mediaspin-A5C7)

## 🎯 Purpose and Intended Users

**Goal**: To systematically identify and analyze types of media bias in editorialized news headlines.

**Target Audience**:
- ML Researchers
- Media Analysts
- Content Moderation Practitioners

**Tasks**:
- Bias Detection
- Text Classification

**Limitations**: The dataset contains subjective and editorialized references to gender, ethnicity, and religion, with potential for misuse.

## 💾 Data

**Source**: Generated from revisions of news headlines from five major English language media outlets.

**Size**: 78,910 pairs

**Format**: CSV

**Annotation**: Annotated using an LLM pipeline, specifically GPT-3.5-turbo.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on model performance in classifying annotated biases.

**Interpretation**: Higher accuracy indicates better model performance in correctly identifying types of bias.

**Baseline Results**: DeBERTa-v3-small achieved 0.773 accuracy for subjective bias.

**Validation**: Human validation with an inter-annotator agreement of 84.9%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Participants included a variety of demographics focusing on political affiliation and education.

**Potential Harm**: ['Potential misuse in content moderation applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
