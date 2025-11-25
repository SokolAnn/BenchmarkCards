# DIVKNOW QA

## 📊 Benchmark Details

**Name**: DIVKNOW QA

**Overview**: DIVKNOW QA is a novel fact-centric multi-hop question-answering benchmark that requires models to utilize heterogeneous knowledge sources equitably to answer a question. It assesses the reasoning ability of LLMs via jointly exploiting open-domain QA over heterogeneous knowledge sources.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HybridQA
- OTT-QA
- NQ-Tables
- TAT-QA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the proficiency of question-answering systems, especially those enhanced by retrieval tools, in addressing knowledge-intensive questions with a strong emphasis on multi-hop multi-source retrieval.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset with human-annotated examples linked to knowledge sources.

**Size**: 940 examples

**Format**: N/A

**Annotation**: Created using a combination of automatic generation through predefined reasoning chains and human annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match (EM)
- F1 Score
- Recall

**Calculation**: Metrics are calculated by comparing model predictions to the ground truth answers.

**Interpretation**: Higher scores indicate better performance in correctly answering multi-hop questions.

**Baseline Results**: Comparative results with existing models showed significant improvements.

**Validation**: The benchmark was validated through human annotation and verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
