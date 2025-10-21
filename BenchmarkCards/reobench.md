# REOBench

## 📊 Benchmark Details

**Name**: REOBench

**Overview**: REOBench is a comprehensive benchmark designed to evaluate the robustness of Earth observation foundation models across six core tasks and twelve perturbation types.

**Data Type**: High-resolution optical remote sensing images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/lx709/REOBench)
- [Resource](https://huggingface.co/datasets/xiang709/REOBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of remote sensing foundation models under various image corruptions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Scene Classification
- Semantic Segmentation
- Object Detection
- Image Captioning
- Visual Question Answering
- Visual Grounding

**Limitations**: The benchmark does not include key modalities such as multispectral, hyperspectral, and SAR data.

## 💾 Data

**Source**: AID for scene classification, ISPRS Potsdam for semantic segmentation, DIOR for object detection, and VRSBench for image captioning, visual question answering, and visual grounding.

**Size**: 20,264 training images and 9,350 test images across multiple datasets

**Format**: JSON

**Annotation**: Annotations include bounding boxes and classification labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Intersection over Union (mIoU)
- Average Precision (AP)

**Calculation**: Metrics are calculated based on model predictions against ground truth annotations.

**Interpretation**: Higher values indicate better model robustness and performance.

**Validation**: Results are validated through systematic experiments across multiple corruptions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Data poisoning
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used is publicly available with no personal information.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
