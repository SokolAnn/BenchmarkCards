# Z EST (ZeroShot learning from Task descriptions)

## 📊 Benchmark Details

**Name**: Z EST (ZeroShot learning from Task descriptions)

**Overview**: Z EST provides a benchmark dataset for systematically measuring how well models can generalize to many tasks in the zero-shot setting.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://allenai.org/data/zest)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate how well models truly understand each task from natural language descriptions.

**Target Audience**:
- NLP Researchers
- Model Developers

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced via Mechanical Turk from various domains.

**Size**: 25,026 (task, input, answer) triples

**Format**: JSON

**Annotation**: Manual annotation by crowdsourced workers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Evaluation is based on F1 score derived from overlapping models' and gold answers.

**Interpretation**: Higher scores indicate better model performance in performing tasks.

**Baseline Results**: Best model (T5-11B with multitask learning) achieves 12% overall on C@90.

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
