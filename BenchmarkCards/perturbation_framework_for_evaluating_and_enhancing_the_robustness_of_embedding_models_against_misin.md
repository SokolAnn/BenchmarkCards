# Perturbation Framework for Evaluating and Enhancing the Robustness of Embedding Models Against Misinformation Edits

## 📊 Benchmark Details

**Name**: Perturbation Framework for Evaluating and Enhancing the Robustness of Embedding Models Against Misinformation Edits

**Overview**: This paper introduces a perturbation framework that generates valid and natural claim variations to assess the robustness of sentence embedding models in a multi-stage retrieval pipeline and evaluate the effectiveness of various mitigation approaches.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2503.03417)

## 🎯 Purpose and Intended Users

**Goal**: To improve claim matching systems and provide reliable fact-checking of evolving misinformation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Claim Matching

**Limitations**: The dataset coverage is limited to claims encountered by fact-checkers, which may not represent the broader misinformation landscape.

## 💾 Data

**Source**: CheckThat22, FactCheckTweet, OOD Dataset from Meedan

**Size**: 3 datasets (CheckThat22: 2,592 claims, FactCheckTweet: 3,578 claims, OOD Dataset: 721 claims)

**Format**: CSV

**Annotation**: Manually verified for validity and naturalness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (MAP)

**Calculation**: Calculated using the similarity between claims and their corresponding fact-checks based on embedding models.

**Interpretation**: Higher MAP indicates better retrieval performance of fact-checks relevant to the claims.

**Validation**: Evaluated across various perturbation types to ensure robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Data poisoning, Prompt injection attack
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Claims used are publicly available and verified. No private data included.

**Data Licensing**: Datasets used are accessible for research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
