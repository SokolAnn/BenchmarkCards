# Customer Support Conversations Dataset (CSConDa)

## 📊 Benchmark Details

**Name**: Customer Support Conversations Dataset (CSConDa)

**Overview**: CSConDa is a high-quality benchmark comprising over 9,000 QA pairs, curated from customer interactions at a Vietnamese software company, aimed at evaluating Vietnamese Large Language Models (ViLLMs) in real-world customer support scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Resources**:
- [Resource](https://huggingface.co/datasets/CSConDa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating Vietnamese Large Language Models (ViLLMs) in customer support applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Customer support interactions with human advisors at a Vietnamese software company (DooPage).

**Size**: 9,849 examples

**Format**: JSON

**Annotation**: Manual annotation by experts with supervision from a domain expert.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Syntactic analysis

**Metrics**:
- BLEU Score
- ROUGE-L
- METEOR
- Cosine Similarity
- BERTScore
- Hallucination Score

**Calculation**: Metrics are calculated based on the models' outputs compared to human-annotated reference answers.

**Interpretation**: Higher scores indicate better performance.

**Validation**: Systematic evaluation of 11 lightweight open-source ViLLMs using CSConDa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures applied to remove personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
