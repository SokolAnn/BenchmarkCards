# COCONut-PanCap

## 📊 Benchmark Details

**Name**: COCONut-PanCap

**Overview**: The COCONut-PanCap dataset is created to enhance panoptic segmentation and grounded image captioning, incorporating fine-grained, region-level captions grounded in segmentation masks to improve the detail of generated captions for multi-modal learning tasks.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- COCO-caption

**Resources**:
- [Resource](https://arxiv.org/abs/2502.02589)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for detailed captioning and grounded segmentation tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Detailed Captioning
- Panoptic Segmentation
- Text-to-Image Generation
- Visual Question Answering
- Referring Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: COCO images with advanced COCONut panoptic masks

**Size**: 143,000 image-text pairs (118,000 for training, 25,000 for validation)

**Format**: JPEG

**Annotation**: Human-edited, densely annotated descriptions with segmentation masks

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CIDEr
- METEOR
- BLEU@4
- ROUGE-L
- PQ

**Calculation**: Metrics are calculated as standard scores comparing generated captions against human annotations.

**Interpretation**: Higher scores indicate better performance in generating detailed and accurate captions.

**Baseline Results**: The proposed dataset outperformed recent detailed caption datasets.

**Validation**: Evaluation was performed on a validation set of 25,000 images.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
