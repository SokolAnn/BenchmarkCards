# PARALLEL PROMPT

## 📊 Benchmark Details

**Name**: PARALLEL PROMPT

**Overview**: PARALLEL PROMPT is the first benchmark for measuring intra-query parallelism in natural user prompts, comprising over 37,000 real-world prompts from public LLM chat logs, each annotated with a structured schema capturing task templates, shared context, and iteration inputs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Russian
- Japanese
- Spanish
- French

**Similar Benchmarks**:
- BIG-Bench
- GSM8K

**Resources**:
- [Resource](https://arxiv.org/abs/2506.18728)

## 🎯 Purpose and Intended Users

**Goal**: To study structure-aware execution in LLM serving pipelines and measure latency improvements.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Public LLM usage logs from WildChat-1M and LMSYS-chat-1M.

**Size**: 37,000 prompts

**Format**: JSON

**Annotation**: Annotated with structured schemas extracted using LLM-assisted prompting and rule-based multilingual validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Latency
- Semantic Fidelity
- Normalized Speedup

**Calculation**: Metrics are calculated based on execution time for both serial and parallel execution strategies.

**Interpretation**: Higher speedups indicate effective parallelization without significant quality loss.

**Baseline Results**: PARALLEL PROMPT: 3.91× speedup, 92% quality preservation; SoT: 2.04× speedup, 81% quality preservation; ToP: 1.73× speedup, 85% quality preservation.

**Validation**: A tiered validation framework ensures the quality and structural integrity of prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: WildChat-1M is under the Open Data Commons Attribution License, LMSYS-Chat-1M requires explicit permissions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
