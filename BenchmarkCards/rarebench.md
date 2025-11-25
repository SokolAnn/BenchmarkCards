# RareBench

## 📊 Benchmark Details

**Name**: RareBench

**Overview**: RareBench is a pioneering benchmark designed to systematically evaluate the capabilities of Large Language Models (LLMs) in diagnosing rare diseases along four critical dimensions.

**Data Type**: electronic health records

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA
- MedBench

**Resources**:
- [Resource](https://doi.org/10.1145/3637528.3671576)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the diagnostic capabilities of LLMs in the context of rare diseases.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Data Scientists

**Tasks**:
- Phenotype Extraction
- Screening for Rare Diseases
- Comparison Analysis of Common and Rare Diseases
- Differential Diagnosis among Universal Rare Diseases

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is compiled from Peking Union Medical College Hospital (PUMCH) and publicly available datasets.

**Size**: 2,185 cases

**Format**: N/A

**Annotation**: Cases were monitored by doctors to ensure patient information confidentiality and quality.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation of LLMs
- Human evaluation for comparative analysis

**Metrics**:
- Top-k Recall
- Mean Rank
- F1-score

**Calculation**: Metrics are calculated based on predictions made by LLMs in an evaluation context.

**Interpretation**: A higher top-k recall indicates better diagnostic accuracy, while mean rank gives insight into the model's predictive rankings.

**Validation**: The model was validated through comparison with clinical specialists and their diagnostic outcomes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patient data is monitored and anonymized to prevent personal information leakage.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study has been approved by the relevant ethical committees.
