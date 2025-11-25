# Q-resafe: Assessing Safety Risks and Quantization-aware Safety Patching

## 📊 Benchmark Details

**Name**: Q-resafe: Assessing Safety Risks and Quantization-aware Safety Patching

**Overview**: This paper presents a comprehensive safety evaluation of quantized large language models (LLMs) and introduces Q-resafe, a quantization-aware safety patching framework that efficiently restores the safety capabilities of quantized LLMs while minimizing the impact on utility.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://thecommonirin.github.io/Qresafe/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety risks associated with quantized LLMs and provide a framework for restoring their safety capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The datasets used include AdvBench for harmful instructions and Ultrachat for benign instructions.

**Size**: 520 harmful instructions and a large-scale dataset from UltraChat.

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Safety Evaluation
- Q-resafe Safety Patching

**Metrics**:
- Attack Success Rate (ASR)
- MT-Bench
- AlpacaEval

**Calculation**: Safety metrics were calculated based on established practices for full-precision LLMs.

**Interpretation**: Lower ASR values indicate better safety performance.

**Baseline Results**: Baseline models were Llama-2-7B-Chat and Gemma-7B-Instruct.

**Validation**: Safety evaluations were validated through systematic assessments using multiple quantization methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
