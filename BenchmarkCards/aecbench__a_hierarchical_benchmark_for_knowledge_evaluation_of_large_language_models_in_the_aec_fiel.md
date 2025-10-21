# AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field

## 📊 Benchmark Details

**Name**: AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field

**Overview**: AECBench is a comprehensive benchmark designed to quantify the strengths and limitations of large language models (LLMs) in the Architecture, Engineering, and Construction (AEC) domain. It features a five-level, cognition-oriented evaluation framework with 23 representative evaluation tasks derived from authentic AEC practice.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Architecture
- Engineering
- Construction

**Languages**:
- Chinese

**Similar Benchmarks**:
- LawBench
- PromptCBLUE
- FinEV AL

**Resources**:
- [GitHub Repository](https://github.com/open-compass/opencompass)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the proficiency of large language models in knowledge-intensive tasks across various cognitive levels in the AEC domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Knowledge Memorization
- Knowledge Understanding
- Knowledge Reasoning
- Knowledge Calculation
- Knowledge Application

**Limitations**: N/A

## 💾 Data

**Source**: Questions are curated from building codes, proprietary internal documents, and licensure examinations, crafted by domain engineers.

**Size**: 4,800 questions

**Format**: N/A

**Annotation**: Questions were validated through a two-round review mechanism involving mid-level engineers and domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the responses' correctness using expert-defined rubrics.

**Interpretation**: Scores indicate the model's ability to perform tasks across cognitive levels in the AEC domain.

**Baseline Results**: DeepSeek-R1 consistently placed among the best-performing models in AECBench.

**Validation**: Evaluated through a comprehensive comparison of LLM outputs against expert benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misapplication of generated models in critical AEC tasks.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
