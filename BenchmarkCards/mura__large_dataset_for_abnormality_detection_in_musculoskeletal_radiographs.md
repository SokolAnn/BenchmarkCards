# MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs

## 📊 Benchmark Details

**Name**: MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs

**Overview**: We introduce MURA, a large dataset of musculoskeletal radiographs containing 40,561 images from 14,863 studies, where each study is manually labeled by radiologists as either normal or abnormal. To evaluate models robustly and to get an estimate of radiologist performance, we collect additional labels from six board-certified Stanford radiologists on the test set, consisting of 207 musculoskeletal studies. We train a 169-layer DenseNet baseline model to detect and localize abnormalities. To encourage advances, we have made our dataset freely available.

**Data Type**: image (multi-view radiographic images)

**Domains**:
- Medical Imaging
- Healthcare

**Similar Benchmarks**:
- Pediatric Bone Age (AIMI)
- 0.E.1 (OAI)
- Digital Hand Atlas
- ChestX-ray14
- OpenI
- MC
- Shenzhen
- JSRT
- DDSM

**Resources**:
- [Resource](http://stanfordmlgroup.github.io/competitions/mura)
- [Resource](https://arxiv.org/abs/1712.06957)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large, publicly available dataset of upper-extremity musculoskeletal radiographs labeled as normal or abnormal to facilitate development and robust evaluation of models for abnormality detection and localization in radiographs.

**Target Audience**:
- Machine Learning Researchers
- Medical Imaging Researchers
- Radiologists
- Model Developers

**Tasks**:
- Binary Classification
- Abnormality Detection
- Abnormality Localization

**Limitations**: N/A

## 💾 Data

**Source**: De-identified, HIPAA-compliant images collected from the Picture Archive and Communication System (PACS) of Stanford Hospital; images originate from clinical radiographic interpretations between 2001 and 2012 and were labeled by board-certified radiologists at the time of clinical interpretation.

**Size**: 40,561 images; 14,863 studies; 12,173 patients. Splits: training: 13,457 studies, 36,808 images; validation: 1,199 studies, 3,197 images; test: 207 studies, 556 images.

**Format**: DICOM images (variable resolutions and aspect ratios)

**Annotation**: Each study was manually labeled as normal or abnormal by board-certified radiologists during clinical interpretation. Additionally, six board-certified Stanford radiologists provided labels on the test set (207 studies); for the test set a gold standard was defined as the majority vote of a disjoint group of three radiologists. A manual review of 100 abnormal studies was performed to label abnormality findings (fracture, hardware, degenerative joint disease, other).

## 🔬 Methodology

**Methods**:
- Automated metrics (AUROC, ROC curve)
- Radiologist manual labeling and majority-vote gold standard
- Statistical comparison using Cohen's kappa
- ROC analysis with sensitivity and specificity

**Metrics**:
- Area Under the Receiver Operating Characteristic Curve (AUROC)
- Sensitivity
- Specificity
- Cohen's kappa statistic
- 95% confidence interval

**Calculation**: Per-view probabilities are predicted by a 169-layer DenseNet and averaged (arithmetic mean) to obtain a study-level probability. A study is predicted abnormal if the study-level probability > 0.5. AUROC is computed by varying classification thresholds. Cohen's kappa is computed as agreement of each radiologist/model with the gold standard (majority vote of three radiologists). 95% confidence intervals for kappa use the standard error of kappa (McHugh, 2012).

**Interpretation**: Higher AUROC, sensitivity, specificity, and Cohen's kappa indicate better detection performance. The paper reports that model performance is comparable to the best radiologist on finger and wrist studies, but lower than the best radiologist on elbow, forearm, hand, humerus, and shoulder studies. Overall the model's performance was lower than radiologists' performance on this task as reported.

**Baseline Results**: Model AUROC: 0.929. At threshold 0.5: sensitivity 0.815 and specificity 0.887. Overall Cohen's kappa for model: 0.705 (95% CI 0.700, 0.710). Per-study-type Cohen's kappa values are reported in Table 2 of the paper (e.g., Finger kappa 0.389 (95% CI 0.332, 0.446); Wrist kappa 0.931 (95% CI 0.922, 0.940)).

**Validation**: Collected additional labels from six board-certified radiologists on the test set of 207 studies. A gold standard was formed by majority vote of a randomly chosen group of three radiologists; the other three radiologists were used to estimate radiologist performance. There is no patient overlap between training, validation, and test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Data privacy rights alignment

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset consists of de-identified, HIPAA-compliant images; data collection was approved by the institutional review board.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Institutional Review Board approval obtained; images are de-identified and described as HIPAA-compliant.
