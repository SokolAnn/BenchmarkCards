# MultiClaimNet

## 📊 Benchmark Details

**Name**: MultiClaimNet

**Overview**: MultiClaimNet is a collection of three multilingual claim clustering datasets constructed from claim-matching pairs, automatically formed to improve fact-checking processes by grouping verified and unverified claims discussing the same underlying facts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Chinese
- French
- German
- Italian
- Portuguese
- Russian
- Arabic
- Turkish
- Korean
- Japanese
- Hindi
- Urdu
- Bengali
- Vietnamese
- Thai
- Swahili
- Filipino
- Malay

**Resources**:
- [Resource](https://zenodo.org/uploads/15100352)

## 🎯 Purpose and Intended Users

**Goal**: To create datasets for claim clustering that enhance the efficiency and scalability of automated fact-checking processes across multiple languages.

**Target Audience**:
- ML Researchers
- Fact-Checkers
- Data Scientists

**Tasks**:
- Clustering
- Fact-Checking

**Limitations**: Data curation bias; reliance solely on textual content for annotation; potential mismerging of claims due to multiple factual statements.

## 💾 Data

**Source**: Constructed from existing claim-matching datasets (ClaimCheck and ClaimMatch) and the MultiClaim fact-checked claims dataset.

**Size**: 85,300 claims

**Format**: JSON

**Annotation**: Claims are annotated for similarity using large language models.

## 🔬 Methodology

**Methods**:
- Automated clustering
- Nearest neighbor search
- Manual validation

**Metrics**:
- Adjusted Rand Index (ARI)
- Adjusted Mutual Index (AMI)
- Homogeneity (HMG)
- Completeness (CMP)
- V-Measure (VM)
- Purity

**Calculation**: Metrics are computed by assessing the generated clusters against ground-truth labels.

**Interpretation**: Higher ARI and AMI scores indicate better clustering performance.

**Validation**: Clusters were validated using both automated processes and manual inspection for large clusters.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: Yes, the datasets include claims in 86 languages, aiming for multilingual representation.

**Potential Harm**: Potential for misrepresentation and bias in automated labeling leading to misinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The method of annotation does not explicitly discuss privacy measures; assumes claims do not contain sensitive personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
