# STAKEOUT

## 📊 Benchmark Details

**Name**: STAKEOUT

**Overview**: STAKEOUT is a new benchmark composed of nine popular attack methods, three datasets, and two pre-trained models for robust evaluation of textual adversarial attack detection methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PierreColombo/AdversarialAttacksNLP)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a robust evaluation framework for adversarial attack detection methods in Natural Language Processing.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Adversarial Attack Detection
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark consists of three datasets: SST2, IMDB, and ag-news, used for sentiment analysis and topic classification.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Area Under the Receiver Operating Characteristic curve (AUROC)
- False Positive Rate (FPR)
- Area Under the Precision-Recall curve (AUPR)

**Calculation**: Metrics are calculated based on the detection performance of adversarial examples versus clean examples.

**Interpretation**: Higher AUROC indicates better overall performance. Lower FPR indicates fewer clean examples misclassified as adversarial.

**Baseline Results**: Baseline methods include detectors based on Mahalanobis distance and language model likelihood.

**Validation**: Extensive numerical experiments were conducted to assess the robustness of the detection methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
