# LONG2RAG (Long-Context & Long-Form Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: LONG2RAG (Long-Context & Long-Form Retrieval-Augmented Generation)

**Overview**: LONG2RAG comprises 280 questions spanning 10 domains and 8 question categories, each associated with 5 retrieved documents with an average length of 2,444 words. It evaluates the extent to which LLMs incorporate key points extracted from the retrieved documents into their generated responses using the Key Point Recall (KPR) metric.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Healthcare
- Finance
- Legal
- Technology
- Arts
- Social Sciences

**Languages**:
- English

**Similar Benchmarks**:
- ProxyQA

**Resources**:
- [Resource](https://arxiv.org/abs/2410.23000)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust benchmark for evaluating long-context and long-form retrieval-augmented generation models in large language models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed using an automated pipeline that ensures minimal data contamination, and questions are designed to reflect real-world complexities in retrieval-augmented generation.

**Size**: 280 questions

**Format**: N/A

**Annotation**: Questions were generated and verified through a human-LLM collaborated verification process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation

**Metrics**:
- Key Point Recall (KPR)

**Calculation**: KPR measures the average coverage of key points from the retrieved documents incorporated in the LLM's generated responses.

**Interpretation**: Higher KPR scores indicate better performance in leveraging retrieved information to construct answers.

**Baseline Results**: KPR results across various LLMs were evaluated and compared to determine relative performance.

**Validation**: LONG2RAG has been validated through extensive testing across 9 state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To ensure ethical standards, the dataset was curated to avoid personal data or sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
