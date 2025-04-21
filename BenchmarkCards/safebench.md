# SafeBench

## 📊 Benchmark Details

**Name**: SafeBench

**Overview**: A comprehensive framework designed for conducting safety evaluations of multimodal large language models (MLLMs), addressing the limitations in existing safety evaluation benchmarks.

**Data Type**: Harmful query dataset, multimodal data

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- MM-SafetyBench
- JailbreakV-28K
- FigStep

**Resources**:
- [Resource](https://safebench-mm.github.io/)
- [Resource](https://huggingface.co/datasets/Zonghao2025/safebench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety of multimodal large language models and provide an up-to-date leaderboard on MLLM safety.

**Target Audience**:
- AI researchers
- Developers of machine learning models
- Safety evaluators

**Tasks**:
- Safety evaluation of MLLMs
- Dataset benchmarking
- Developing automated evaluation protocols

**Limitations**: Limited sample size may not fully capture the diversity of harmful queries.

**Out of Scope Uses**:
- Evaluation of extreme scenarios?
- Non-harmful use cases?

## 💾 Data

**Source**: Generated using a combination of LLM judges and surveys of existing guidelines.

**Size**: 2,300 harmful query pairs across 23 risk scenarios.

**Format**: Text, images, audio

**Annotation**: High-quality harmful queries generated and categorized by LLM judges.

## 🔬 Methodology

**Methods**:
- Jury deliberation evaluation protocol
- Automated dataset generation pipeline

**Metrics**:
- Attack Success Rate (ASR)
- Safety Risk Index (SRI)

**Calculation**: ASR is computed as the ratio of successful harmful responses to total queries. SRI is the aggregated threat response score normalized to a scale of 0 to 100.

**Interpretation**: Higher ASR indicates lower safety performance. Higher SRI indicates better safety performance.

**Baseline Results**: N/A

**Validation**: Conducted large-scale experiments on 15 open-source MLLMs and 6 commercial MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Medical Advice
- Legal Advice
- Investment Advice
- Personal Privacy
- Cybersecurity
- Hate Speech
- Violence
- Illegal Activities

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Potential generation of harmful outputs including misinformation, privacy violations, and incitement of violence.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is not collected; focuses on generated content safety.

**Data Licensing**: Datasets created from LLM outputs and public resources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Focuses on safety evaluation without violating ethical standards.
