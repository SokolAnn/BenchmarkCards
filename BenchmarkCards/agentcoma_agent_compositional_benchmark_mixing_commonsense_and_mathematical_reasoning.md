# AgentCoMa (Agent Compositional Benchmark Mixing Commonsense and Mathematical Reasoning)

## 📊 Benchmark Details

**Name**: AgentCoMa (Agent Compositional Benchmark Mixing Commonsense and Mathematical Reasoning)

**Overview**: AgentCoMa is a compositional benchmark that requires both commonsense and mathematical reasoning to solve real-world tasks, aimed at evaluating large language models (LLMs) in mixed reasoning scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Bamboogle
- MultiArith

**Resources**:
- [Resource](https://agentcoma.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the ability of LLMs to combine different types of reasoning (commonsense and mathematical) in agentic settings.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark is constrained to questions requiring exactly two reasoning steps, with a fixed order of commonsense preceding mathematical reasoning.

## 💾 Data

**Source**: Expert-created questions and validations by postgraduate-level annotators.

**Size**: 260 samples

**Format**: JSON

**Annotation**: Manually annotated by experts without using LLMs or automated processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the correctness of answers to compositional tasks versus individual reasoning steps.

**Interpretation**: Performance gap is observed between individual reasoning steps and overall compositional accuracy.

**Validation**: Data samples undergo a multi-step validation process including binary yes/no questionnaire and expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
