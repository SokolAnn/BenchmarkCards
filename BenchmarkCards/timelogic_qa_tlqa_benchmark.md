# TimeLogic QA (TLQA) benchmark

## 📊 Benchmark Details

**Name**: TimeLogic QA (TLQA) benchmark

**Overview**: The TLQA benchmark is designed specifically to evaluate the temporal logical understanding capabilities of VideoQA models, providing a scalable framework to automatically generate QA pairs from existing video datasets with temporal annotations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- STAR
- AGQA
- Breakfast
- CrossTask

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the gap in evaluating temporal logical reasoning in VideoQA through a structured benchmarking approach.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Leveraging temporal annotations from existing video datasets like STAR, Breakfast, AGQA, and CrossTask.

**Size**: 32,000 question-answer pairs for TLQA-Small (TLQA-S) and 160,000 pairs for TLQA-Large (TLQA-L)

**Format**: N/A

**Annotation**: Automatically generated from existing annotations in video datasets.

## 🔬 Methodology

**Methods**:
- Zero-Shot evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated by comparing the model's responses with the ground truth answers.

**Interpretation**: Higher scores indicate better performance in temporal logical reasoning.

**Baseline Results**: Different models' performances on TLQA-S evaluated across various temporal operators and datasets.

**Validation**: Evaluation against established VideoQA models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
