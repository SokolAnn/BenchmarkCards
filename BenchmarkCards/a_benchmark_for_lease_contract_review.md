# A Benchmark for Lease Contract Review

## 📊 Benchmark Details

**Name**: A Benchmark for Lease Contract Review

**Overview**: This paper releases a new benchmark dataset of 179 lease agreement documents annotated with entities and red flags, aimed at improving the automation of contract reviews and reducing risks.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for the automatic detection of entities and red flags in lease agreements.

**Target Audience**:
- Legal Professionals
- Machine Learning Researchers

**Tasks**:
- Entity Extraction
- Red Flag Detection

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available lease agreements retrieved from the U.S. Securities and Exchange Commission (SEC) database.

**Size**: 179 documents

**Format**: N/A

**Annotation**: Manual annotation by legal professionals.

## 🔬 Methodology

**Methods**:
- ALBERT-based model for predictions
- CRF model for baseline
- Random Forest model for red flag detection

**Metrics**:
- Mean Average Precision (MAP)
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the performance of the models on the annotated dataset.

**Interpretation**: Higher scores in MAP, Precision, Recall, and F1 Score indicate better model performance in detecting entities and red flags.

**Baseline Results**: CRF and Random Forest models established as baselines for comparison.

**Validation**: Evaluation performed on a split of the annotated dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
