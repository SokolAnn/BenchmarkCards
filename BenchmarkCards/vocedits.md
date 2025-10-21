# VOCEdits

## 📊 Benchmark Details

**Name**: VOCEdits

**Overview**: VOCEdits is a benchmark dataset for evaluating fine-grained object-level image editing, involving transformations such as flipping, scaling, rotation, translation, and shear. It is built upon PASCAL VOC 2012 with augmented instructional edit prompts, ground-truth transformations, and object masks before and after editing.

**Data Type**: image with instructional edit prompts and object masks

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://poem.compute.dtu.dk)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a comprehensive dataset for assessing the precision and reliability of object-level editing tasks in image processing.

**Target Audience**:
- ML Researchers
- Model Developers
- Computer Vision Practitioners

**Tasks**:
- Object Detection
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: PASCAL VOC 2012 dataset, augmented with instructional prompts and ground-truth transformations.

**Size**: 3030 unique samples

**Format**: N/A

**Annotation**: Augmented with instructional edits and precise ground-truth object masks for before-and-after transformations.

## 🔬 Methodology

**Methods**:
- Image-to-Image Translation
- Segmentation Mask Generation
- Instruction Parsing

**Metrics**:
- Intersection over Union (IoU)

**Calculation**: IoU is calculated between the predicted and ground-truth segmentation masks after applying transformations.

**Interpretation**: Higher IoU values indicate better performance in accurately editing images according to instructions.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
