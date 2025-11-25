# EngineMT-QA (Aero Engine Multi-Task Question Answering Dataset)

## 📊 Benchmark Details

**Name**: EngineMT-QA (Aero Engine Multi-Task Question Answering Dataset)

**Overview**: EngineMT-QA is a large-scale, multi-task, and temporal-textual QA dataset specifically designed for time-series data. It captures intricate interactions between time-series signals and natural language through questions and answers derived from real-world aero engine operational scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://pandalin98.github.io/itformer)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on bridging time-series data with natural language through a standardized dataset for evaluating Time-Series Question Answering methodologies.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed based on the N-CMAPSS aero engine dataset, reflecting real-world engine operation and maintenance scenarios through expert-designed question-answer pairs.

**Size**: 110,000 question-answer pairs

**Format**: N/A

**Annotation**: Expert-designed Q&A pairs linking sensor trends to internal engine conditions, ensuring alignment with field-specific principles.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are assessed based on the task-specific evaluation methodologies outlined for each QA task.

**Interpretation**: Performance is interpreted based on task-specific evaluation metrics with state-of-the-art results achieved by the proposed ITFormer framework.

**Baseline Results**: ITFormer-7B achieved the best performance across all tasks, with results including 58.04 in ROUGE-L for Understanding and 88.69 in F1 for Reasoning.

**Validation**: Validation processes include expert analysis to ensure the dataset's alignment with physical models governing engine performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
