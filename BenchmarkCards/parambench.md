# ParamBench

## 📊 Benchmark Details

**Name**: ParamBench

**Overview**: ParamBench is a graduate-level benchmark consisting of around 11.5K questions in Hindi language covering 16 diverse subjects specific to the Indian context, examining language understanding and culturally nuanced reasoning through various question formats.

**Data Type**: question-answering pairs

**Domains**:
- Education

**Languages**:
- Hindi

**Similar Benchmarks**:
- KMMLU
- CMMLU
- BIG-Bench
- HELM
- SANSKRITI
- MILU

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Identify and quantify current gaps in LLM performance for the Indian context, guiding development of culturally and linguistically aligned models.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions are collected from UGC-NET and UPSC Civil Services examination papers.

**Size**: 11,446 questions

**Format**: CSV

**Annotation**: Annotated by subject-matter experts proficient in Hindi

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Direct answer matching

**Metrics**:
- Accuracy

**Calculation**: Accuracy is reported as the proportion of correct outputs based on direct answer matching generated responses compared with the gold key.

**Interpretation**: Higher accuracy indicates better performance on culturally grounded questioning.

**Validation**: Quality assurance protocols included both manual and automated checks

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
