# CodeRepoQA: A Large-scale Benchmark for Software Engineering Question Answering

## 📊 Benchmark Details

**Name**: CodeRepoQA: A Large-scale Benchmark for Software Engineering Question Answering

**Overview**: CodeRepoQA is a large-scale benchmark specifically designed for evaluating repository-level question-answering capabilities in software engineering, comprising 585,687 entries across five programming languages.

**Data Type**: multi-turn question-answering pairs

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- CodeQA
- CS1QA
- CodeApex

**Resources**:
- [GitHub Repository](https://github.com/kinesiatricssxilm14/CodeRepoQA)

## 🎯 Purpose and Intended Users

**Goal**: To present a novel large-scale benchmark derived from conversations in GitHub repository issues for evaluating question-answering capabilities of language models.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from 30 well-known GitHub repositories containing software engineering issues.

**Size**: 585,687 entries

**Format**: N/A

**Annotation**: Filtered and cleaned data to ensure relevance and quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU
- ROUGE-L
- ROUGE-1
- Edit Similarity

**Calculation**: Metrics are calculated based on the comparison of generated responses to the ground truth.

**Interpretation**: Scores indicate the performance of LLMs in generating relevant answers.

**Baseline Results**: N/A

**Validation**: Evaluated using ten popular large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
