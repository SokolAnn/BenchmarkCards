# InductionBench

## 📊 Benchmark Details

**Name**: InductionBench

**Overview**: InductionBench is a new benchmark designed to evaluate the inductive reasoning ability of large language models (LLMs). It tests whether LLMs can infer a string-to-string transformation from a finite set of input-output pairs.

**Data Type**: input-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Wenyueh/inductive_reasoning_benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To assess the inductive reasoning capabilities of LLMs by testing their ability to hypothesize the underlying relationship between inputs and outputs from finite examples.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Inductive Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Functions derived from well-defined computational classes (ISL, L-OSL, R-OSL).

**Size**: 1,080 examples

**Format**: N/A

**Annotation**: Automated evaluation against known ground-truth functions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- Compatibility

**Calculation**: Metrics are calculated based on the comparison of predicted rules against the unique ground-truth rule set.

**Interpretation**: Higher scores indicate better performance in reproducing the intended transformations.

**Baseline Results**: N/A

**Validation**: Evaluated using state-of-the-art LLMs across various settings of k and size of input-output pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
