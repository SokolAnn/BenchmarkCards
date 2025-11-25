# Alama Health QA

## 📊 Benchmark Details

**Name**: Alama Health QA

**Overview**: Alama Health QA is a benchmark designed to assess medical language models with a focus on African disease burdens and is anchored on the Kenyan Clinical Practice Guidelines. It aims to provide contextually relevant medical question-answering data.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- AfriMed-QA
- MMLU-Medical
- PubMedQA
- MedMCQA
- MedQA-USMLE

**Resources**:
- [Resource](https://doi.org/10.48550/arXiv.2411.15640)

## 🎯 Purpose and Intended Users

**Goal**: To provide a regionally relevant benchmark for evaluating medical language models, ensuring they are applicable within the context of African healthcare and aligned with local guidelines.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset currently focuses only on English language questions; future versions plan to incorporate other African languages.

## 💾 Data

**Source**: Constructed from the Kenyan Clinical Practice Guidelines using a retrieval-augmented generation framework.

**Size**: 40,607 questions

**Format**: JSON

**Annotation**: Leveraged expert input for question generation and alignment with clinical guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Flesch-Kincaid Grade Level
- Type-Token Ratio (TTR)

**Calculation**: Evaluation metrics calculated based on reviewer assessments and semantic analysis of medical question-answering pairs.

**Interpretation**: Scores on metrics reflect the clinical relevance, guideline alignment, and complexity of the questions in the context of healthcare.

**Validation**: Validated through expert ratings across key medical areas.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection and handling processes conform to privacy best practices outlined by the Kenyan health regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with local health data regulations as per Kenyan standards.
