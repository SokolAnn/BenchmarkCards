# HaluEval-Wild

## 📊 Benchmark Details

**Name**: HaluEval-Wild

**Overview**: HaluEval-Wild is designed to evaluate LLM hallucinations in real-world interactions using challenging user queries collected from ShareGPT.

**Data Type**: User Queries

**Domains**:
- General Domain: Real-World User Queries

**Similar Benchmarks**:
- HaluEval
- FACTOOL
- HaluEval-2.0
- Uhgeval

**Resources**:
- [GitHub Repository](https://github.com/HaluEval-Wild/HaluEval-Wild)

## 🎯 Purpose and Intended Users

**Goal**: Enhance understanding and improve LLM reliability in scenarios reflective of real-world interactions.

**Target Audience**:
- NLP researchers
- AI developers

**Tasks**:
- Evaluate hallucination rates of LLMs
- Improve model responses to challenging queries

**Limitations**: Focuses on challenging queries specifically designed to induce hallucinations may not fully encapsulate everyday user interactions.

## 💾 Data

**Source**: ShareGPT dataset

**Size**: 500 challenging user queries

**Format**: N/A

**Annotation**: Manually verified and categorized based on hallucination types.

## 🔬 Methodology

**Methods**:
- Query filtering
- Classification using Llama-2-7B model
- Retrieval-Augmented Generation (RAG)

**Metrics**:
- Hallucination rate
- Accuracy of query classification

**Calculation**: N/A

**Interpretation**: Evaluating LLM responses based on their consistency with reference answers.

**Validation**: Manual verification for classification accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination risks in language models

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Manual verification to exclude personally identifiable information (PII).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to ethical guidelines in data collection and dissemination.
