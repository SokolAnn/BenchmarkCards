# Interpolated Approximate Measurement (IAM)

## 📊 Benchmark Details

**Name**: Interpolated Approximate Measurement (IAM)

**Overview**: IAM quantifies sample-level unlearning completeness by interpolating the model’s generalization-fitting behavior gap on queried samples, revealing risks of both over-unlearning and under-unlearning in approximate unlearning systems.

**Data Type**: text

**Domains**:
- Machine Learning
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Membership Inference Attacks (MIA)

**Resources**:
- [GitHub Repository](https://github.com/Happy2Git/Unlearning_Inference_IAM)
- [Resource](https://zenodo.org/records/15606363)

## 🎯 Purpose and Intended Users

**Goal**: To measure sample-level unlearning completeness and identify unlearning risks in machine learning models, particularly in approximate unlearning settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Unlearning Inference

**Limitations**: N/A

## 💾 Data

**Source**: CIFAR-10, CIFAR-100, CINIC-10, and Purchase datasets; also applicable to LLaMA-2 models.

**Size**: 197,324 records for Purchase; 60,000 images for CIFAR datasets; 270,000 images for CINIC-10.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Computed CDF values for the membership scores
- Used weighted averaging for interpolation results

**Metrics**:
- Area Under the Curve (AUC)
- Spearman correlation

**Calculation**: Combined scores from interpolated estimates and shadow models to calculate membership scores indicating unlearning completeness.

**Interpretation**: A membership score of 0 indicates that the model’s response relies entirely on generalization ability, while a score closer to 1 indicates fitting behavior.

**Baseline Results**: Existing Membership Inference Attack methods were benchmarked against IAM.

**Validation**: Evaluated across various datasets and approximating unlearning algorithms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Identified unlearning risks including under-unlearning (incomplete removal of data influence) and over-unlearning (removal of useful data influence).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used are publicly available; no personal information involved.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
