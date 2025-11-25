# Token-by-Token Regeneration and Domain Biases: A Benchmark of LLMs on Advanced Mathematical Problem-Solving

## 📊 Benchmark Details

**Name**: Token-by-Token Regeneration and Domain Biases: A Benchmark of LLMs on Advanced Mathematical Problem-Solving

**Overview**: This study evaluates 10 language models on 945 competition-level mathematics problems, focusing on their ability to generate executable Python code. The findings reveal a performance gap between the most and least effective models, along with implications for using token-by-token regeneration in enhancing model outputs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH

**Resources**:
- [GitHub Repository](https://github.com/hendrycks/math)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark 10 LLMs on competition-level mathematics problems and identify performance gaps and areas for improvement.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: The MATH dataset, a publicly available collection of 12,500 competition-level mathematics problems.

**Size**: 945 problems

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Weighted accuracy

**Calculation**: Weighted accuracy calculated as the percentage of answers scoring 4 or 5 across the dataset.

**Interpretation**: Performance is assessed based on a 5-point scale for accuracy, where higher scores reflect better correctness.

**Baseline Results**: The gpt-4o-mini-2024-07-18 achieved an accuracy of 83.7% while open-codestral-mamba:v0.1 scored 49.2%.

**Validation**: The evaluation was conducted using a dedicated high-performance model for assessing response correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
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
