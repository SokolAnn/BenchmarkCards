# EvoWiki

## 📊 Benchmark Details

**Name**: EvoWiki

**Overview**: EvoWiki is a continually auto-updated evaluation dataset that captures the evolving nature of knowledge for evaluating LLMs’ ability to utilize external knowledge in dynamic, real-world scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LiveBench
- Realtime QA
- TemporalWiki

**Resources**:
- [GitHub Repository](https://github.com/wtangdev/EvoWiki)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the knowledge evolution capabilities of large language models (LLMs) and how effectively they adapt to evolving knowledge.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: Despite being recognized as high-quality corpora, Wikidata and Wikipedia inevitably contain noise.

## 💾 Data

**Source**: Constructed using continually updated knowledge graphs and sources, such as Wikidata and Wikipedia.

**Size**: 10,264 questions

**Format**: JSON

**Annotation**: Generated questions are verified based on context and correctness through human evaluation.

## 🔬 Methodology

**Methods**:
- Retrieval-Augmented Generation
- Continual Learning

**Metrics**:
- Accuracy
- Fluency
- Answerability

**Calculation**: Metrics are calculated based on the percentage of correct answers as well as human evaluations.

**Interpretation**: Higher scores indicate better performance in accurately answering questions based on the evolving knowledge.

**Validation**: Evaluated through experiments comparing models' performances on different knowledge evolution levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
