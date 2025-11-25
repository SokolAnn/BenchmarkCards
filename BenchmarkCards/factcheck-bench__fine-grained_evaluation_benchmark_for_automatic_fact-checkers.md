# Factcheck-Bench: Fine-Grained Evaluation Benchmark for Automatic Fact-checkers

## 📊 Benchmark Details

**Name**: Factcheck-Bench: Fine-Grained Evaluation Benchmark for Automatic Fact-checkers

**Overview**: Factcheck-Bench constructs an open-domain document-level factuality benchmark in three-level granularity: claim, sentence, and document, enabling evaluation of automatic fact-checking systems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FEVER
- HaluEval
- FELM

**Resources**:
- [GitHub Repository](https://github.com/yuxiaw/Factcheck-GPT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of automatic fact-checking systems in detecting and correcting factual errors in LLM outputs.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Fact-checking Systems Developers

**Tasks**:
- Fact-Checking
- Claim Correction
- Evidence Retrieval

**Limitations**: The dataset consists of only 94 instances and is focused on high-stakes factual errors.

## 💾 Data

**Source**: Annotated examples collected from hallucinations posted by ChatGPT users on Twitter and in-house brainstorming.

**Size**: 94 instances

**Format**: JSON

**Annotation**: In-house manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of the factuality of claims detected and corrected.

**Interpretation**: High F1 and accuracy scores indicate effective detection and correction of factual errors.

**Baseline Results**: The best F1 score for existing fact-checkers in preliminary experiments was F1=0.63.

**Validation**: Validated through in-house annotations ensuring high-quality factual verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
