# MixEval

## 📊 Benchmark Details

**Name**: MixEval

**Overview**: MixEval is a new paradigm for establishing efficient, gold-standard large language model (LLM) evaluation by strategically mixing off-the-shelf benchmarks. It bridges comprehensive real-world user queries with efficient and fairly-graded ground-truth-based benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- MT-Bench
- Chatbot Arena

**Resources**:
- [Resource](https://mixeval.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient and effective benchmark for evaluating large language models (LLMs) that aligns closely with real-world user queries and preferences.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Web queries mined from Common Crawl and matched with existing benchmarks.

**Size**: 4,000 queries

**Format**: N/A

**Annotation**: Automatically filtered and categorized using open-source LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Correlation with human preferences

**Calculation**: Correlation is calculated between model scores and Chatbot Arena Elo scores.

**Interpretation**: Higher correlation indicates better agreement with human preferences.

**Baseline Results**: N/A

**Validation**: Stability tests show low standard deviation in model scores across versions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination, Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
