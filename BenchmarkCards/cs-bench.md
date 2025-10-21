# CS-Bench

## 📊 Benchmark Details

**Name**: CS-Bench

**Overview**: CS-Bench is the first multilingual benchmark dedicated to evaluating the performance of large language models in computer science, comprising approximately 10,000 curated test samples covering 26 subfields across 4 key areas of computer science with varied task forms.

**Data Type**: question-answering pairs

**Domains**:
- Computer Science

**Languages**:
- English
- Chinese
- French
- German

**Similar Benchmarks**:
- MMLU
- C-Eval
- TruthfulQA

**Resources**:
- [Resource](https://csbench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically analyze the knowledge and reasoning capabilities of mainstream large language models in the field of computer science.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Assessment
- Reasoning Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Approximately 10,000 curated test samples collected from various computer science-related sources, including exams, blog articles, and authorized teaching materials.

**Size**: 10,000 examples

**Format**: N/A

**Annotation**: Manually labeled by a team with backgrounds in computer science.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers given by the models across various tasks.

**Interpretation**: Higher accuracy indicates better performance in addressing computer science-related questions.

**Baseline Results**: Baseline models include over 30 mainstream large language models evaluated on CS-Bench.

**Validation**: Tested using a random sampling of 10% of the data for validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
