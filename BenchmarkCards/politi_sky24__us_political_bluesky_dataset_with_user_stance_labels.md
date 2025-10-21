# POLITI SKY24: U.S. Political Bluesky Dataset with User Stance Labels

## 📊 Benchmark Details

**Name**: POLITI SKY24: U.S. Political Bluesky Dataset with User Stance Labels

**Overview**: The dataset comprises 16,044 user-target stance pairs enriched with engagement metadata, interaction graphs, and user posting histories, intended for the stance detection task focused on the 2024 U.S. presidential candidates Kamala Harris and Donald Trump.

**Data Type**: user-target stance pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.15616911)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive stance dataset focused on the 2024 U.S. presidential candidates, facilitating analysis of user viewpoints on a decentralized social network.

**Target Audience**:
- ML Researchers
- Social Scientists

**Tasks**:
- Stance Detection

**Limitations**: Sampling biases may exist due to the methodology of selecting users based on hashtag usage.

## 💾 Data

**Source**: Bluesky social network

**Size**: 16,044 user-target stance pairs

**Format**: Custom

**Annotation**: Labeled using a pipeline that combines text embedding and LLMs to determine user stances.

## 🔬 Methodology

**Methods**:
- Document retrieval using embedding models
- Stance labeling with Large Language Models (LLMs)

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the proportion of correct stance labels assigned to users.

**Interpretation**: Higher accuracy indicates better identification of user stances toward the political candidates.

**Baseline Results**: Average accuracy of 81% achieved by the selected LLM.

**Validation**: Utilized a validation set of users to configure and fine-tune the stance labeling pipeline.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected following Bluesky's terms of service with privacy considerations for user-generated content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
