# PatternNetv2; RSICDv2; RESISC45v2; MLRSNetv2

## 📊 Benchmark Details

**Name**: PatternNetv2; RSICDv2; RESISC45v2; MLRSNetv2

**Overview**: Curated four remote sensing benchmarks and introduced experimental protocols and datasets for three domain generalization tasks (base-to-new class, cross-dataset, single-source multi-target) to evaluate few-shot optical remote sensing scene recognition and generalization using APPLeNet.

**Data Type**: image (optical remote sensing images)

**Domains**:
- Remote Sensing

**Similar Benchmarks**:
- PatternNet
- RSICD
- RESISC45
- MLRSNet

**Resources**:
- [GitHub Repository](https://github.com/mainaksingha01/APPLeNet)
- [Resource](https://arxiv.org/abs/2304.05995)

## 🎯 Purpose and Intended Users

**Goal**: Provide evaluation protocols and curated dataset versions to study few-shot optical remote sensing scene recognition and domain generalization (base-to-new class, cross-dataset, single-source multi-target).

**Target Audience**:
- Researchers in Remote Sensing and Computer Vision

**Tasks**:
- Few-shot Image Classification
- Base-to-New Class Generalization
- Cross-Dataset Generalization
- Single-Source Multi-Target Domain Generalization

**Limitations**: N/A

## 💾 Data

**Source**: PatternNet, RSICD, RESISC45, and MLRSNet; curated v2 versions (PatternNetv2, RSICDv2, RESISC45v2, MLRSNetv2) using the 16 overlapping classes for the single-source multi-target setup (as stated, details in supplementary).

**Size**: PatternNet: 38 classes, each class containing 800 images (256 x 256 pixels). RSICD: 30 classes, a total of 10,000 images (224 x 224 pixels). RESISC45: 45 classes, each class containing 700 images (256 x 256 pixels). MLRSNet: 46 classes, a total of 109,161 images (256 x 256 pixels). v2 datasets: curated versions with 16 overlapping classes (number of images per v2 not specified).

**Format**: N/A

**Annotation**: Class labels as provided by the original datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Few-shot evaluation (k-shot protocol)
- Zero-shot / cross-dataset evaluation
- Ablation studies

**Metrics**:
- Top-1 Accuracy
- Accuracy
- Harmonic mean (H) of base and new class accuracies

**Calculation**: Report average Top-1 accuracy across three seeds. Harmonic mean (H) computed between the classification accuracies of the Base and New classes for base-to-new experiments. Cross-dataset and single-source multi-target evaluations use accuracy as reported in tables.

**Interpretation**: Higher Top-1 Accuracy and higher Harmonic mean indicate better overall classification performance and better trade-off between base and new classes (H denotes harmonic mean used to generalize the trade-off performance between the base and new classes).

**Baseline Results**: Selected results reported in the paper: Base-to-New average harmonic mean: CLIP 56.63, CoOp 68.85, CoCoOp 69.88, ProGrad 69.70, APPLeNet 72.56. Cross-dataset (PatternNet as source) accuracies: APPLeNet PatternNet 88.17, RSICD 44.87, RESISC45 50.97, MLRSNet 46.83 (Table 2). Single-source multi-target (PatternNetv2 as source) accuracies: APPLeNet 96.63 (PatternNetv2), 81.03 (RSICDv2), 82.23 (RESISC45v2), 74.03 (MLRSNetv2) (Table 3).

**Validation**: Experiments run with three random seeds and report average Top-1 accuracy. For base-to-new, datasets are randomly and equally divided into source (base classes) and target (novel classes) as stated. Few-shot shots varied (1,4,8,16,32) for sensitivity analysis. Supplementary material contains additional dataset split details.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
