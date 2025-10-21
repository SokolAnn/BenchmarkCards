# DeepTumorVQA (Deep Tumor Visual Question Answering)

## 📊 Benchmark Details

**Name**: DeepTumorVQA (Deep Tumor Visual Question Answering)

**Overview**: DeepTumorVQA is a diagnostic visual question answering (VQA) benchmark targeting abdominal tumors in CT scans, comprising 9,262 CT volumes and 395K expert-level questions spanning four diagnostic categories.

**Data Type**: question-answer pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Schuture/DeepTumorVQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality and diagnostically meaningful benchmark for evaluating state-of-the-art models in realistic clinical contexts.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: The dataset construction may introduce noise from segmentation variability and is intended for research, not clinical deployment.

## 💾 Data

**Source**: 9,262 CT volumes gathered from 17 public datasets and 88 centers, annotated by 23 board-certified radiologists.

**Size**: 9,262 CT volumes, 3.7M slices, 395K question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation by board-certified radiologists.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Mean Relative Accuracy (MRA)

**Calculation**: Metrics are calculated using task-specific evaluations.

**Interpretation**: Higher accuracy indicates better model performance at answering clinical questions.

**Baseline Results**: N/A

**Validation**: Extensive benchmarking was conducted using four state-of-the-art vision-language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
