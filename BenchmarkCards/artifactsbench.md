# ArtifactsBench

## 📊 Benchmark Details

**Name**: ArtifactsBench

**Overview**: ArtifactsBench is a benchmark for evaluating LLMs on interactive visual artifacts, emphasizing visual fidelity and interactive integrity. It includes 1,825 diverse tasks evaluated using a multimodal automated evaluation pipeline.

**Data Type**: executable queries

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- WebDev Arena
- HumanEval
- SWE-Bench
- WebBench
- WebGen-Bench

**Resources**:
- [Resource](https://artifactsbenchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and scalable evaluation framework for LLM-generated interactive visual artifacts.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Code Generation
- User Interaction Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Self-constructed queries based on expert sourcing and LLM generation.

**Size**: 1,825 examples

**Format**: N/A

**Annotation**: Checklist-guided evaluation using dual referees.

## 🔬 Methodology

**Methods**:
- Automated evaluation using MLLM referees
- Checklist-guided assessment
- Human evaluation for validation

**Metrics**:
- Ranking consistency with human preferences
- Pairwise agreement with human experts

**Calculation**: Evaluation scores are derived from checklist assessments and are validated against human rankings.

**Interpretation**: Higher scores indicate better performance in visual fidelity and interactive functionality.

**Baseline Results**: Achieved up to 94.4% ranking consistency with WebDev Arena.

**Validation**: Validated through a 280-instance expert study.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open source

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
