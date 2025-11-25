# MIRIAD (Medical Instruction and Retrieval Dataset)

## 📊 Benchmark Details

**Name**: MIRIAD (Medical Instruction and Retrieval Dataset)

**Overview**: MIRIAD is a large-scale, curated corpus of 5,821,948 medical instruction-response pairs, each rephrased from and grounded in a passage from peer-reviewed medical literature using a semi-automated pipeline combining LLM generation, filtering, grounding, and human annotation.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/miriad)
- [GitHub Repository](https://github.com/eth-medical-ai-lab/MIRIAD)

## 🎯 Purpose and Intended Users

**Goal**: MIRIAD aims to provide a comprehensive knowledge base for down-stream medical AI applications, enabling improved retrieval-augmented generation (RAG) performance in clinical tasks.

**Target Audience**:
- Researchers
- Clinicians
- Patients

**Tasks**:
- Medical Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Semantic Scholar Open Research Corpus (S2ORC)

**Size**: 5,821,948 examples

**Format**: N/A

**Annotation**: Semi-automated pipeline with human annotation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of models trained with and without MIRIAD on various medical question-answering tasks.

**Interpretation**: Improved metrics indicate enhanced performance when using MIRIAD compared to unstructured sources.

**Baseline Results**: Existing medical QA datasets like PubMedQA consist of fewer than 300,000 questions.

**Validation**: The dataset undergoes multi-tier quality control including automated filtering and human expert annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: ODC-By v1.0, allows reuse and modification with proper attribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
