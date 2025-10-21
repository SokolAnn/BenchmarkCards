# Aymara Image Fairness Evaluation

## 📊 Benchmark Details

**Name**: Aymara Image Fairness Evaluation

**Overview**: A benchmark for assessing social bias in AI-generated images, evaluating 13 commercial LMMs on their depiction of gender in professional roles using gender-neutral prompts to expose bias.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/aymara-ai-sdk)

## 🎯 Purpose and Intended Users

**Goal**: To assess gender bias in AI-generated images across multiple large multimodal models.

**Target Audience**:
- Researchers
- AI Developers

**Limitations**: Only evaluates binary gender representation, leaving out non-binary and transgender representations.

## 💾 Data

**Source**: Generated images from 13 LMMs using programmatically created prompts.

**Size**: 965 images

**Format**: N/A

**Annotation**: Automated scoring determined the gender representation in generated images.

## 🔬 Methodology

**Methods**:
- Automated evaluation

**Metrics**:
- Gender Bias Score
- Fairness Score

**Calculation**: Gender Bias Score measures deviation from gender parity for male and female predicted outputs; Fairness Score averages adherence to parity across all tasks.

**Interpretation**: Higher scores (closer to 1) indicate better performance toward gender equality in generated images.

**Baseline Results**: A comparison of model outputs indicates varying levels of gender bias across models, with some amplifying bias and others demonstrating significant gender parity.

**Validation**: Validated against human annotations showing a high agreement rate.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
