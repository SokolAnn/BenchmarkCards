# AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field

## 📊 Benchmark Details

**Name**: AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field

**Overview**: AECBench is a comprehensive benchmark designed to quantify the strengths and limitations of current large language models (LLMs) in the Architecture, Engineering, and Construction (AEC) domain. It features a five-level, cognition-oriented evaluation framework with 23 representative evaluation tasks derived from authentic AEC practice.

**Data Type**: question-answering pairs

**Domains**:
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

**Goal**: To establish a standardized evaluation benchmark for assessing the knowledge capabilities of LLMs specific to the AEC domain, providing a rigorous and reliable means for practitioners and researchers to evaluate and improve LLMs.

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

**Source**: Curated by domain engineers based on building codes, proprietary documents, and licensure examinations.

**Size**: 4,800 questions

**Format**: N/A

**Annotation**: Crafted primarily by engineers and validated through a two-round expert review.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-as-a-Judge

**Metrics**:
- Accuracy
- F1 Score
- Kendall's tau

**Calculation**: Evaluation metrics for multiple-choice questions, classification tasks, and automated scoring of open-ended responses.

**Interpretation**: A decline in performance is observed across tasks as cognitive complexity increases.

**Validation**: Tasks were validated through comprehensive reviews by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
