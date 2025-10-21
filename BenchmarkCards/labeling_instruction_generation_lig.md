# Labeling Instruction Generation (LIG)

## 📊 Benchmark Details

**Name**: Labeling Instruction Generation (LIG)

**Overview**: We introduce a new task, Labeling Instruction Generation, to address missing publicly available labeling instructions. In Labeling Instruction Generation, we take a reasonably annotated dataset and: 1) generate a set of examples that are visually representative of each category in the dataset; 2) provide a text label that corresponds to each of the examples. We introduce a framework that requires no model training ... This framework acts as a proxy to human annotators that can help to both generate a final labeling instruction set and evaluate its quality.

**Data Type**: image-text pairs (visual examples plus text descriptions / instruction pairs)

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- COCO
- NuImages
- ADE20K
- OpenImages
- ImageNet

**Resources**:
- [Resource](https://arxiv.org/abs/2306.14035)
- [GitHub Repository](https://github.com/openimages)

## 🎯 Purpose and Intended Users

**Goal**: Generate multi-modal labeling instructions (visual examples plus text) for existing datasets that lack labeling instructions in order to increase dataset transparency, reproducibility, and utility.

**Target Audience**:
- Dataset curators
- Annotators
- Machine Learning Researchers
- Dataset Developers
- Policy makers

**Tasks**:
- Labeling Instruction Generation
- Image Retrieval
- Dataset Annotation (annotation guidance)

**Limitations**: Framework focuses on generating text and image pairs only; generated text instructions may sometimes be less nuanced and/or detailed compared to human generated text; current implementation does not include negative examples.

## 💾 Data

**Source**: Existing annotated datasets (NuImages and COCO): images with categorical labels and bounding boxes as provided by the original datasets.

**Size**: NuImages: 83,724 images and 25 classes; NuImages database index built with approximately 14 million visual embeddings. COCO: evaluated across 80 classes (per-paper reporting).

**Format**: FAISS on-disk index of visual embeddings produced by a pre-trained vision-language model; image patches (grid patches) extracted from images; original dataset bounding box annotations retained.

**Annotation**: Annotated with class bounding boxes (as provided by the original datasets).

## 🔬 Methodology

**Methods**:
- Automated evaluation via image-retrieval (held-out test set)
- Human evaluation (forced-choice between instruction sets)
- 5-fold training/testing (cross-validation) for evaluation stability

**Metrics**:
- Precision
- Recall
- Average Precision (AP)
- mean Average Precision (mAP)
- Area Under Precision-Recall Curve (AUC)

**Calculation**: For retrieval evaluation, the system returns the top 1000 unique retrievals per category; APs and mAPs are calculated from exactly 1,000 returns and averaged across 5 folds. During greedy search, candidate pairs are scored by AUC of precision-recall curves computed on top-k retrieved images.

**Interpretation**: Higher AUC/AP/mAP indicates better retrieval performance and thus better labeling instructions. Precision at lower k values is emphasized as more important because the most immediate retrieved images are accessed first.

**Baseline Results**: NuImages: PDC mAP = 15.44 versus Original Texts mAP = 8.77 (PDC outperforms strongest baseline by 7.06 mAP). COCO subset: PDC mAP = 54.9 versus Original Texts mAP = 42.0 (PDC outperforms strongest baseline by 12.9 mAP). Human study: across 23 NuImages categories and N=9 participants, participants preferred PDC generated instructions over original instructions 44% of the time.

**Validation**: 5-fold splits with non-overlapping train/test sets used for quantitative evaluation; human behavioral forced-choice experiment with 9 participants across 23 NuImages categories for qualitative validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Transparency
- Fairness
- Data Laws
- Governance
- Societal Impact

**Atlas Risks**:
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias
- **Data Laws**: Data usage restrictions
- **Governance**: Lack of data transparency
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Bias in medical imaging and framing biases that can have real-world consequences (explicitly discussed as an application area where instructions influence labels)', 'Reduced dataset transparency and reproducibility when labeling instructions are not available']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Paper explicitly mentions EU privacy laws such as GDPR and notes policy concerns around data bias and transparency; no specific compliance procedures are described.
