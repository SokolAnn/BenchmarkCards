# CORAL (Conversational Retrieval-Augmented Generation Language Benchmark)

## 📊 Benchmark Details

**Name**: CORAL (Conversational Retrieval-Augmented Generation Language Benchmark)

**Overview**: CORAL is a large-scale benchmark designed to assess Retrieval-Augmented Generation (RAG) systems in realistic multi-turn conversational settings, including diverse information-seeking conversations automatically derived from Wikipedia. It supports three core tasks of conversational RAG: passage retrieval, response generation, and citation labeling.

**Data Type**: conversational data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TopiOCQA
- QReCC
- Wizard of Wikipedia
- CoQA
- OR-QuAC
- Doc2Dial
- TREC CAsT19
- TREC CAsT20
- TREC CAsT21
- TREC CAsT22

**Resources**:
- [GitHub Repository](https://github.com/Ariya12138/CORAL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark that systematically evaluates and advances conversational Retrieval-Augmented Generation systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Conversational Passage Retrieval
- Response Generation
- Citation Labeling

**Limitations**: The use of the CORAL benchmark is limited to assessing conversational RAG methods, as it borrows content from Wikipedia which may lead to contamination in the conversational process due to training data overlap.

## 💾 Data

**Source**: Automatically derived from English Wikipedia pages

**Size**: 8,000 conversations

**Format**: JSON

**Annotation**: Automatically generated through tailored sampling from Wikipedia pages

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Mean Average Precision (MAP)
- NDCG
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the evaluated tasks of passage retrieval, response generation, and citation labeling.

**Interpretation**: Higher MRR, MAP, and NDCG scores indicate better retrieval performance, while higher BLEU and ROUGE-L scores indicate better response quality.

**Baseline Results**: Fine-tuned open-source LLM outperforms commercial closed-source LLM in retrieval tasks.

**Validation**: The benchmark's effectiveness and reliability are validated through comprehensive evaluations of various RAG methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to detect inaccuracies in conversational contexts and improve clarity in responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data comprises non-sensitive information derived from Wikipedia, while ensuring citations are maintained for accountability.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
