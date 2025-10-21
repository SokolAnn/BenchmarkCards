# JurisTCU

## 📊 Benchmark Details

**Name**: JurisTCU

**Overview**: This paper introduces JurisTCU, a Brazilian Portuguese dataset for legal information retrieval (LIR) containing 16,045 jurisprudential documents and 150 queries annotated with relevance judgments. It addresses the scarcity of Portuguese-language LIR datasets with query relevance annotations.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Portuguese

**Similar Benchmarks**:
- MS MARCO
- mMARCO
- Ulysses-RFCorpus

**Resources**:
- [Resource](https://huggingface.co/datasets/LeandroRibeiro/JurisTCU)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the Portuguese-language information retrieval (IR) research community and to improve legal search systems.

**Target Audience**:
- ML Researchers
- Legal Domain Professionals

**Tasks**:
- Information Retrieval

**Limitations**: The JurisTCU dataset focuses on TCU jurisprudence, and its use to infer the performance of retrievers may not generalize to other domains.

## 💾 Data

**Source**: The dataset was created using documents produced by TCU, which includes jurisprudence from the Brazilian Federal Court of Accounts.

**Size**: 16,045 documents

**Format**: N/A

**Annotation**: Relevance judgments created through a hybrid approach combining LLM-based scoring with expert domain validation.

## 🔬 Methodology

**Methods**:
- Lexical search
- Semantic search

**Metrics**:
- Precision (P@10)
- Recall (R@10)
- Mean Reciprocal Rank (MRR@10)
- Normalized Discounted Cumulative Gain (nDCG@10)

**Calculation**: Metrics were calculated by evaluating retrieved documents against the relevance judgments for each query.

**Interpretation**: Higher precision and recall indicate better performance of the search methods applied.

**Baseline Results**: BM25 baseline performance was evaluated against various document expansion methods and LLM-based models.

**Validation**: 14 experiments were conducted using the dataset for validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
