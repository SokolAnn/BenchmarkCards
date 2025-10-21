# ProCQA: A Large-scale Community-based Programming Question Answering Dataset for Code Search

## 📊 Benchmark Details

**Name**: ProCQA: A Large-scale Community-based Programming Question Answering Dataset for Code Search

**Overview**: ProCQA is a large-scale programming question answering dataset extracted from the StackOverflow community, offering naturally structured mixed-modal QA pairs. This dataset encompasses approximately 5 million QA pairs across 11 programming languages, designed for effective evaluation and pre-training of code search models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- CodeSearchNet
- CodeQA
- CoSQA

**Resources**:
- [GitHub Repository](https://github.com/jordane95/procqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and diverse programming question answering dataset useful for evaluating and training code language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Education Practitioners

**Tasks**:
- Answer Retrieval
- Answer Generation

**Limitations**: N/A

## 💾 Data

**Source**: StackOverflow community through public dataset dumps.

**Size**: 5,000,000 QA pairs

**Format**: Mixed-modal data format with natural language questions and answers including code snippets.

**Annotation**: Rule-based filtering for low-quality questions and answers.

## 🔬 Methodology

**Methods**:
- Contrastive learning
- Pre-training
- Fine-tuning

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Recall
- ROUGE

**Calculation**: Metrics are calculated based on the performance of models trained on the ProCQA dataset across various benchmarks.

**Interpretation**: Higher scores in MRR and Recall indicate better retrieval of relevant code snippets based on user queries.

**Baseline Results**: Compared to CodeRetriever, the proposed models demonstrate improvements of 1 to 10 percentage points across various benchmarks.

**Validation**: Validation performed through evaluation on several existing code retrieval benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: The dataset aims to reduce data contamination to ensure fairness in model training.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
