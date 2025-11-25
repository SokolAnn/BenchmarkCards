# VideoA11y (Method and Dataset for Accessible Video Description)

## 📊 Benchmark Details

**Name**: VideoA11y (Method and Dataset for Accessible Video Description)

**Overview**: VideoA11y is a method and dataset designed to generate high-quality video descriptions specifically tailored for blind and low vision individuals, utilizing multimodal large language models and 42 audio description guidelines. The associated VideoA11y-40K dataset consists of 40,000 videos described in detail to enhance accessibility for BLV users.

**Data Type**: video and descriptions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://people-robots.github.io/VideoA11y/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance video accessibility for blind and low vision individuals by generating high-quality video descriptions.

**Target Audience**:
- ML Researchers
- Video Content Creators
- Accessibility Advocates

**Tasks**:
- Video Description Generation

**Limitations**: None

## 💾 Data

**Source**: VideoA11y-40K dataset is curated and includes various videos described specifically for blind and low vision users, incorporating multimodal large language models.

**Size**: 40,000 videos

**Format**: N/A

**Annotation**: Descriptions were generated using a method that adheres to audio description guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Custom metrics
- Standard metrics evaluation

**Metrics**:
- Descriptiveness
- Objectivity
- Accuracy
- Clarity
- BLEU Score
- ROUGE-L
- CIDEr
- SPICE

**Calculation**: Metrics calculated based on evaluations from both human users and automated scoring based on ground truth descriptions.

**Interpretation**: Higher scores in the metrics indicate better quality in descriptions, showing how well they serve the needs of blind and low vision users compared to traditional human-generated descriptions.

**Validation**: Validated through multiple user studies involving both sighted participants and blind and low vision individuals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset includes demographic breakdowns based on the user studies involving BLV individuals.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants in user studies gave informed consent as part of the study design and IRB approval.

**Compliance With Regulations**: Not Applicable
