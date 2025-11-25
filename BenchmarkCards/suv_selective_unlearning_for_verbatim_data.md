# SUV (Selective Unlearning for Verbatim data)

## 📊 Benchmark Details

**Name**: SUV (Selective Unlearning for Verbatim data)

**Overview**: SUV is a selective unlearning framework designed to prevent large language models from memorizing copyrighted content while preserving overall model utility. It constructs a dataset of copyrighted infringement cases to apply Direct Preference Optimization for unlearning, ensuring the model's performance on unrelated tasks remains intact.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CBP-500
- CBP-50

**Resources**:
- [GitHub Repository](https://github.com/xz-liu/SUV/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable and practical solution for mitigating copyright infringement risks in large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: A dataset constructed from 500 predominantly copyrighted books.

**Size**: 3.46 million sentences

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Direct Preference Optimization (DPO)
- Gradient Projection
- Fisher Regularization

**Metrics**:
- ROUGE-L
- Longest Common Subsequence (LCS)

**Calculation**: Metrics like ROUGE-L and LCS are used to evaluate the similarity between original and generated content.

**Interpretation**: Lower ROUGE-L scores indicate better unlearning performance metrics.

**Baseline Results**: Compared against baselines such as Vanilla model, Stable Sequential Unlearning (SSU), Gradient Ascent (GA), and Negative Preference Optimization (NPO).

**Validation**: Validated using experiments that measure unlearning performance and downstream task efficiency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Copyright Risk
- Utility Performance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
