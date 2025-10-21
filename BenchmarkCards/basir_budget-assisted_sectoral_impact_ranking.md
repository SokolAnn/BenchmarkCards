# BASIR (Budget-Assisted Sectoral Impact Ranking)

## 📊 Benchmark Details

**Name**: BASIR (Budget-Assisted Sectoral Impact Ranking)

**Overview**: BASIR is an annotated dataset mapping excerpts from Indian Union Budget transcripts (1947-2025) to sectoral impacts, facilitating the identification and ranking of sectors based on their predicted performance influenced by budget announcements.

**Data Type**: text

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/sohomghosh/BASIR_Budget_Assisted_Sectoral_Impact_Ranking/tree/main/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically identify and rank sectors based on their expected performance following Indian Union Budget announcements.

**Target Audience**:
- Investors
- Policymakers
- Financial Analysts
- Researchers

**Tasks**:
- Multi-Label Classification
- Performance Ranking

**Limitations**: The annotation approach may overlook subtle sector relationships. Temporal coverage is limited to data available post-1997, potentially missing long-term effects.

## 💾 Data

**Source**: A comprehensive corpus of Union Budget transcripts from the Ministry of Finance of India spanning from 1947 to 2025.

**Size**: 1,600+ excerpts for sector identification, 400+ texts for sector ranking

**Format**: JSON

**Annotation**: Manually validated sector tagging based on sector-company mapping and budget transcript text.

## 🔬 Methodology

**Methods**:
- Multi-label sector classification using fine-tuned embeddings and language models
- Performance ranking based on predicted sector returns

**Metrics**:
- F1 Score
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Performance is calculated based on the difference in opening prices for constituent companies of sectors around budget announcements.

**Interpretation**: Higher F1 Scores indicate better sector classification performance; NDCG scores reflect better ranking performance.

**Baseline Results**: Acc achieved 0.605 F1 score and 0.997 NDCG score in sector ranking.

**Validation**: Cross-validation methods employed for robustness in sector performance prediction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-SA-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
