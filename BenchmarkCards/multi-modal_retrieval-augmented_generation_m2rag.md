# Multi-Modal Retrieval-Augmented Generation (M2RAG)

## 📊 Benchmark Details

**Name**: Multi-Modal Retrieval-Augmented Generation (M2RAG)

**Overview**: M2RAG is a benchmark designed to evaluate the effectiveness of Multi-modal Large Language Models (MLLMs) in leveraging knowledge from multi-modal retrieval documents, comprising tasks such as image captioning, multi-modal question answering, multi-modal fact verification, and image reranking.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebQA
- Factify

**Resources**:
- [GitHub Repository](https://github.com/NEUIR/M2RAG)

## 🎯 Purpose and Intended Users

**Goal**: To advance the evaluation of retrieval-augmented generation in multi-modal contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Captioning
- Multi-Modal Question Answering
- Multi-Modal Fact Verification
- Image Reranking

**Limitations**: N/A

## 💾 Data

**Source**: WebQA and Factify datasets

**Size**: 389,750 documents

**Format**: JSON

**Annotation**: Annotated based on user queries and related multi-modal documents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BERTScore
- ROUGE-L
- CIDEr
- Accuracy
- F1 Score

**Calculation**: Calculated using standard evaluation metrics for each task as discussed in the methodology section of the paper.

**Interpretation**: Higher scores indicate better performance in correctly leveraging retrieved multi-modal documents for generation tasks.

**Baseline Results**: Performance of models like MiniCPM-V 2.6 and Qwen2-VL on the M2RAG benchmark shows significant improvements after applying MM-RAIT.

**Validation**: Ensured through comparative analysis with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC0-1.0 for WebQA; MIT for Factify.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
