# OK-VQA (Object Retrieval for Visual Question Answering with Outside Knowledge)

## 📊 Benchmark Details

**Name**: OK-VQA (Object Retrieval for Visual Question Answering with Outside Knowledge)

**Overview**: This paper introduces the task of object retrieval for visual question answering with outside knowledge, proposing a multi-scale group collaborative embedding learning (MS-GCEL) method for general object retrieval. The study includes the establishment of an OK-VQA evaluation benchmark.

**Data Type**: image-object pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2403.10798)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the precision and relevance of visual question answering by improving object-level retrieval methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Object Retrieval
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Images extracted from COCO 2017, VOC 2007, BelgaLogos, Visual Genome, and LVIS datasets.

**Size**: 121,298 training images, 9,904 validation images, 108,077 Generalization evaluation images.

**Format**: N/A

**Annotation**: Objects extracted using the segment anything model (SAM).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall@1
- Mean Average Precision (mAP)

**Calculation**: Recall@1 measures the accuracy of the top 1 retrieved object, while mAP is computed based on ranking indices of matching objects.

**Interpretation**: Higher Recall@1 and mAP indicate better performance in object retrieval and question answering tasks.

**Baseline Results**: STML (previous method) performance serves as a baseline for evaluation against the proposed MS-GCEL method.

**Validation**: Cross-validation performed on various datasets to assess the generalization capability of the MS-GCEL model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
