# AirQA (A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation)

## 📊 Benchmark Details

**Name**: AirQA (A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation)

**Overview**: AirQA is a human-annotated multi-modal multi-task multi-paper QA dataset with function-based instance-specific evaluations, consisting of 13,948 papers and 1,246 questions, aimed at evaluating an agent's research capabilities in realistic scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- M3SciQA
- PeerQA
- LitQA2

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate question answering capabilities of models in the AI research domain through a comprehensive dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collection of papers primarily from arXiv and other academic sources.

**Size**: 13,948 papers

**Format**: JSON

**Annotation**: Human-annotated by AI students with expertise in the field.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Evaluation is based on the correctness of answers as judged by designed Python functions.

**Interpretation**: Scores reflect the correctness of model outputs compared to the correct answers.

**Baseline Results**: N/A

**Validation**: Evaluators use specific Python functions to assess model outputs against expected outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
