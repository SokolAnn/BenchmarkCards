# WorldView-Bench

## 📊 Benchmark Details

**Name**: WorldView-Bench

**Overview**: WorldView-Bench is a benchmark designed to evaluate Global Cultural Inclusivity (GCI) in Large Language Models (LLMs) by analyzing their ability to accommodate diverse worldviews through free-form generative evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- HELM
- MT-Bench
- BLEND
- NORMAD

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://arxiv.org/abs/2505.09595)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to assess cultural inclusivity biases in Large Language Models (LLMs) through open-ended questions that require generators to produce culturally diverse responses.

**Target Audience**:
- ML Researchers
- AI Developers
- Cultural Anthropologists

**Tasks**:
- Cultural Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: OpenAI's o1 model generated and human-validated questions.

**Size**: 175 questions

**Format**: N/A

**Annotation**: Questions were validated through a multi-stage pipeline involving automated and human validation.

## 🔬 Methodology

**Methods**:
- Zero-shot classification
- Sentiment analysis

**Metrics**:
- Perspective Distribution Score (PDS)
- PDS Entropy

**Calculation**: PDS measures the representational share of cultural perspectives extracted from LLM responses.

**Interpretation**: Higher PDS and entropy values indicate greater cultural inclusivity in LLM outputs.

**Validation**: Three-stage validation process involving automated generation, LLM-assisted evaluation, and final human validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
