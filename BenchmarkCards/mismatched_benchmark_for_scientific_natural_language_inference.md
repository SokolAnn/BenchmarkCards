# MISMATCHED Benchmark for Scientific Natural Language Inference

## 📊 Benchmark Details

**Name**: MISMATCHED Benchmark for Scientific Natural Language Inference

**Overview**: The MISMATCHED benchmark introduces a new evaluation framework for scientific natural language inference (NLI) by covering non-computer science domains. It includes human annotated sentence pairs from psychology, engineering, and public health, serving as an out-of-domain test bed.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SCINLI
- MS CINLI

**Resources**:
- [GitHub Repository](https://github.com/fshaik8/MisMatched)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging benchmark for evaluating the robustness of scientific NLI models across non-CS domains.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Natural Language Inference

**Limitations**: Although the MISMATCHED benchmark enhances diversity in scientific NLI, many scientific domains (e.g., Physics, Chemistry) are not covered.

## 💾 Data

**Source**: Annotated research articles from non-CS domains, including psychology, engineering, and public health.

**Size**: 2,700 sentence pairs

**Format**: JSON

**Annotation**: Human annotated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1

**Calculation**: Macro F1 calculated based on the performance across all classes in the benchmark.

**Interpretation**: Higher Macro F1 indicates better performance in correctly identifying the semantic relationships.

**Baseline Results**: Best performing SLM baseline (SCIBERT) achieved a Macro F1 of 78.17%.

**Validation**: The benchmark was validated through human annotations for ensuring quality and consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The datasets include diverse scientific domains but do not cover all possible domains.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
