# DABstep (Data Agent Benchmark for Multi-step Reasoning)

## 📊 Benchmark Details

**Name**: DABstep (Data Agent Benchmark for Multi-step Reasoning)

**Overview**: DABstep is a novel benchmark for evaluating AI agents on realistic multi-step data analysis tasks, comprising over 450 real-world challenges derived from a financial analytics platform, requiring models to combine code-based data processing with contextual reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinanceBench
- GAIA
- DABench

**Resources**:
- [Resource](https://huggingface.co/spaces/adyen/DABstep)
- [Resource](https://huggingface.co/datasets/adyen/dabstep)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of DABstep is to rigorously evaluate AI agents on realistic, multi-step data analysis tasks.

**Target Audience**:
- Machine Learning Researchers
- AI Developers
- Data Analysts

**Tasks**:
- Multi-step Reasoning
- Data Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Tasks are derived from operational workloads at Adyen, including real financial analytics tasks.

**Size**: 450 tasks

**Format**: CSV, JSON, Markdown

**Annotation**: Tasks were curated based on real internal queries, ensuring diverse data manipulation and contextual understanding.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Factoid evaluation

**Metrics**:
- Accuracy

**Calculation**: Tasks are scored based on a binary correctness evaluation of factoid answers.

**Interpretation**: High accuracy indicates capable multi-step reasoning and data manipulation abilities.

**Baseline Results**: Top models achieved 14.55% accuracy on Hard tasks.

**Validation**: Evaluation against a hidden test set to ensure robust generalization capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymized datasets have been used to ensure privacy.

**Data Licensing**: Creative Commons Attribution 4.0 International

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
