# KGAR EVION

## 📊 Benchmark Details

**Name**: KGAR EVION

**Overview**: KGAR EVION is a knowledge graph-based agent designed for complex biomedical question-answering (QA) that integrates structured knowledge with the latent knowledge embedded in large language models. The agent verifies generated triplets against a grounded knowledge graph to enhance accuracy in medical reasoning and improves performance across newly curated datasets.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU-Med
- MedQA-US
- PubMedQA
- BioASQ

**Resources**:
- [GitHub Repository](https://github.com/mims-harvard/KGARevion)

## 🎯 Purpose and Intended Users

**Goal**: To enhance accuracy and reliability in handling complex biomedical queries through a multi-step reasoning process.

**Target Audience**:
- ML Researchers
- Domain Experts
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Three newly curated medical QA datasets (MedDDx) with different levels of semantic complexity, and AfriMed-QA focused on African healthcare.

**Size**: 1,769 question-answering samples

**Format**: CSV

**Annotation**: Generated via a combination of knowledge graph integration and expert review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on evaluation against benchmark datasets with maintained records of correctness.

**Interpretation**: Higher metrics indicate better performance in answering complex biomedical questions accurately.

**Baseline Results**: KGAR EVION demonstrates significant improvements in accuracy over 15 baseline models in handling complex medical queries across three datasets.

**Validation**: Validated through comparisons with multiple choice and open-ended reasoning settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
