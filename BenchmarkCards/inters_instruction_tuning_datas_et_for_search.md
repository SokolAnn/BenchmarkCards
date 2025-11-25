# INTERS (INstruction Tuning datas Et foR Search)

## 📊 Benchmark Details

**Name**: INTERS (INstruction Tuning datas Et foR Search)

**Overview**: INTERS is a novel instruction tuning dataset designed to enhance the search capabilities of large language models (LLMs) across 20 tasks in information retrieval (IR), encompassing query understanding, document understanding, and query-document relationship understanding.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- FLAN

**Resources**:
- [GitHub Repository](https://github.com/DaoD/INTERS)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of LLMs on search-related tasks through instruction tuning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Query Understanding
- Document Understanding
- Query-document Relationship Understanding
- Fact Verification
- Summarization
- Reading Comprehension
- Conversational Question Answering
- Query Intent Classification
- Query Expansion
- Query Reformulation
- Query Suggestion
- Query Matching
- Query Clarification
- Citation Prediction
- Subtopic Generation
- Duplicate Question Retrieval
- Argument Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from 43 distinct datasets tailored for 20 different tasks in information retrieval.

**Size**: 200,000 examples

**Format**: JSONL

**Annotation**: Manual crafting of templates and task descriptions, along with zero-shot and few-shot examples.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Metrics are calculated based on model outputs compared to reference answers.

**Interpretation**: Higher scores indicate better understanding and performance in retrieval tasks.

**Baseline Results**: State-of-the-art models such as LLaMA, Mistral, and Falcon are fine-tuned with INTERS to evaluate their performance.

**Validation**: Model performance is validated through extensive experiments on various IR tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0 for released datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
