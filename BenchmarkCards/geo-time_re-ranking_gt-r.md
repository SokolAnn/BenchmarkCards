# Geo-Time Re-ranking (GT-R)

## 📊 Benchmark Details

**Name**: Geo-Time Re-ranking (GT-R)

**Overview**: The Geo-Time Re-ranking (GT-R) framework improves the retrieval and recommendation of similar spatiotemporal and semantic associated environmental events by integrating multiple criteria including spatial proximity, temporal association, semantic similarity, and category-instructed similarity.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Environmental Science

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the efficiency and effectiveness of retrieving and recommending similar environmental events using Large Language Models (LLMs) with a focus on spatiotemporal analysis.

**Target Audience**:
- Researchers in Climate Change
- Environmental Scientists
- Data Scientists
- Policy Makers

**Tasks**:
- Information Retrieval
- Event Recommendation

**Limitations**: The dependency on well-defined geospatial and temporal metadata, which may not always be available or accurately captured.

## 💾 Data

**Source**: Local Environmental Observer (LEO) Network events

**Size**: 4,000 events

**Format**: structured text

**Annotation**: Manually curated by domain experts and community observers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Hit Rate
- nDCG
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are computed based on the ranking of relevant events retrieved.

**Interpretation**: Higher metrics indicate better retrieval effectiveness and relevance of recommendations.

**Baseline Results**: The proposed GT-R model achieved up to 40% improvement over heuristic models.

**Validation**: Empirical tests using a dataset of 1,000 query events linked to candidate events.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
