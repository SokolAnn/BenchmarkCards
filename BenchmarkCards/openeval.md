# OpenEval

## 📊 Benchmark Details

**Name**: OpenEval

**Overview**: OpenEval is an evaluation testbed that benchmarks Chinese LLMs across capability, alignment, and safety, addressing the gaps overlooked by existing benchmarks focused primarily on capabilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- M3KE
- CMMLU
- FlagEval

**Resources**:
- [Resource](http://openeval.org.cn/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation platform for Chinese LLMs, covering capability, alignment, and safety assessments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Commonsense Reasoning
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 25 benchmark datasets created specifically for evaluating Chinese LLMs.

**Size**: 300,000 questions

**Format**: JSON

**Annotation**: Datasets compiled from various sources and manually curated.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Each benchmark employs specific metrics suited to their tasks, measuring LLM performance accordingly.

**Interpretation**: High scores indicate better alignment with human values and performance on various NLP tasks.

**Validation**: Phased public evaluation and benchmark update strategy implemented.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
