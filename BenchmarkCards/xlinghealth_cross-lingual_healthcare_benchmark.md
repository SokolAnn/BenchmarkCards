# XLingHealth (Cross-Lingual Healthcare Benchmark)

## 📊 Benchmark Details

**Name**: XLingHealth (Cross-Lingual Healthcare Benchmark)

**Overview**: XLingHealth is a cross-lingual healthcare benchmark for clinical health inquiry that focuses on evaluating multilingual capabilities of large language models (LLMs) in relation to healthcare queries. It incorporates datasets translated into Hindi, Chinese, and Spanish, and uses the framework XLingEval for comprehensive assessments.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Spanish
- Chinese
- Hindi

**Resources**:
- [GitHub Repository](https://github.com/claws-lab/XLingEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of XLingHealth is to assess the multilingual capabilities of large language models (LLMs) in healthcare contexts, ensuring equitable access to health information across languages.

**Target Audience**:
- Healthcare practitioners
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Developed from three healthcare datasets: HealthQA, LiveQA, and MedicationQA, which are originally curated in English and translated into other languages.

**Size**: 2,070 question-answer pairs

**Format**: N/A

**Annotation**: Expert-annotated by medical professionals.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Correctness
- Consistency
- Verifiability

**Calculation**: Metrics are calculated through comparative analyses of LLM-generated responses against ground truth answers across multiple languages.

**Interpretation**: Higher scores indicate better performance in providing correct, consistent, and verifiable responses.

**Validation**: Through a combined approach of algorithmic evaluation and expert human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
