# AGIBench: A Multi-granularity, Multimodal, Human-referenced, Auto-scoring Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: AGIBench: A Multi-granularity, Multimodal, Human-referenced, Auto-scoring Benchmark for Large Language Models

**Overview**: AGIBench is a multi-granularity, multimodal, human-referenced, and auto-scoring benchmarking methodology for evaluating large language models (LLMs), focusing on diverse question types and difficulty levels.

**Data Type**: multimodal question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- BIG-Bench
- HELM

**Resources**:
- [Resource](https://www.benchcouncil.org/agibench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the question-solving abilities and intelligence of LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions are primarily sourced from national civil service examinations.

**Size**: 927 questions

**Format**: N/A

**Annotation**: Questions are labeled with a four-tuple <ability branch, knowledge, difficulty, modal>.

## 🔬 Methodology

**Methods**:
- Auto-scoring methodology
- Heuristic regular expression searching

**Metrics**:
- Average accuracy
- Worst-case accuracy
- Best-case accuracy
- Majority voting accuracy
- Repeatability

**Calculation**: Metrics are calculated based on the accuracy of responses from multiple evaluations of the same questions.

**Interpretation**: Higher accuracy reflects better performance of LLMs in understanding and answering questions across various difficulties and modalities.

**Baseline Results**: N/A

**Validation**: Validation through experiments on twelve LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
