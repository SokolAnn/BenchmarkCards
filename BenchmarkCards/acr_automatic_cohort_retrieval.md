# ACR (Automatic Cohort Retrieval)

## 📊 Benchmark Details

**Name**: ACR (Automatic Cohort Retrieval)

**Overview**: This paper presents a new benchmark task for Automatic Cohort Retrieval (ACR), emphasizing the need for high-quality cohort retrieval systems capable of handling longitudinal patient data across extensive healthcare databases.

**Data Type**: query-patient pairs, electronic medical records

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA

**Resources**:
- [Resource](https://arxiv.org/abs/2406.14780)

## 🎯 Purpose and Intended Users

**Goal**: To advance the efficiency and quality of cohort retrieval systems in healthcare, utilizing methods that integrate both large language models and neuro-symbolic architectures for processing electronic medical records.

**Target Audience**:
- Healthcare Researchers
- Data Scientists
- Clinical Researchers

**Tasks**:
- Cohort Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: EMR dataset from four healthcare sites comprising longitudinal patient records.

**Size**: 1,436 patients, 115,865 records

**Format**: N/A

**Annotation**: Structured and human-labeled query-patient pairs created through clinical abstractions.

## 🔬 Methodology

**Methods**:
- Recruitment of patient cohorts via querying
- Evaluation based on precision, recall, and F1-score

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Calculated based on true positives, false negatives, and false positives derived from the cohort retrieval results.

**Interpretation**: Higher precision indicates fewer false positives, while high recall indicates capturing more true positive patients.

**Validation**: Evaluated against gold standard datasets generated from clinical abstractions and reasoning processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Patient data anonymized from EMRs for research purposes.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
