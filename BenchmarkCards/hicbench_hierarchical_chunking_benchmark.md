# HiCBench (Hierarchical Chunking Benchmark)

## 📊 Benchmark Details

**Name**: HiCBench (Hierarchical Chunking Benchmark)

**Overview**: HiCBench is a QA benchmark focused on hierarchical document chunking, designed to effectively evaluate the impact of chunking methods on different components of Retrieval-Augmented Generation (RAG) systems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Youtu-RAG/HiCBench)
- [GitHub Repository](https://github.com/TencentCloudADP/HiChunk.git)

## 🎯 Purpose and Intended Users

**Goal**: To assess the performance of chunking methods and their impact on retrievers and response models within RAG systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: OHRBench document corpus

**Size**: 130 documents

**Format**: N/A

**Annotation**: Manually annotated multi-level document chunking points and synthesized evidence-dense QA pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Rouge metrics
- Fact Coverage

**Calculation**: F1 metrics for chunking accuracy, Fact-Cov metric for response quality evaluation.

**Interpretation**: Higher F1 scores and Fact-Cov metrics indicate better chunking quality and response quality.

**Baseline Results**: F1 scores of chunking methods compared across several datasets.

**Validation**: Evaluated using LongBench, Qasper, GutenQA, and OHRBench datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
