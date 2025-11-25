# V ALSE (Vision And Language Structured Evaluation)

## 📊 Benchmark Details

**Name**: V ALSE (Vision And Language Structured Evaluation)

**Overview**: V ALSE is a novel benchmark designed for testing general-purpose pretrained vision and language (V&L) models for their visio-linguistic grounding capabilities on specific linguistic phenomena. It offers a suite of six tests covering various linguistic constructs.

**Data Type**: image-caption-foil triples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Heidelberg-NLP/VALSE)

## 🎯 Purpose and Intended Users

**Goal**: To assess the extent to which models learn to ground specific linguistic phenomena as a consequence of their pretraining (or fine-tuning).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Built using existing high-quality image captioning and VQA data.

**Size**: 8782 instances

**Format**: N/A

**Annotation**: Manual validation by crowdsourcing for all generated foils.

## 🔬 Methodology

**Methods**:
- Binary classification
- Image-sentence alignment score

**Metrics**:
- Accuracy
- Precision
- Foil Precision
- Pairwise Ranking Accuracy
- Area Under ROC Curve (AUC-ROC)

**Calculation**: Metrics calculated based on distinguishing correct and foiled examples.

**Interpretation**: High scores indicate better grounding capabilities of V&L models.

**Baseline Results**: N/A

**Validation**: Manual validation through a survey of human annotators on 5 categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
