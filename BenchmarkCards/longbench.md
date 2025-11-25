# -LongBench

## 📊 Benchmark Details

**Name**: -LongBench

**Overview**:  -LongBench introduces a length-controllable long-context benchmark and a novel metric, LongScore, to evaluate long-context capabilities of LLMs by disentangling baseline ability from long-context performance. It aims to provide a more accurate assessment of LLMs' true ability to handle extended contexts.

**Data Type**: length-controllable long-context tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LongBench
- L-Eval
- NIAH
- RULER
- Ada-LEval
- Helmet

**Resources**:
- [GitHub Repository](https://github.com/uservan/100-LongBench.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust platform for evaluating and comparing LLMs across varying context lengths, minimizing the influence of prior knowledge or base abilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Key Retrieval
- Information Retrieval
- Single-doc QA
- Multi-doc QA
- Information Comprehension
- Information Summarization

**Limitations**: The proposed metric requires models to demonstrate relatively strong base ability on the task, which can cause performance evaluation fluctuations if the base ability is insufficient.

## 💾 Data

**Source**: Constructed from a combination of real and synthetic tasks to evaluate long-context capabilities.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Experimental evaluation across various models
- LongScore evaluation metric

**Metrics**:
- Accuracy
- LongScore

**Calculation**: LongScore separates Base Ability from long-context capability, allowing for a more accurate evaluation.

**Interpretation**: Higher LongScore indicates better long-context capability regardless of base ability.

**Baseline Results**: N/A

**Validation**: Reliability and effectiveness of the benchmark validated through comprehensive experiments comparing various open-source models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
