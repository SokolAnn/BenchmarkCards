# Project MPG (Model Performance and Goodness)

## 📊 Benchmark Details

**Name**: Project MPG (Model Performance and Goodness)

**Overview**: Project MPG introduces an aggregation approach to derive two primary metrics – 'Goodness' representing answer accuracy and 'Performance' reflecting queries per second (QPS) for evaluating large language models (LLMs), facilitating a unified metric for decision-making across various benchmarks.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- SQuAD
- BigBench

**Resources**:
- [GitHub Repository](https://github.com/sylinrl/TruthfulQA)
- [Resource](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux)
- [Resource](https://huggingface.co/datasets/tdiggelm/climate_fever)
- [Resource](https://huggingface.co/datasets/allenai/ai2_arc)
- [Resource](https://huggingface.co/datasets/boolq)
- [Resource](https://huggingface.co/datasets/rajpurkar/squad)
- [GitHub Repository](https://github.com/google/BIG-bench/tree/main/bigbench)
- [Resource](https://huggingface.co/datasets/EdinburghNLP/xsum)
- [Resource](https://huggingface.co/datasets/cais/mmlu)

## 🎯 Purpose and Intended Users

**Goal**: Provide a lightweight evaluation approach for resource-constrained developers to select models that align with their requirements for quality and latency, allowing for efficient comparison of LLM capabilities.

**Target Audience**:
- ML Researchers
- Engineers at smaller companies
- University researchers

**Tasks**:
- Factual Recall
- Linguistic Capability and Social Understanding
- Problem Solving

**Limitations**: Any attempt to aggregate many capabilities into a single number will create problems, such as assuming different measures within a sub-domain reflect the same underlying construct.

## 💾 Data

**Source**: Various existing LLM benchmarks including MMLU, SQuAD, BigBench, and Climate-FEVER.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Bayesian posterior sampling
- Aggregate scoring

**Metrics**:
- Goodness score
- Performance score

**Calculation**: Scores are computed using beta distributions of observed data from benchmarks combined with a binomial likelihood function.

**Interpretation**: Higher scores indicate better model capabilities across evaluated benchmarks.

**Baseline Results**: N/A

**Validation**: Correlations with existing benchmarks such as MMLU and Chatbot Arena validate model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
