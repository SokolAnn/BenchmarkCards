# Reddit Reports of Chronic Pain (RRCP)

## 📊 Benchmark Details

**Name**: Reddit Reports of Chronic Pain (RRCP)

**Overview**: This research presents the RRCP dataset, which comprises 86,537 Reddit submissions from 12 subreddits related to chronic pain. It aims to model the linguistic expression of chronic pain experiences by analyzing the semantic structure of discussions on Reddit and comparing concerns among different pathologies.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/praw-dev/praw)
- [GitHub Repository](https://github.com/dmarx/psaw)
- [Resource](https://gitlab.hlt.inesc-id.pt/dapn/rrcp-collection-public)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the RRCP dataset is to gain insights into the experience of chronic pain as reported in various subreddits, to identify similarities and differences in pain discussions across multiple pathologies.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Data Scientists

**Tasks**:
- Text Classification
- Natural Language Processing

**Limitations**: The dataset is limited to user-generated content from Reddit, which may not be representative of all chronic pain experiences due to demographic biases.

## 💾 Data

**Source**: The RRCP dataset was created by collecting all textual submissions from selected Reddit subreddits related to chronic pain.

**Size**: 86,537 submissions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- TF-IDF
- Cosine Similarity

**Calculation**: Metrics were calculated using clustering and topic modeling techniques to understand the semantic structures of chronic pain discussions.

**Interpretation**: Common themes and concerns related to chronic pain were identified through clustering of document centroids and topic modeling.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through comparison of semantic spans among the various subreddits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset offers a limited demographic analysis based purely on public information available from Reddit users.

**Potential Harm**: ['Potential bias due to demographic underrepresentation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To protect user privacy, no identifying information about individual posters was collected or disclosed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was not sought directly, as the data was collected from public Reddit submissions under its Terms of Use.

**Compliance With Regulations**: Not Applicable
