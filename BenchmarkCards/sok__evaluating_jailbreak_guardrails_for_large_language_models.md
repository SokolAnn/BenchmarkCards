# SoK: Evaluating Jailbreak Guardrails for Large Language Models

## 📊 Benchmark Details

**Name**: SoK: Evaluating Jailbreak Guardrails for Large Language Models

**Overview**: This paper provides a comprehensive analysis of jailbreak guardrails for large language models (LLMs), proposing a multi-dimensional taxonomy and a Security-Efficiency-Utility evaluation framework for assessing their effectiveness.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- JailbreakHub
- JailbreakBench
- SafeMTData
- MultiJail
- AlpacaEval
- OR-Bench

**Resources**:
- [GitHub Repository](https://github.com/xunguangwang/SoK4JailbreakGuardrails)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured foundation for understanding, developing, and deploying LLM jailbreak guardrails, guiding the principled advancement of security mechanisms in AI applications.

**Target Audience**:
- ML Researchers
- Practitioners
- Industry Professionals

**Tasks**:
- Jailbreak Guardrail Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Multiple datasets including JailbreakHub, JailbreakBench, SafeMTData, MultiJail, AlpacaEval, OR-Bench

**Size**: 3,300 prompts

**Format**: CSV

**Annotation**: Collected and categorized from diverse sources and user prompts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)
- Pass Guardrail Rate (PGR)
- Extra Delay
- GPU Memory Overhead
- False Positive Rate (FPR)

**Calculation**: Calculated based on performance against various jailbreak attacks using the defined metrics.

**Interpretation**: Lower ASR and FPR indicate better performance; trade-offs exist between security and efficiency.

**Baseline Results**: Comparison with popular jailbreak defense methods including Perplexity Filter, SmoothLLM, and GuardReasoner.

**Validation**: Extensive empirical evaluation against multiple benchmarks and guardrail methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Data poisoning
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
