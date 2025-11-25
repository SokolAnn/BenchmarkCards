# Multidimensional Evaluation Framework for LLM-based Recommenders

## 📊 Benchmark Details

**Name**: Multidimensional Evaluation Framework for LLM-based Recommenders

**Overview**: The paper proposes a reproducible multidimensional evaluation framework specifically for evaluating the performance of LLM-based recommenders. It introduces four new evaluation dimensions—history length sensitivity, candidate position bias, generation-involved performance, and hallucinations—on top of traditional utility and novelty metrics.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FairLLM
- CFaiRLLM
- FairEvalLLM

**Resources**:
- [GitHub Repository](https://github.com/JiangDeccc/EvaLLMasRecommender)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for LLMs as recommenders, covering both traditional and novel evaluation dimensions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Recommender System Developers

**Tasks**:
- Recommendation Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Four real-world datasets: Amazon All Beauty, Sports & Outdoors, Movielens-1M, LastFM.

**Size**: 22363 users, 12101 items, 198502 interactions (Beauty); 35598 users, 18357 items, 296337 interactions (Sports); 6040 users, 3416 items, 999611 interactions (ML-1M); 1543 users, 7286 items, 173778 interactions (LastFM).

**Format**: CSV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hit Ratio (HR)
- Normalized Discounted Cumulative Gain (NDCG)
- Serendipity
- Average Recommendation Popularity (ARP)
- Overlap Item Coverage (OIC)
- Gini Coefficient

**Calculation**: Metrics are calculated based on the performance of LLMs in terms of accuracy and various fairness dimensions across multiple datasets.

**Interpretation**: Higher values in utility metrics indicate better performance in recommendation accuracy.

**Baseline Results**: Traditional recommendation models (e.g., BPRMF, GRU4Rec) are used as baselines for comparison.

**Validation**: The framework is validated using existing LLMs and traditional models across several datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Hallucination
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
