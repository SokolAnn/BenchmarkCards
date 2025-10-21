# RepoQA: Evaluating Long Context Code Understanding

## 📊 Benchmark Details

**Name**: RepoQA: Evaluating Long Context Code Understanding

**Overview**: RepoQA is a benchmark to evaluate LLMs on long-context code understanding through the Searching Needle Function (SNF) task, which includes 500 code search tasks across 50 popular repositories in 5 programming languages.

**Data Type**: code search tasks

**Domains**:
- Computer Science

**Languages**:
- Python
- C++
- Java
- TypeScript
- Rust

**Similar Benchmarks**:
- Needle in a Haystack
- RepoBench
- Cross-CodeEval

**Resources**:
- [Resource](https://evalplus.github.io/repoqa.html)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively evaluate the long-context capabilities of LLMs when understanding code in real-world scenarios.

**Target Audience**:
- ML Researchers
- Software Developers
- Benchmark Designers

**Tasks**:
- Code Search

**Limitations**: N/A

## 💾 Data

**Source**: 500 code search tasks gathered from 50 popular code repositories.

**Size**: 500 tasks

**Format**: N/A

**Annotation**: Automatically annotated using GPT-4 for natural language descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the retrieval success rate of LLMs retrieving correct functions.

**Interpretation**: Models are compared based on their accuracy in retrieving relevant functions from the code context.

**Baseline Results**: Accuracy rates of various LLMs evaluated range from below 1% to over 90%, depending on the model and language.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
