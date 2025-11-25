# SUBSPEC (Substitute Speculative Decoding)

## 📊 Benchmark Details

**Name**: SUBSPEC (Substitute Speculative Decoding)

**Overview**: SUBSPEC is a novel lossless and training-free technique designed to maximize inference throughput for offloaded large language models (LLMs) on consumer-grade devices. It constructs highly aligned draft models to effectively mitigate the latency due to parameter offloading, enabling competitive inference speeds with substantial speedups.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EAGLE
- MT-Bench

**Resources**:
- [GitHub Repository](https://github.com/NYCU-EDgeAi/subspec)

## 🎯 Purpose and Intended Users

**Goal**: To accelerate inference of large language models on consumer GPUs with limited memory by proposing a new method for speculative decoding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Generation
- Code Generation
- Mathematical Reasoning
- Instruction Following
- Summarization

**Limitations**: The minimum GPU memory requirement is approximately 7.1GB for Qwen2.5 7B, which may restrict the model layers that can remain GPU-resident compared to alternative methods.

## 💾 Data

**Source**: Quantized substitute layers generated from offloaded target LLM portions and shared GPU layers.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Benchmarking across multiple generative tasks
- Asynchronous data transfer
- Chunked prefill for long contexts

**Metrics**:
- Throughput
- Average Acceptance Length (τ)

**Calculation**: For throughput, tokens per second are measured across various drafts and configurations.

**Interpretation**: Higher average acceptance lengths and throughput indicate better efficiency in LLM inference.

**Baseline Results**: SubSpec achieves up to 12.5× speedup compared to baseline offloading inference.

**Validation**: Empirical validation through extensive benchmarking with diverse models and tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
