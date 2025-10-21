# ASE Dataset (Automated Optical Inspection for Defect Classification)

## 📊 Benchmark Details

**Name**: ASE Dataset (Automated Optical Inspection for Defect Classification)

**Overview**: The ASE dataset is proposed for defect classification and addresses challenges such as data insufficiency and monotonous patterns in images, which are not effectively handled by traditional models. By leveraging vision-language models (VLM) and large-language models (LLM) through a prompting strategy, the dataset aims to capture external-modal features to enhance classification performance.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/breezedeus/cnocr)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for enhancing defect classification in industrial manufacturing through the use of multimodal learning techniques.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Defect Classification

**Limitations**: N/A

## 💾 Data

**Source**: Provided by ASE corporation, consisting of image and corresponding statistical data about defects.

**Size**: 455 samples

**Format**: N/A

**Annotation**: Numeric and textual information recorded corresponding to visual data.

## 🔬 Methodology

**Methods**:
- Prompting with VLM-LLM
- Progressive Feature Alignment (PFA)
- Cross-modality attention fusion (CMAF)

**Metrics**:
- F1 Score
- Macro F1 Score

**Calculation**: F1 Score is calculated as 2 * (precision * recall) / (precision + recall), with macro F1 Score being the average across classes.

**Interpretation**: Higher F1 and Macro F1 Scores indicate better classification performance across the dataset.

**Validation**: Model performance is validated through experiments comparing results across multiple defect classification methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
