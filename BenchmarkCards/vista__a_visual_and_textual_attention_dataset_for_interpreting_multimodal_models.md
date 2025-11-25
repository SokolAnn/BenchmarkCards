# VISTA: A Visual and Textual Attention Dataset for Interpreting Multimodal Models

## 📊 Benchmark Details

**Name**: VISTA: A Visual and Textual Attention Dataset for Interpreting Multimodal Models

**Overview**: VISTA is a human-annotated visual and textual attention dataset designed to enhance the interpretability of Vision-Language Models (VLMs) by aligning eye-tracking data with textual descriptions to understand how humans associate visual regions with corresponding text segments.

**Data Type**: image-text saliency maps

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To explore and enhance the interpretability of Vision-Language Models through human-annotated visual and textual attention data.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Image-Text Alignment
- Image Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Data collected through eye-tracking with participants describing images while their attention was recorded.

**Size**: 508 image-text saliency maps

**Format**: N/A

**Annotation**: Manual annotation with eye-tracking data collection.

## 🔬 Methodology

**Methods**:
- Evaluation of image-text alignment models
- Use of NCC (Normalized Cross-Correlation) and AUC (Area Under Curve) metrics

**Metrics**:
- Normalized Cross-Correlation (NCC)
- Area Under Curve (AUC)

**Calculation**: NCC calculates correlation between the eye-tracking map and generated saliency map; AUC measures how well the saliency map distinguishes between human fixations and other areas.

**Interpretation**: Higher NCC and AUC scores indicate better alignment with human visual attention.

**Baseline Results**: N/A

**Validation**: Bootstrapping technique to estimate stability across iterations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Interpretability
- Transparency

**Atlas Risks**:
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants' audio recordings were deleted to ensure de-identification.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from participants before data collection.

**Compliance With Regulations**: Not Applicable
