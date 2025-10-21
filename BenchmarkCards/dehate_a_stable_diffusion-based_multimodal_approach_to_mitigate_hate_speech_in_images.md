# DeHate (A Stable Diffusion-based Multimodal Approach to Mitigate Hate Speech in Images)

## 📊 Benchmark Details

**Name**: DeHate (A Stable Diffusion-based Multimodal Approach to Mitigate Hate Speech in Images)

**Overview**: The paper introduces a multimodal dataset for identifying hate in digital content, leveraging stable diffusion techniques to generate hate attention maps and blurring hateful regions from images.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset focused on dehating digital content and encourage research in hate speech mitigation.

**Target Audience**:
- ML Researchers
- AI Ethics Practitioners
- Model Developers

**Tasks**:
- Image Dehate

**Limitations**: N/A

## 💾 Data

**Source**: Hatenorm dataset and generated through the stable-diffusion model.

**Size**: 2,411 instances

**Format**: N/A

**Annotation**: Using Diffusion Attentive Attribution Maps (DAAM) for generating heatmaps to identify hateful content.

## 🔬 Methodology

**Methods**:
- Image Generation
- Image Blurring

**Metrics**:
- Intersection over Union (IoU)

**Calculation**: IoU was computed between the predicted blurred component and the ground truth blurred component in the test dataset.

**Interpretation**: A higher IoU indicates better performance of the dehate model.

**Baseline Results**: Baseline performance is an IoU score of 0.49.

**Validation**: Evaluated through shared task submissions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Ethics in AI

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Mitigation of harmful and hateful content in digital images.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
