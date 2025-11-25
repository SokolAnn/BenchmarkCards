# CITB (Continual Instruction Tuning Benchmark)

## 📊 Benchmark Details

**Name**: CITB (Continual Instruction Tuning Benchmark)

**Overview**: CITB is a benchmark suite that establishes learning and evaluation protocols for the problem of Continual Instruction Tuning (CIT), including two long task streams to systematically study various continual learning methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hyintell/CITB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for continual instruction tuning and facilitate research in various continual learning methods.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering
- Dialogue Generation

**Limitations**: The experiments are conducted only with T5-small and tasks are limited to English from the SuperNI dataset.

## 💾 Data

**Source**: SuperNI dataset

**Size**: 756 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE-L
- Average ROUGE-L (AR)
- Final ROUGE-L (FR)
- Forward Transfer (FWT)
- Backward Transfer (BWT)

**Calculation**: Metrics are calculated based on model performance across different tasks after continual learning.

**Interpretation**: Performance is evaluated based on the ability to retain knowledge of previous tasks while effectively learning new tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
