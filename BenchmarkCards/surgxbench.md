# SurgXBench

## 📊 Benchmark Details

**Name**: SurgXBench

**Overview**: SurgXBench is the first VLM benchmarking framework for surgical tasks that integrates explainability, analyzing model attention and causal reasoning in surgical applications.

**Data Type**: image

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Rau et al. 2025

**Resources**:
- [Resource](https://arxiv.org/abs/2505.10764)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess the performance of vision-language models (VLMs) in surgical tasks, and to improve these models through explainability analysis.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Instrument Classification
- Triplet Recognition

**Limitations**: The benchmark is initially focused on instrument and action classification, while other important tasks in the surgical domain should be explored in the future.

## 💾 Data

**Source**: Cholec80BBox and CholecT45 datasets

**Size**: 51,700 frames for Cholec80BBox, 90,500 frames for CholecT45

**Format**: N/A

**Annotation**: Manually annotated with ground truth for instrument classification and triplet recognition.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Explainability analysis

**Metrics**:
- Precision
- Recall
- F1 Score
- Attention Alignment (AA)
- Attention Coverage (AC)
- RAFT Attention Score (RAS)

**Calculation**: Metrics are calculated based on true positives, false positives, and annotated regions using predicted attention heatmaps and standard evaluation metrics.

**Interpretation**: Performance is interpreted based on how well models align their attention with clinically relevant cues in surgical images.

**Validation**: Models are validated through attentional analysis and classification accuracy, comparing performance across general and surgical VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to prevent misclassification that may arise from misunderstanding the contextual cues in surgical images.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
