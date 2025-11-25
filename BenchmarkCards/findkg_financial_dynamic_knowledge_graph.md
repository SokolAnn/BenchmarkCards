# FinDKG (Financial Dynamic Knowledge Graph)

## 📊 Benchmark Details

**Name**: FinDKG (Financial Dynamic Knowledge Graph)

**Overview**: FinDKG is an open-source dynamic knowledge graph dataset created from financial news articles, used for detecting trends in financial markets.

**Data Type**: quintuples (entities, entity categories, relation types, timestamps)

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://xiaohui-victor-li.github.io/FinDKG/#data)
- [Resource](https://huggingface.co/victorlxh/ICKG-v3.2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dynamic knowledge graph for analyzing financial trends and facilitate thematic investing.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Financial Analysts

**Tasks**:
- Link Prediction
- Temporal Knowledge Graph Learning

**Limitations**: N/A

## 💾 Data

**Source**: Financial news articles collected from the Wall Street Journal via open-source web archives.

**Size**: 400,000 articles

**Format**: Quintuples

**Annotation**: Automated extraction of entities, relationships, and timestamps using the Integrated Contextual Knowledge Graph Generator (ICKG).

## 🔬 Methodology

**Methods**:
- Graph Neural Networks
- Attention-Based Learning
- Temporal Embedding Learning

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Hits@3
- Hits@10

**Calculation**: Performance is evaluated by calculating MRR and Hits metrics based on predicted link ranks.

**Interpretation**: Higher values of MRR and Hits metrics indicate better model performance in link prediction tasks.

**Validation**: Models utilized a validation set with early stopping mechanism to avoid overfitting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
