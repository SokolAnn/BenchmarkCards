# FinDABench

## 📊 Benchmark Details

**Name**: FinDABench

**Overview**: FinDABench is a comprehensive benchmark designed to evaluate the financial data analysis capabilities of Large Language Models (LLMs) within the context of financial data analysis, organized around three core competencies: Foundational Ability, Reasoning Ability, and Technical Skill.

**Data Type**: text

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- BBT-CFLEB
- FinEval
- PIXIU
- SuperCLUE-Fin

**Resources**:
- [GitHub Repository](https://github.com/cubenlp/BIBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a measure for in-depth analysis of LLM abilities in financial data analysis and to foster the advancement of LLMs in this field.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Financial Analysts

**Tasks**:
- Numerical Reasoning QA
- Early Warning Analysis
- Fin-report Fraud Detection
- Fin-report to Markdown
- Data to Insight
- NL2ViSQL

**Limitations**: N/A

## 💾 Data

**Source**: Real Scenarios

**Size**: 2,400 instances

**Format**: N/A

**Annotation**: Manually checked and annotated with expert guidance to ensure accuracy in financial contexts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- EM (Exact Match)
- Rouge

**Calculation**: Metrics are calculated based on model predictions compared to gold standard answers.

**Interpretation**: Higher scores indicate better performance in understanding and analyzing financial data.

**Baseline Results**: GPT-4 achieves a score of 32.37% total result in zero-shot settings.

**Validation**: Examined via a comprehensive assessment of 41 different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
