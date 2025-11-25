# PutnamGAP

## 📊 Benchmark Details

**Name**: PutnamGAP

**Overview**: PutnamGAP is a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems designed to evaluate the robustness of large language models (LLMs) in mathematical reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic method for assessing the robustness of LLMs' mathematical reasoning capabilities by stress-testing them on mathematically equivalent problems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: All Putnam Problems from 1938 to 2024

**Size**: 6,306 items

**Format**: LaTeX

**Annotation**: Manually validated with an automated grading system

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Robustness scores calculated using a normalized metric based on accuracy differences.

**Interpretation**: Higher robustness scores indicate better performance stability under variations of problem formulations.

**Baseline Results**: N/A

**Validation**: Statistical testing and inter-rater validation for scoring.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under a non-commercial licence

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
