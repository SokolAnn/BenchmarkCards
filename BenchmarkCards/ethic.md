# ETHIC

## 📊 Benchmark Details

**Name**: ETHIC

**Overview**: ETHIC is a novel benchmark designed to assess LLMs' ability to fully utilize provided context in long-context tasks. It emphasizes high information coverage and includes 1,986 test instances across four domains: books, debates, medicine, and law.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NIAH
- RULER
- Counting-Stars
- ZeroSCROLLS
- L-Eval
- InfiniteBench
- BAMBOO
- Loong
- LooGLE

**Resources**:
- [GitHub Repository](https://github.com/dmis-lab/ETHIC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' capabilities in fully utilizing long context in natural language processing tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Recalling
- Summarizing
- Organizing
- Attributing

**Limitations**: N/A

## 💾 Data

**Source**: Collected documents online from Project Gutenberg, Hansard, MSˆ2 dataset, and CourtListener.

**Size**: 1,986 instances

**Format**: N/A

**Annotation**: Manually reviewed and annotated using GPT-4o for accuracy.

## 🔬 Methodology

**Methods**:
- F1 Score
- Human evaluation
- LCS (Longest Common Subsequence)

**Metrics**:
- F1 Score
- Score (1-5)
- LCS (%)

**Calculation**: Metrics calculated based on comparison of model outputs with ground truth using specific evaluation criteria for each task.

**Interpretation**: Results indicate how well models performed based on F1 scores or specific task evaluations.

**Baseline Results**: Gemini Pro 1.5 (F1: 69.1% in Recalling), GPT-4o (F1: 49.5%)

**Validation**: Random sampling of annotations was performed to ensure label quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
