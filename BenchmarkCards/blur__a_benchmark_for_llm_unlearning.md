# BLUR: A Benchmark for LLM Unlearning

## 📊 Benchmark Details

**Name**: BLUR: A Benchmark for LLM Unlearning

**Overview**: BLUR is a benchmark for LLM unlearning that provides realistic scenarios of forget-retain overlap, extended evaluation tasks, combined forget/retain queries, and relearning datasets of varying degrees of difficulty.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TOFU
- WMDP
- Who's Harry Potter

**Resources**:
- [Resource](https://huggingface.co/datasets/forgelab/BLUR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive suite of datasets to evaluate unlearning algorithms under challenging but realistic queries.

**Target Audience**:
- ML Researchers
- Safety Practitioners

**Tasks**:
- Machine Unlearning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Multiple datasets curated for unlearning evaluations, including TOFU, WMDP, and RWKU.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Forget Quality (ROUGE-L)
- Retain Quality (ROUGE-L)
- Perplexity

**Calculation**: Metrics are calculated based on comparison of base model answers and unlearned model answers using ROUGE-L recall scores.

**Interpretation**: Higher values for retain quality indicate better preservation of retain knowledge, while lower values for forget quality indicate better unlearning.

**Baseline Results**: N/A

**Validation**: Performance of existing unlearning methods evaluated across the new benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
