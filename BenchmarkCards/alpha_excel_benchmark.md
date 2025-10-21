# Alpha Excel Benchmark

## 📊 Benchmark Details

**Name**: Alpha Excel Benchmark

**Overview**: This study presents a novel benchmark for evaluating Large Language Models (LLMs) using challenges derived from the Financial Modeling World Cup (FMWC) Excel competitions. The benchmark provides a standardized framework for assessing LLM capabilities in realistic business-oriented tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/reveondivad/certify/blob/main/excel_benchmark_with_answers_v14.json)

## 🎯 Purpose and Intended Users

**Goal**: To create a practical evaluation framework for measuring Large Language Models' capabilities on business-relevant tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Numerical Reasoning
- Pattern Recognition
- Problem-Solving
- Data Analysis

**Limitations**: The benchmark's translation from interactive spreadsheet challenges to text-based evaluations sacrifices elements of the original task environment.

## 💾 Data

**Source**: Challenges derived from historical FMWC competitions.

**Size**: 113 challenges

**Format**: JSON

**Annotation**: Challenges transformed into standardized JSON format for programmatic evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Models are scored based on the quality of their solutions with partial credit for multi-step problems.

**Interpretation**: The scoring system allocates points according to solution quality, reflecting correctness in multi-step problems.

**Baseline Results**: GPT-4o-mini demonstrated the highest overall performance.

**Validation**: The evaluation system maintains consistent environmental conditions across evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
