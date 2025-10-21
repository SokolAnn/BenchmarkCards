# HalLoc (Token-level Localization of Hallucinations for Vision Language Models)

## 📊 Benchmark Details

**Name**: HalLoc (Token-level Localization of Hallucinations for Vision Language Models)

**Overview**: HalLoc is a large-scale dataset comprising 155K samples annotated at the token level with specific types of hallucinations across Visual Question Answering (VQA), instruction-following, and image captioning tasks, designed to facilitate the development of models for efficient hallucination detection.

**Data Type**: token-level annotated samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/dbsltm/cvpr25_halloc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for efficient detection of hallucinations in vision-language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Instruction Following
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available dataset composed of synthesized hallucinated samples via HQA-injection pipeline.

**Size**: 155,953 examples

**Format**: N/A

**Annotation**: Token-level annotated with specific types of hallucinations including object, attribute, relationship, and scene hallucinations.

## 🔬 Methodology

**Methods**:
- Token-level hallucination detection model
- Probabilistic assessments integrated into existing VLMs

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on the model's performance across different hallucination types.

**Interpretation**: Higher F1 scores indicate better performance in accurately identifying hallucinations.

**Baseline Results**: N/A

**Validation**: N/A

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
