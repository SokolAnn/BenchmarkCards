# HOH (How Outdated information Harms Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: HOH (How Outdated information Harms Retrieval-Augmented Generation)

**Overview**: HOH is the first benchmark designed to evaluate the impact of outdated information on Retrieval-Augmented Generation (RAG). It features a dynamic QA dataset and a mock search engine that maintains both current and historical documents, addressing the challenges presented by outdated knowledge in language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RealtimeQA
- FreshQA
- TemporalWiki
- EvolvingQA
- GrowOVER

**Resources**:
- [GitHub Repository](https://github.com/0russwest0/HoH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Retrieval-Augmented Generation systems' robustness against outdated information and enhance understanding of temporal challenges in RAG.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark mainly relies on changes in Wikipedia snapshots, which may not reflect rapid real-world changes.

## 💾 Data

**Source**: Generated from Wikipedia snapshots for capturing evolving real-world knowledge.

**Size**: 96,124 question-answer pairs and 219,463 documents

**Format**: JSON

**Annotation**: Annotated for current and outdated answers, including evidence and last modified timestamps.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated by evaluating LLM responses as 'perfect', 'missing', or 'harmful'.

**Interpretation**: A response is considered 'perfect' if it accurately answers the question without errors.

**Baseline Results**: Llama-70B achieved only a modest score of 51.7% on the benchmark.

**Validation**: Extensive experiments reveal the significant impact of outdated information on RAG performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The benchmark allows for assessments across various demographics but lacks explicit demographic categorizations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
