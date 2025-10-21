# Microsoft COCO: Common Objects in Context

## 📊 Benchmark Details

**Name**: Microsoft COCO: Common Objects in Context

**Overview**: A new large-scale dataset to advance object recognition in the context of scene understanding by gathering images of complex everyday scenes with per-instance segmentations. The dataset contains photos of 91 object types with a total of 2,500,000 labeled instances in 328,000 images and is intended to support detecting non-iconic views, contextual reasoning between objects, and precise 2D localization.

**Data Type**: image (per-instance segmentation masks, bounding boxes, image-level category labels, five written captions per image)

**Domains**:
- Computer Vision

**Similar Benchmarks**:
- ImageNet
- PASCAL VOC
- SUN

**Resources**:
- [Resource](http://mscoco.org/)
- [Resource](https://arxiv.org/abs/1405.0312)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale dataset for detecting and segmenting common objects in their natural context to drive research in non-iconic view detection, contextual reasoning between objects, and precise 2D localization (instance-level segmentation).

**Target Audience**:
- Computer Vision Researchers
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Object Detection
- Instance Segmentation
- Object Localization
- Image Captioning
- Scene Understanding

**Limitations**: Only 'thing' categories are labeled (no 'stuff' categories). The 2014 release is limited to a subset of 80 categories with segmentations for 80 categories (11 categories omitted in the 2014 segmentation release). Annotations for test data are not released; the evaluation server for automatic evaluation on the test set was still being finalized at the time of writing.

## 💾 Data

**Source**: Images collected primarily from Flickr using object-object and object-scene queries; annotations collected via Amazon Mechanical Turk (AMT) through hierarchical category labeling, instance spotting, instance segmentation, and segmentation verification.

**Size**: 2,500,000 labeled instances in 328,000 images. 2014 release: 82,783 training, 40,504 validation, 40,775 testing images. Cumulative 2015 release: 165,482 train, 81,208 val, 81,434 test images. 2014 train+val contains 886,000 segmented object instances and nearly 270,000 segmented people.

**Format**: N/A

**Annotation**: Per-instance segmentation masks, category presence labels (hierarchical labeling), instance spotting coordinates, bounding boxes derived from segmentation masks, segmentation verification (3-5 workers per segmentation), crowd labeling for dense instance groups, and five written captions per image. Annotation collection used AMT with 8 workers for labeling stages, training tasks for segmenters, and verification stages to accept/reject segmentations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation
- Baseline algorithm evaluation (Deformable Parts Model)

**Metrics**:
- Average Precision (AP) for detection
- Intersection over Union (IoU) for bounding boxes and segmentation overlap
- Performance drop (cross-dataset generalization) as proposed by Torralba and Efros

**Calculation**: A detection is considered correct if intersection over union (IoU) between predicted and ground truth bounding boxes is at least 0.5. Segmentation quality is measured as the IoU between predicted and ground truth segmentation masks, computed for correct detections. Average Precision (AP) is used for detection evaluation. Cross-dataset performance drop is computed as the difference in AP when training on one dataset and testing on another.

**Interpretation**: Higher Average Precision (AP) indicates better detection performance. Higher Intersection over Union (IoU) indicates better localization/segmentation quality. IoU >= 0.5 is used as the correctness threshold for detections. Larger cross-dataset performance drop indicates poorer generalization between datasets.

**Baseline Results**: Baseline evaluations using Deformable Parts Model variants (DPMv5-P trained on PASCAL VOC and DPMv5-C trained on MS COCO) are reported. The paper reports that average performance of DPMv5-P on MS COCO drops by nearly a factor of 2 compared to PASCAL VOC. The performance difference of the DPMv5-P models across the two datasets is 12.7 AP, while DPMv5-C models have a 7.7 AP difference.

**Validation**: Annotation validation steps include: union of multiple AMT workers for category labeling (8 workers used; recall analysis performed), training tasks for segmentation workers (workers required to pass segmentation training), segmentation verification where each segmentation is shown to 3 annotators and, if any annotator indicates poor quality, to 2 additional workers (segmentations not receiving at least 4/5 favorable votes are discarded), removal of near-duplicate images across splits, and grouping images by photographer and date to minimize near-duplicates.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
