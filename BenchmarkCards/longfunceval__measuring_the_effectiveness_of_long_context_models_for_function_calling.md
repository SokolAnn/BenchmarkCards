# LongFuncEval: Measuring the effectiveness of long context models for function calling

## 📊 Benchmark Details

**Name**: LongFuncEval: Measuring the effectiveness of long context models for function calling

**Overview**: This paper investigates the long context understanding capabilities of large language models (LLMs) in tool calling scenarios, identifying three key challenges: large tool catalog, long tool responses, and long multi-turn conversations. A new evaluation dataset is created to assess the models' performance on these challenges.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BFCL
- ComplexFuncBench

**Resources**:
- [GitHub Repository](https://github.com/ShishirPatil/gorilla)

## 🎯 Purpose and Intended Users

**Goal**: To study the challenges in long context tool calling and evaluate the performance of LLMs on these tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Modified existing benchmarks, new evaluation set created for long tool responses.

**Size**: 566 samples

**Format**: JSON

**Annotation**: Manual annotation based on tool API responses and created question templates.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- AST accuracy

**Calculation**: Calculated based on the performance of models in handling long context tool calling scenarios.

**Interpretation**: Model performance is assessed on a scale of AST accuracy as it varies with different context lengths and complexities.

**Validation**: Comparative analysis with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
