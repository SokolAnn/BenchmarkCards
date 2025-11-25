# XRAG (eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: XRAG (eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation)

**Overview**: XRAG is an open-source, modular codebase designed to evaluate foundational components of advanced Retrieval-Augmented Generation (RAG) systems, providing a comprehensive benchmark for assessing their effectiveness across pre-retrieval, retrieval, post-retrieval, and generation phases.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- DropQA
- NaturalQA

**Resources**:
- [GitHub Repository](https://github.com/DocAILab/XRAG)
- [Resource](https://huggingface.co/datasets/DocAILab/XRAG_Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework for benchmarking advanced Retrieval-Augmented Generation (RAG) systems and optimize their performance through comprehensive testing.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: While XRAG supports core RAG modules, its toolkit currently lacks comprehensive coverage of all RAG advancements and does not support RAG component training.

## 💾 Data

**Source**: Three benchmark datasets: HotpotQA, DropQA, and NaturalQA, which are preprocessed into a unified format for RAG evaluations.

**Size**: Total of 265,164 examples across all datasets

**Format**: Unified dataset structured to facilitate performance testing for retrieval and generation modules.

**Annotation**: Dataset sources include metadata from the original datasets, annotated for extracting relevant information.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1
- Mean Reciprocal Rank (MRR)
- Mean Average Precision (MAP)
- Hit@1
- Hit@10
- DCG
- NDCG
- ChrF
- METEOR
- ROUGE

**Calculation**: Evaluation metrics are calculated based on the performance of RAG components across various configurations.

**Interpretation**: Higher scores indicate better retrieval and generation performance.

**Baseline Results**: Baseline performance metrics are provided for each dataset tested, with detailed comparisons between different approaches.

**Validation**: The framework incorporates validation procedures to ensure reliability and accuracy of the evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias, Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is licensed under CC BY-NC-SA 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
