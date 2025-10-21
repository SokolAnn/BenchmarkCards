# WLASL-Lex2001

## 📊 Benchmark Details

**Name**: WLASL-Lex2001

**Overview**: We introduce the task of Phonological Property Recognition (PPR) and contribute WLASL-Lex2001, a large-scale, automatically constructed dataset of American Sign Language signs annotated with six different phonological properties, along with an analysis of dataset quality and an empirical study of baseline models.

**Data Type**: video (videos annotated with phonological property labels; extracted 3D and 2D skeleton keypoints)

**Domains**:
- Sign Language Processing
- Computer Vision
- Natural Language Processing

**Languages**:
- American Sign Language

**Similar Benchmarks**:
- WLASL
- ASL-Lex (ASL-Lex 1.0)
- WLASL2000

**Resources**:
- [Resource](https://arxiv.org/abs/2203.06096)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the task of Phonological Property Recognition (PPR) and provide WLASL-Lex2001, a large-scale automatically constructed dataset labelled with six phonological properties, analyse dataset quality, and provide empirical baselines.

**Target Audience**:
- Researchers in Sign Language Processing
- Computer Vision researchers
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Phonological Property Recognition (classification)
- Flexion classification
- Major location classification
- Minor location classification
- Movement classification
- Selected fingers classification
- Sign type classification

**Limitations**: Dataset follows a long-tailed distribution (class imbalance). Dataset is automatically constructed so may contain incorrectly assigned ground-truth labels or low quality input due to automated construction.

## 💾 Data

**Source**: Automatically constructed by cross-referencing WLASL2000 videos with ASL-Lex 1.0 phonological annotations; skeleton keypoints extracted with FrankMocap and HRNet.

**Size**: 10,017 videos; 800 glosses

**Format**: 3D keypoints (x,y,z) from FrankMocap; 2D keypoints (x,y) with confidence score from HRNet; videos (fixed-length 150 frames inputs used in experiments).

**Annotation**: Automatically annotated by mapping glosses in WLASL2000 to phonological properties from ASL-Lex 1.0 (ASL-Lex properties were originally coded by 3 ASL-versed people).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (training multiple deep learning models as baselines)
- Automated metrics

**Metrics**:
- Accuracy
- Class-balanced Accuracy
- Precision (micro and macro)
- Recall (micro and macro)
- Matthews correlation coefficient (MCC)

**Calculation**: Accuracy reported with 95% confidence intervals using asymptotic normal approximation. Matthews correlation coefficient (MCC) computed as MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)). Class-balanced accuracy computed to account for class imbalance. Model selection based on validation MCC.

**Interpretation**: Higher Accuracy indicates better general performance; Class-balanced Accuracy assesses per-class performance under class imbalance; MCC provides a trade-off between overall and class-level performance and was used for hyperparameter/model selection.

**Baseline Results**: Majority-class baselines and multiple model baselines reported. Best reported model: STGCN (using HRNet) achieves 84.12% ± 0.29 accuracy on the SIGNTYPE test set (mean ± std over 5 seeds). Detailed per-task results reported in Table 1 and additional metrics in Table 10.

**Validation**: For each phonological property: 70:15:15 train/validation/test splits stratified on the phonological label (Phoneme split). Additionally, gloss-level stratified splits (Gloss split) where glosses in validation/test do not appear in training to evaluate generalisation to unseen glosses. Model selection on validation set; final models trained on train+validation for test evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
