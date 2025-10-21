# Synthetic Datasets for Knowledge Graph Completion Evaluation

## 📊 Benchmark Details

**Name**: Synthetic Datasets for Knowledge Graph Completion Evaluation

**Overview**: Proposes synthetic datasets to evaluate the inference ability of pre-trained language model-based knowledge graph completion (KGC) methods by separately considering pre-trained knowledge and inference capabilities.

**Data Type**: triples with descriptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2311.09109)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the inference capabilities of PLM-based knowledge graph completion methods by constructing synthetic datasets.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Knowledge Graph Completion

**Limitations**: N/A

## 💾 Data

**Source**: WN18RR, FB15k-237, Wikidata5m

**Size**: Multiple datasets with varying sizes (e.g., 40,943 entities, 86,835 training triples for WN18RR)

**Format**: N/A

**Annotation**: Synthetic data generation methods described in the paper.

## 🔬 Methodology

**Methods**:
- Evaluation of KGC methods using synthetic datasets

**Metrics**:
- Hits@k

**Calculation**: Metrics calculated based on the rank prediction metrics such as Hits@k, mean rank (MR), and mean reciprocal rank (MRR).

**Interpretation**: Higher Hits@k values indicate better performance in inferring unseen links.

**Baseline Results**: TransE performance for comparison, specific scores not provided.

**Validation**: Results validated through experiments on different pre-trained models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
