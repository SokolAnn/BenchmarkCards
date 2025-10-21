# A Language-Guided Benchmark for Weakly Supervised Open Vocabulary Semantic Segmentation

## 📊 Benchmark Details

**Name**: A Language-Guided Benchmark for Weakly Supervised Open Vocabulary Semantic Segmentation

**Overview**: We propose a novel unified weakly supervised OVSS pipeline that can perform ZSS, FSS and Cross-dataset segmentation on novel classes without using pixel-level labels for either the base (seen) or the novel (unseen) classes in an inductive setting. We propose Weakly-Supervised Language-Guided Segmentation Network (WLSegNet), a novel language-guided segmentation pipeline that i) learns generalizable context vectors with batch aggregates (mean) to map class prompts to image features using frozen CLIP and ii) decouples weak ZSS/FSS into weak semantic segmentation and Zero-Shot segmentation.

**Data Type**: image (weakly labelled image-level labels; segmentation masks used as evaluation targets / pseudo-labels)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- PASCAL VOC
- MS COCO
- Pascal-5i
- COCO-20i

**Resources**:
- [Resource](https://arxiv.org/abs/2302.14163)
- [GitHub Repository](https://github.com/mustafa1728/WLSegNet)

## 🎯 Purpose and Intended Users

**Goal**: To define and evaluate a unified weakly supervised open-vocabulary semantic segmentation pipeline (WLSegNet) that performs Weak Zero-Shot Segmentation (WZSS), Weak Few-Shot Segmentation (WFSS), Generalized Weak Zero-Shot Segmentation (WGZSS) and Cross-dataset Segmentation in an inductive setting using only image-level labels and a frozen vision-language model.

**Target Audience**:
- ML Researchers
- Computer Vision Researchers
- Model Developers

**Tasks**:
- Open Vocabulary Semantic Segmentation
- Zero-Shot Segmentation
- Generalized Zero-Shot Segmentation
- Few-Shot Segmentation
- Weakly Supervised Semantic Segmentation
- Cross-dataset Segmentation

**Limitations**: Limitations like overfitting on seen classes and large computational requirements reported by existing prompt-based learning methods.

## 💾 Data

**Source**: PASCAL VOC 2012 and MS COCO 2014 datasets using Pascal-5i and COCO-20i splits. PASCAL VOC: standard Pascal-5i folds (20 classes with 4 folds, seen/unseen splits). MS COCO: COCO-20i splits (80 classes with 4 folds, 60 seen / 20 unseen).

**Size**: PASCAL VOC 2012: 11,185 training images and 1,449 validation images (20 semantic classes). MS COCO 2014: 82,081 training images and 40,137 validation images (80 semantic classes).

**Format**: N/A

**Annotation**: Image-level labels (weak labels). Pseudo-segmentation masks generated for training via a Pseudo-label Generation (PLG) module (L2G used as PLG; RCA also evaluated as alternative). Class-agnostic mask proposals generated (MaskFormer used in experiments).

## 🔬 Methodology

**Methods**:
- Automated metrics (mIOU and harmonic mIOU)
- Comparative benchmarking against baseline methods (pixel-supervised and weakly-supervised baselines)
- Ablation studies
- Qualitative analysis (visualization of predicted masks)

**Metrics**:
- Mean Intersection over Union (mIOU)
- harmonic mIOU
- seen mIOU
- unseen mIOU

**Calculation**: Evaluation metrics follow conventions used in prior work [56]. Results are reported as mIOU per fold and as seen/unseen/harmonic mIOU in tables. (The paper states metrics follow conventions in [56]; detailed formulae beyond table reporting are not provided in the text.)

**Interpretation**: Higher mIOU and harmonic mIOU indicate better segmentation performance. The paper compares absolute mIOU and harmonic mIOU values across methods and reports improvements in mIOU points over baselines.

**Baseline Results**: The paper reports that WLSegNet beats existing weakly supervised baselines by 39 and 3 mIOU points respectively for weak generalized Zero-Shot and weak Few-Shot semantic segmentation on PASCAL VOC, and beats weak Few-Shot semantic segmentation baselines by 5 mIOU points on MS COCO. In 2-way 1-shot weak FSS, WLSegNet outperforms baselines by 13 and 22 mIOU points on PASCAL VOC and MS COCO respectively. Detailed per-table numbers are reported in Tables 1-9 of the paper.

**Validation**: Validated via extensive experiments on PASCAL VOC (Pascal-5i splits) and MS COCO (COCO-20i splits) across multiple folds and settings (WZSS, WGZSS, WFSS, Cross-dataset), with ablation studies varying prompt strategies, mask proposal methods, CLIP backbones and pseudo-label generators; qualitative visualizations are also provided.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
