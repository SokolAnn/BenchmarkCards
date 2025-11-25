# JAMSessions

## 📊 Benchmark Details

**Name**: JAMSessions

**Overview**: JAMSessions is a new dataset of over 100k user-query-item triples with anonymized user/item embeddings, combining conversational queries and user long-term preferences for personalized music recommendation.

**Data Type**: user-query-item triples

**Domains**:
- Natural Language Processing
- Music Recommendation

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hcai-mms/jam)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of JAMSessions is to provide a scalable and realistic dataset for training and evaluating natural language music recommendation systems that account for user preferences expressed over time.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Music Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Dataset of user-query-item triplets sampled from the search logs of a music streaming service.

**Size**: 112,337 triplets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Contrastive Learning
- Evaluation against baseline models

**Metrics**:
- Recall
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Metrics are calculated based on the proportion of relevant items retrieved and the ranking of relevant items.

**Interpretation**: A higher Recall and NDCG indicates better performance in retrieving relevant items in response to user queries.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
