# LLMEval-Med

## 📊 Benchmark Details

**Name**: LLMEval-Med

**Overview**: LLMEval-Med is a comprehensive benchmark designed for evaluating the performance of large language models (LLMs) in medical contexts, featuring 2,996 high-quality questions derived from real-world clinical scenarios and electronic health records across five core medical dimensions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedMCQA
- MedQA
- MedBench
- MultiMedQA

**Resources**:
- [GitHub Repository](https://github.com/llmeval/LLMEval-Med)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and comprehensive evaluation framework for medical LLMs, ensuring authenticity and practicality in real clinical scenarios.

**Target Audience**:
- ML Researchers
- Medical Professionals
- AI Developers

**Tasks**:
- Medical Knowledge Evaluation
- Medical Language Understanding
- Medical Reasoning
- Medical Safety and Ethics
- Medical Text Generation

**Limitations**: Despite its comprehensive nature, LLMEval-Med primarily focuses on Chinese medical contexts, which may limit generalizability to other healthcare systems and languages.

## 💾 Data

**Source**: Real-world clinical records and expert-designed clinical scenarios.

**Size**: 2,996 questions

**Format**: N/A

**Annotation**: Curated and reviewed by medical professionals to ensure high-quality assessment criteria.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Usability Rate

**Calculation**: Usability Rate reflects whether the model’s responses provide genuine medical value.

**Interpretation**: Responses scoring 4 or above indicate adequate addressing of user inquiries.

**Baseline Results**: N/A

**Validation**: High human-machine agreement rate for usability judgments across tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
