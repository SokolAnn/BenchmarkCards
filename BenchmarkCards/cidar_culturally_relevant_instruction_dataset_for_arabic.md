# CIDAR (Culturally Relevant Instruction Dataset For Arabic)

## 📊 Benchmark Details

**Name**: CIDAR (Culturally Relevant Instruction Dataset For Arabic)

**Overview**: CIDAR is the first open Arabic instruction-tuning dataset culturally-aligned by human reviewers, containing 10,000 instruction and output pairs that represent the Arab region.

**Data Type**: instruction-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/ARBML/CIDAR)
- [Resource](https://hf.co/datasets/arbml/CIDAR)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset that reflects the cultural differences and linguistic peculiarities of the Arabic language, enhancing the alignment of Large Language Models (LLMs) with Arabic culture.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Tuning

**Limitations**: The dataset size might limit its uses in large-scale instruction tuning and may not fully incorporate various Arabic dialects.

## 💾 Data

**Source**: Derived from the ALPAGASUS dataset and supplemented with additional instructions from the Ask the Teacher website.

**Size**: 10,000 instruction-output pairs

**Format**: Parquet

**Annotation**: Manually reviewed and localized by human reviewers.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Localization review

**Metrics**:
- Instruction success rate
- Cultural relevance accuracy

**Calculation**: Metrics are computed based on the manual review and comparison with Western cultural datasets.

**Interpretation**: A higher accuracy indicates a better alignment with Arabic cultural contexts.

**Validation**: The dataset was validated through extensive human review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes modifications to ensure representation of diverse Arabic cultural elements.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
