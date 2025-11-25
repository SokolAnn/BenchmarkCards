# PingPong: A Benchmark for Role-Playing Language Models with User Emulation and Multi-Model Evaluation

## 📊 Benchmark Details

**Name**: PingPong: A Benchmark for Role-Playing Language Models with User Emulation and Multi-Model Evaluation

**Overview**: We introduce a benchmark for evaluating the role-playing capabilities of language models by leveraging different language models to simulate users in dynamic, multi-turn conversations and assess the resulting dialogues.

**Data Type**: dialogue exchanges

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian

**Similar Benchmarks**:
- EQ-bench
- RPBench-Auto

**Resources**:
- [GitHub Repository](https://github.com/ilyagusev/ping_pong_bench)
- [Resource](https://ilyagusev.github.io/ping_pong_bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust and dynamic evaluation framework for language models' role-playing capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Role-Playing Evaluation

**Limitations**: Sample size of 64 conversations per model may limit statistical robustness.

## 💾 Data

**Source**: Conversations evaluated include character scenarios drawn from various media, designed for role-playing interactions.

**Size**: 64 conversations per model evaluated

**Format**: JSON

**Annotation**: Manual annotation by human evaluators with assessments on multiple criteria.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Character consistency
- Entertainment value
- Language fluency

**Calculation**: Spearman correlation used to compare model annotations with human evaluations.

**Interpretation**: Scores reflect model performance in role-playing contexts based on conversational quality.

**Validation**: Correlation with human annotations validated through manual evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: Efforts made to include diverse character and situation designs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only artificially generated conversations used, avoiding privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
