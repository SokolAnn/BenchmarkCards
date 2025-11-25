# CVLUE (Chinese Vision-Language Understanding Evaluation)

## 📊 Benchmark Details

**Name**: CVLUE (Chinese Vision-Language Understanding Evaluation)

**Overview**: CVLUE is a vision-language understanding benchmark dataset specifically designed for the comprehensive evaluation of vision-language models in Chinese VLU. Its images are representative of Chinese culture, and it includes four distinct tasks: image-text retrieval, visual question answering, visual grounding, and visual dialogue.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese

**Similar Benchmarks**:
- VLUE
- CLiMB
- MUGE
- Flickr30K-CN
- COCO-CN

**Resources**:
- [GitHub Repository](https://github.com/WangYuxuan93/CVLUE)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CVLUE is to provide a fair and comprehensive evaluation platform for evaluating vision-language models in the context of Chinese culture.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Image-Text Retrieval
- Visual Question Answering
- Visual Grounding
- Visual Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Images were manually collected from the Chinese Internet, ensuring representation of Chinese culture.

**Size**: 17,920 training examples, 3,116 validation examples, 8,973 test examples for Image-Text Retrieval; 14,362 training examples, 2,571 validation examples, 7,169 test examples for Visual Question Answering; 10,769 training examples, 1,965 validation examples, 5,385 test examples for Visual Grounding; 3,975 training examples, 651 validation examples, 2,036 test examples for Visual Dialogue.

**Format**: N/A

**Annotation**: Images were annotated through a combination of expert and crowd-sourced methods, including manual labeling and peer reviews.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- Recall at k (R@k)
- Intersection over Union (IoU)

**Calculation**: Metrics are calculated based on the specific evaluation tasks defined in CVLUE.

**Interpretation**: Higher scores indicate better performance in understanding and generating responses regarding Chinese visual-language tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Cultural representation

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Images collected from the Chinese Internet are visually unobtrusive, with sensitive information obscured.

**Data Licensing**: The proposed dataset will be made publicly available for research purposes under the CC BY-NC-ND 4.0 license.

**Consent Procedures**: All annotators have given informed consent and are compensated.

**Compliance With Regulations**: Not Applicable
