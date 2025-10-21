# A Data-scalable Transformer for Medical Image Segmentation: Architecture, Model Efficiency, and Benchmark

## 📊 Benchmark Details

**Name**: A Data-scalable Transformer for Medical Image Segmentation: Architecture, Model Efficiency, and Benchmark

**Overview**: We present MedFormer, a data-scalable Transformer designed for generalizable 3D medical image segmentation. Our approach incorporates three key elements: a desirable inductive bias, hierarchical modeling with linear-complexity attention, and multi-scale feature fusion that integrates spatial and semantic information globally. MedFormer can learn across tiny- to large-scale data without pre-training. Comprehensive experiments demonstrate MedFormer’s potential as a versatile segmentation backbone, outperforming CNNs and vision Transformers on seven public datasets covering multiple modalities (e.g., CT and MRI) and various medical targets (e.g., healthy organs, diseased tissues, and tumors). We provide public access to our models and evaluation pipeline, offering solid baselines and unbiased comparisons to advance a wide range of downstream clinical applications.

**Data Type**: 3D medical image volumes (CT and MRI) with segmentation masks

**Domains**:
- Medical Image Analysis
- Healthcare

**Similar Benchmarks**:
- AMOS (Abdominal Multi-Organ Benchmark)
- LiTS (Liver Tumor Segmentation Challenge)
- KiTS
- Medical Segmentation Decathlon (MSD)
- ACDC
- BCV
- UK Biobank

**Resources**:
- [GitHub Repository](https://github.com/yhygao/CBIM-Medical-Image-Segmentation)
- [Resource](https://arxiv.org/abs/2203.00131)

## 🎯 Purpose and Intended Users

**Goal**: Develop MedFormer, a data-scalable Transformer for generalizable 3D medical image segmentation, and provide a comprehensive and unbiased benchmark and evaluation pipeline (codebase) for fair comparison of segmentation architectures.

**Target Audience**:
- Medical image analysis researchers
- Model developers
- Machine learning researchers

**Tasks**:
- 3D Medical Image Segmentation
- Semantic Segmentation

**Limitations**: The study is limited to supervised training and does not explore self-supervised or semi-supervised training or large-scale foundation model paradigms. The paper notes that transferring pre-trained weights from natural images to medical images can be sub-optimal due to domain gap.

## 💾 Data

**Source**: Collected large cardiac cine MRI dataset composed of UK Biobank, ACDC, M&Ms, and M&Ms-2 (used as a combined training dataset and M&Ms test set for evaluation) and seven public datasets used for generalization experiments: ACDC, BCV, LiTS, KiTS, AMOS CT, AMOS MR, MSD Lung.

**Size**: Collected cardiac dataset: 3,176 3D MR images (1,588 scans labeled in ED and ES phases = 3,176 3D images). Public datasets (as reported): ACDC 100 cases, BCV 30 training images, LiTS 131 training cases, KiTS 210 cases, AMOS CT 200 training scans (AMOS CT validation set used for reporting), AMOS MR 40 training scans, MSD Lung 63 CT scans.

**Format**: N/A

**Annotation**: Manual segmentation annotations (e.g., left ventricle (LV), right ventricle (RV), left ventricular myocardium (MYO) for cardiac datasets). BCV: labels manually created by two undergraduate students and verified by a radiologist. Other public datasets provide their respective segmentation annotations as described in their dataset releases.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Five-fold cross-validation on available training sets (unless otherwise noted)
- Consistent training and evaluation pipeline: re-implementation of all comparison models within the same framework and training procedures
- Out-of-distribution / robustness evaluation using M&Ms vendor domains (multi-vendor testing)

**Metrics**:
- Dice similarity coefficient (DSC)
- 95% Hausdorff Distance (95HD)
- Number of parameters
- FLOPs
- Inference time and GPU memory consumption

**Calculation**: DSC = 2 |P ∩ G| / (|P| + |G|). 95% Hausdorff Distance (95HD) measures the largest symmetrical distance between two segmentation maps with 95% percentile to reduce outlier influence. (Formulas provided in Appendix C of the paper.)

**Interpretation**: A DSC of 1 indicates a perfect segmentation while 0 indicates no overlap. Higher DSC indicates better overlap. Lower 95% Hausdorff Distance indicates better boundary agreement; 95% HD is used to reduce the impact of outliers.

**Baseline Results**: Reported baseline results include: On the collected large cardiac MRI dataset (Table 1) MedFormer DSC: 5%: 87.72, 10%: 87.99, 40%: 88.80, 70%: 88.92, 100%: 89.05. On seven public datasets (Table 2) MedFormer average DSC = 82.83; nnUNet average DSC = 81.05. Detailed per-dataset and per-model results are provided in Tables 1-3 and appendices.

**Validation**: Five-fold cross-validation on training sets for public datasets; M&Ms test set used as held-out test set for robustness evaluation across four vendor domains; AMOS reported on official validation set. The evaluation avoids ensembles, test-time augmentation, and post-processing to ensure fair comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Privacy
- Governance
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Governance**: Lack of testing diversity, Unrepresentative risk testing
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
