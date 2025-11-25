# ECRECer (Enzyme Commission Number Recommendation and Benchmarking)

## 📊 Benchmark Details

**Name**: ECRECer (Enzyme Commission Number Recommendation and Benchmarking)

**Overview**: ECRECer is a cloud platform for accurately predicting Enzyme Commission (EC) numbers based on novel deep learning techniques. It provides three standard datasets for benchmarking and evaluation in enzyme function annotation tasks.

**Data Type**: protein sequences

**Domains**:
- Biotechnology
- Bioinformatics

**Languages**:
- N/A

**Similar Benchmarks**:
- CatFam
- PRIAM
- ECPred
- DeepEC

**Resources**:
- [Resource](https://ecrecer.biodesign.ac.cn)
- [GitHub Repository](https://github.com/kingstdio/ECRECer/blob/main/document/supplementary.pdf)

## 🎯 Purpose and Intended Users

**Goal**: To improve the speed and accuracy of enzyme function annotation by predicting EC numbers for protein sequences.

**Target Audience**:
- Biologists
- Bioinformaticians
- Researchers in enzyme function prediction

**Tasks**:
- Enzyme or Non-enzyme Annotation
- Multifunctional Enzyme Prediction
- EC Number Prediction

**Limitations**: The performance of multifunctional enzyme annotation is relatively low, and the accuracy and recall of EC number annotation are less than 90%.

## 💾 Data

**Source**: Swiss-Prot database

**Size**: 469,134 protein sequences for training and 7,101 for testing

**Format**: FASTA

**Annotation**: Labeled with enzyme or non-enzyme, EC numbers, and function counts.

## 🔬 Methodology

**Methods**:
- Extreme Multi-label Classification
- K-Nearest Neighbors (KNN)
- XGBoost
- Scalable Linear Extreme Classifier (SLICE)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated using standard formulas for classification performance.

**Interpretation**: An accuracy score above 80% is considered high enough for enzyme function annotation tasks.

**Baseline Results**: The ECRECer platform achieved 93.12% accuracy for enzyme or non-enzyme prediction, improving upon the best-performing existing methods by significant margins.

**Validation**: Validated against multiple state-of-the-art methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
