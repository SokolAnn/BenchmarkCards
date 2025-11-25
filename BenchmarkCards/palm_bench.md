# PALM BENCH

## 📊 Benchmark Details

**Name**: PALM BENCH

**Overview**: A comprehensive benchmark of compressed large language models on mobile platforms that focuses on evaluating resource efficiency, generative performance, and harmful outputs for compressed models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mlc-ai/mlc-llm)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of large language models on mobile devices, focusing on resource efficiency, power consumption, and harmful outputs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Various popular LLMs and existing benchmark datasets such as SQuAD and Natural Questions.

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically generated evaluations based on benchmark datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Profiling and monitoring

**Metrics**:
- Exact Match
- F1 Score
- Throughput (Tok/s)
- Power Consumption

**Calculation**: Metrics are calculated by comparing the performance of quantized models against their non-quantized counterparts.

**Interpretation**: Higher scores indicate better performance and lower resource usage.

**Baseline Results**: N/A

**Validation**: Automated evaluation from performance metrics collected during benchmarking.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: Evaluates the frequency of hallucinations and toxicity in generated outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
