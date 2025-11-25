# PubLayNet

## 📊 Benchmark Details

**Name**: PubLayNet

**Overview**: We develop the PubLayNet dataset for document layout analysis by automatically matching the XML representations and the content of over 1 million PDF articles that are publicly available on PubMed Central™. The size of the dataset is comparable to established computer vision datasets, containing over 360 thousand document images, where typical document layout elements are annotated. The experiments demonstrate that deep neural networks trained on PubLayNet accurately recognize the layout of scientific articles. The pre-trained models are also a more effective base model for transfer learning on a different document domain. We release the dataset (https://github.com/ibm-aur-nlp/PubLayNet) to support development and evaluation of more advanced models for document layout analysis.

**Data Type**: image (PDF page images with bounding box annotations and instance segmentations)

**Domains**:
- Computer Vision
- Document Analysis

**Similar Benchmarks**:
- Medical Article Records Groundtruth (MARG)
- ICDAR datasets
- ENP image and ground truth dataset
- ICDAR 2013 Table Competition
- COCO
- ImageNet

**Resources**:
- [GitHub Repository](https://github.com/ibm-aur-nlp/PubLayNet)
- [Resource](https://arxiv.org/abs/1908.07836)

## 🎯 Purpose and Intended Users

**Goal**: Automatically generate a large dataset of article pages annotated with document layout components by exploiting paired PDF and XML representations in PubMed Central Open Access (PMCOA) to support development and evaluation of document layout analysis models and transfer learning.

**Target Audience**:
- Researchers
- Model developers

**Tasks**:
- Document Layout Analysis
- Object Detection
- Instance Segmentation
- Table Detection
- Transfer Learning

**Limitations**: The documents in PubLayNet are all scientific literature, which is domain specific and limits the heterogeneity of layout. PubLayNet does not contain relationships between the layout elements, e.g., a paragraph and a section title.

## 💾 Data

**Source**: PubMed Central Open Access (PMCOA) PDF and XML pairs; 1,162,856 articles with complete XML representation were downloaded from ftp.ncbi.nlm.nih.gov/pub/pmc on 3 October 2018 and automatically annotated.

**Size**: 364,232 pages total (340,391 training; 11,858 development; 11,983 testing); 3,571,250 annotated instances total (3,311,660 training; 127,815 development; 131,775 testing).

**Format**: N/A

**Annotation**: Automatically annotated by matching PDF elements parsed with PDFMiner to XML nodes from PMCOA using Unicode normalization and fuzzy string matching (Levenshtein-based). Bounding boxes generated for all categories; instance segmentations generated for text, title, and list from textlines; figure and table segmentations use bounding boxes. Quality control removed non-title pages with annotation quality < 99% and title pages with annotation quality < 90%.

## 🔬 Methodology

**Methods**:
- Automated evaluation using object detection models (Faster-RCNN, Mask-RCNN) implemented with Detectron
- Fine-tuning / transfer learning
- 5-fold cross-document-validation for SPD documents
- Human curation of development and testing sets

**Metrics**:
- Mean Average Precision (MAP) @ Intersection over Union (IoU) [0.50:0.95]
- Precision
- Recall
- F1 Score

**Calculation**: MAP calculated as mean average precision over IoU thresholds from 0.50 to 0.95 following the COCO detection evaluation protocol. Table detection evaluated with the official ICDAR 2013 evaluation toolkit to produce Precision, Recall, and F1-score.

**Interpretation**: High MAP (reported MAP > 0.9 on development and testing sets) indicates accurate layout detection. Models perform better on tables and figures than on text, titles, and lists. Titles are the most difficult category to detect.

**Baseline Results**: Faster-RCNN and Mask-RCNN trained on PubLayNet (ResNeXt-101-64x4d backbone) achieve on development set: macro average MAP F-RCNN 0.902, M-RCNN 0.910; on testing set: F-RCNN 0.900, M-RCNN 0.907. Per-category MAP on test (M-RCNN): Text 0.917, Title 0.828, List 0.887, Table 0.947, Figure 0.955. Fine-tuned table detection on ICDAR 2013: Image input F-RCNN Precision 0.972 Recall 0.964 F1 0.968; M-RCNN Precision 0.940 Recall 0.955 F1 0.947. Fine-tuning from PubLayNet outperforms ImageNet/COCO pre-training on SPD documents (5-fold cross-document-validation).

**Validation**: Data partitioned at journal level to maximize differences between training, development, and testing sets. Development and testing sets were curated by humans (profound erroneous pages removed and moderate erroneous pages corrected). For SPD domain adaptation, 5-fold cross-document-validation was used on 20 manually annotated SPD documents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: PMCOA provided under the Creative Commons license (PubMed Central Open Access).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
