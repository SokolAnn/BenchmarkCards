# WAKEN LLM (Evaluating Reasoning Potential and Stability in LLMs via Fine-Grained Benchmarking)

## 📊 Benchmark Details

**Name**: WAKEN LLM (Evaluating Reasoning Potential and Stability in LLMs via Fine-Grained Benchmarking)

**Overview**: WAKEN LLM is a framework that quantifies the portion of 'Unknown' output attributable to model incapacity and evaluates whether stimulation can convert them into either correct answers or justified responses with valid reasoning.

**Data Type**: verifiable and unverifiable samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIG-Bench
- MMLU
- ScienceQA

**Resources**:
- [Resource](https://arxiv.org/abs/2507.16199)

## 🎯 Purpose and Intended Users

**Goal**: To explore the effects of the Vague Perception phenomenon on reasoning tasks and quantify the LLMs' reasoning potential.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: FLD, FOLIO, ScienceQA

**Size**: 2,840 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Overall Benchmark Converting Rate

**Calculation**: Metrics are calculated based on LLM's initial responses and the conversion rates after stimulation.

**Interpretation**: Increased conversion rates indicate improvement in LLM's reasoning abilities.

**Baseline Results**: N/A

**Validation**: Benchmark validation was done through comparative experiments on different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: FLD: MIT; FOLIO: research-only; ScienceQA: CC-BY-NC-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
