# Coreferenced Image Narratives (CIN)

## 📊 Benchmark Details

**Name**: Coreferenced Image Narratives (CIN)

**Overview**: Introduces CIN, a dataset for resolving coreferences in multimodal long-form image narrations. CIN augments the Localized Narratives subset with annotated coreference chains and links each chain to bounding boxes in the corresponding image. The dataset is provided for evaluation (annotations are not provided for training) and is accompanied by multiple baselines and analysis.

**Data Type**: image-text pairs (images with long-form narrations and bounding boxes linking coreference chains to image regions)

**Domains**:
- Natural Language Processing
- Computer Vision

**Similar Benchmarks**:
- Localized Narratives
- Flickr30k Entities
- RefCOCO
- Who’s Waldo
- NYU-RGBD v2
- SIMMC 2.0
- MPII-MD
- ReferItGame

**Resources**:
- [Resource](https://arxiv.org/abs/2211.14563)
- [Resource](https://labelstud.io/)
- [Resource](https://spacy.io/)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the task of resolving coreferences in multimodal long-form narrations and provide CIN, a dataset with coreference chain annotations and grounding (bounding boxes) to benchmark coreference resolution and narrative grounding in image narrations.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Multimodal Research Community

**Tasks**:
- Coreference Resolution
- Narrative Grounding
- Visual Grounding

**Limitations**: Annotations are provided only for evaluation and are not available for training; manual annotation is expensive; narrations are noisy and contain many first-person utterances which are filtered out during annotation.

## 💾 Data

**Source**: 1880 images from the Localized Narratives dataset (subset of Flickr30k) with long-form text descriptions (narrations) and mouse traces; annotations consist of mention marking, coreference chain identification and bounding boxes linking chains to image regions.

**Size**: 1880 images; 19,587 noun phrase mentions; 1,659 pronouns; 3,310 coreference chains; 21,246 bounding boxes; split: 1000 test images, 880 validation images.

**Format**: N/A

**Annotation**: Manual annotation using a Label Studio-based interface: annotators marked mentions, identified coreference chains (including singletons) and drew bounding boxes for chains/mentions. Six annotators were employed; 30 images were doubly annotated to compute inter-annotator agreement.

## 🔬 Methodology

**Methods**:
- Automated metrics (MUC, BLANC, IoU-based grounding accuracy)
- Baseline model comparisons (text-only CR baselines, visual grounding baselines, weakly-supervised grounding baselines)
- Ablation studies

**Metrics**:
- MUC F-measure
- BLANC Precision
- BLANC Recall
- BLANC F1
- Intersection over Union (IoU) thresholded at 0.5 (Grounding Accuracy)
- Percentage Accuracy for narrative grounding

**Calculation**: MUC F-measure counts coreference links (pairs of mentions) common to the predicted and ground-truth chains. BLANC measures precision and recall for coreferent and non-coreferent links and averages them. Narrative grounding considered correct if IoU between predicted and ground-truth box is > 0.5; any-box protocol used when multiple ground-truth boxes exist.

**Interpretation**: Higher MUC-F1 indicates better recovery of coreference links; BLANC also accounts for non-coreferent links (so BLANC can be relatively higher when many singletons/non-coreferent links are present); grounding accuracy is reported as percentage of mentions with IoU>0.5.

**Baseline Results**: Selected results on CIN: Rule-Based [29] MUC-F1 6.4, BLANC-F1 4.9; Neural-Coref [30] MUC-F1 0.13, BLANC-F1 3.23; Similarity-based MUC-F1 9.06, BLANC-F1 45.98; GLIP MUC-F1 0.12, BLANC-F1 31.66; MAFy MUC-F1 13.21, BLANC-F1 38.17; MAF++ MUC-F1 15.65, BLANC-F1 47.21. Ours (final model with mouse traces and regularizer): MUC-F1 19.19, BLANC-F1 48.53; Narrative grounding overall accuracy 29.36%.

**Validation**: Dataset split follows predefined split of Flickr30k: 1000 test, 880 validation. Inter-annotator agreement measured on 30 doubly annotated images: exact-match coreference chains 79.9%; bounding box IoU>0.6 agreement 81%. Models selected based on validation set performance.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
