# FinRAGBench-V (A Benchmark for Multimodal RAG with Visual Citation in the Financial Domain)

## 📊 Benchmark Details

**Name**: FinRAGBench-V (A Benchmark for Multimodal RAG with Visual Citation in the Financial Domain)

**Overview**: FinRAGBench-V is a comprehensive visual RAG benchmark tailored for finance that effectively integrates multimodal data and provides visual citation to ensure traceability. It includes a bilingual retrieval corpus and a high-quality, human-annotated QA dataset spanning heterogeneous data types and question categories.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- FinQA
- OmniEval
- MME-Finance

**Resources**:
- [Resource](https://huggingface.co/datasets/zhaosuifeng/FinRAGBench-V)
- [GitHub Repository](https://github.com/zhaosuifeng/FinRAGBench-V)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development and evaluation of multimodal Retrieval-Augmented Generation systems in the financial domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A retrieval corpus collected from diverse real-world financial document sources, processed to create a QA dataset using LLM assistance and manual verification.

**Size**: 60,780 Chinese pages and 51,219 English pages in the retrieval corpus; 1,394 QA pairs in the dataset.

**Format**: Various formats including charts, tables, and plaintext.

**Annotation**: QA pairs synthesized using GPT-4o assistance with manual verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Precision
- ROUGE
- nDCG
- MRR

**Calculation**: Metrics such as precision and recall for visual citations are calculated based on the citation sets supporting the generated answers.

**Interpretation**: High precision and recall indicate effective visual citation capabilities, while ROUGE assesses the accuracy of generated answers compared to ground truth.

**Baseline Results**: Extensive experiments show multimodal retrievers outperform traditional text-based methods.

**Validation**: The benchmark's validation relied on both qualitative assessments by experts and quantitative evaluation metrics.

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

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
