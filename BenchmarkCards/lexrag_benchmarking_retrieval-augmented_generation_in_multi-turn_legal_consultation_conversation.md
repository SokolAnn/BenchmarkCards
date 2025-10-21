# LexRAG (Benchmarking Retrieval-Augmented Generation in Multi-Turn Legal Consultation Conversation)

## 📊 Benchmark Details

**Name**: LexRAG (Benchmarking Retrieval-Augmented Generation in Multi-Turn Legal Consultation Conversation)

**Overview**: LexRAG is the first benchmark specifically designed to evaluate Retrieval-Augmented Generation (RAG) in multi-turn legal consultations. It consists of 1,013 multi-turn dialogue samples and 17,228 candidate legal articles, with an emphasis on assessing conversational knowledge retrieval and response generation capabilities.

**Data Type**: multi-turn dialogues

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- LexGLUE

**Resources**:
- [GitHub Repository](https://github.com/CSHaitao/LexRAG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized platform for evaluating retrieval and generation capabilities in complex legal consultation conversations.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- AI Developers

**Tasks**:
- Conversational Knowledge Retrieval
- Response Generation

**Limitations**: LexRAG primarily focuses on Chinese legal scenarios, which limits its applicability in broader multilingual contexts.

## 💾 Data

**Source**: Legal statutes and real-world legal consultation platforms.

**Size**: 1,013 multi-turn dialogues

**Format**: JSON

**Annotation**: Annotated by legal experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall
- NDCG
- ROUGE
- BLEU

**Calculation**: Metrics calculated based on the relevance of responses and retrieval accuracy.

**Interpretation**: Higher scores indicate better performance in generating accurate and relevant legal answers.

**Validation**: Rigorous evaluation through expert validation and comparison with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Annotations conducted by a diverse team of legal experts.

**Potential Harm**: Potential for inaccurate legal information leading to misunderstandings.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
