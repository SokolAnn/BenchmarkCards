# CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models

## 📊 Benchmark Details

**Name**: CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models

**Overview**: CRUD-RAG is a comprehensive benchmark that evaluates Retrieval-Augmented Generation (RAG) systems through various application scenarios categorized into Create, Read, Update, and Delete (CRUD), providing a robust evaluation framework for language models handling external knowledge.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- RGB
- NQ
- RAGAS
- ARES

**Resources**:
- [GitHub Repository](https://github.com/IAAR-Shanghai/CRUD_RAG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for RAG systems, facilitating the assessment of their performance across various CRUD application scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Continuation
- Question Answering
- Hallucination Modification
- Multi-Document Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from nearly 300,000 historical news articles from major Chinese news websites.

**Size**: 86,834 retrieval documents and various datasets for evaluation tasks totaling 10,728 for text continuation, 10,728 for multi-document summarization, 3,199 for single-document QA, 3,192 for multi-document QA, 5,130 for hallucination modification.

**Format**: N/A

**Annotation**: Datasets were created using automated generation via GPT-4 with manual refinement for QA tasks to ensure quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU
- ROUGE
- bertScore
- RAGQuestEval

**Calculation**: Metrics calculated by comparing output against ground truth using specific scoring mechanisms designed for various tasks.

**Interpretation**: Higher scores in metrics indicate better performance of RAG systems in generating accurate and relevant text based on retrieval.

**Baseline Results**: Experiments conducted with various LLMs including GPT-3.5, GPT-4, and Qwen-14B for comparison.

**Validation**: Extensive evaluation through various experiments demonstrating the efficacy of RAG across the CRUD framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
