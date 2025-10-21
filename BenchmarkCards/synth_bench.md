# SYNTH BENCH

## 📊 Benchmark Details

**Name**: SYNTH BENCH

**Overview**: SYNTH BENCH encompasses 8 domain-specific documents across 4 domains, featuring diverse query complexities, clue completeness, and fine-grained citation granularity. It serves to evaluate retrievers on queries of different complexities and generators on fidelity to retrieved documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Education
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- Natural Questions
- TriviaQA
- SQuAD
- PopQA
- HotpotQA
- WikiMultiHopQA

**Resources**:
- [GitHub Repository](https://github.com/EachSheep/RAGSynth)

## 🎯 Purpose and Intended Users

**Goal**: To optimize retriever robustness and generator fidelity through the use of synthetic data in the RAG framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 8 domain-specific document collections across 4 domains.

**Size**: N/A

**Format**: N/A

**Annotation**: Manually curated and validated through specific evaluation criteria.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Criteria-based Score for Generation (CSG)

**Calculation**: CSG is calculated based on completeness, understanding, and citation scores.

**Interpretation**: A higher CSG indicates better fidelity and robustness of the generated answers.

**Baseline Results**: N/A

**Validation**: Evaluated on queries of different complexities.

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
