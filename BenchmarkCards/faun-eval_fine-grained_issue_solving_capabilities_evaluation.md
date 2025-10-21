# FAUN-Eval (Fine-grained Issue Solving Capabilities Evaluation)

## 📊 Benchmark Details

**Name**: FAUN-Eval (Fine-grained Issue Solving Capabilities Evaluation)

**Overview**: FAUN-Eval is a benchmark specifically designed to evaluate the Fine-grained Issue Solving capabilities of Large Language Models (LLMs) across three distinct tasks: Question Answering (QA), Fault Localization, and Code Editing.

**Data Type**: question-answering pairs

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- JavaScript
- TypeScript
- Go

**Similar Benchmarks**:
- SWE-Bench

**Resources**:
- [Resource](https://anonymous.4open.science/status/FAUN-Eval)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the atomic capabilities of LLMs in solving real-world GitHub issues in software engineering tasks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Question Answering
- Fault Localization
- Code Editing

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 30 well-known GitHub repositories with issue and pull request data.

**Size**: 300 entries

**Format**: JSON

**Annotation**: Data curated through cross-referencing and keyword verification methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual review

**Metrics**:
- Exact Match (EM)
- BLEU
- CodeBLEU
- ROUGE-L
- ROUGE-1
- Edit Similarity

**Calculation**: Metrics are calculated using the predictions from models compared against the ground truth.

**Interpretation**: Higher scores across metrics indicate better performance in the corresponding tasks.

**Validation**: Models evaluated against ground truth for accuracy in QA, fault localization, and code editing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
