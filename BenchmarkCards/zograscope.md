# ZOGRASCOPE

## 📊 Benchmark Details

**Name**: ZOGRASCOPE

**Overview**: ZOGRASCOPE is a benchmark designed specifically for property graphs and queries written in Cypher, including a diverse set of manually annotated queries of varying complexity, organized into three partitions: iid, compositional, and length.

**Data Type**: question-Cypher query pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/interact-erc/ZOGRASCOPE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for advancing research in semantic parsing over property graphs and to evaluate the performance of semantic parsers.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Semantic Parsing

**Limitations**: The dataset does not currently include complex query patterns such as nested sub-queries.

## 💾 Data

**Source**: Built from an open-access crime investigation graph using Cypher queries.

**Size**: 5,000 samples

**Format**: N/A

**Annotation**: Each example is manually annotated by experts.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- In-context learning (dynamic and fixed)
- Zero-shot evaluation

**Metrics**:
- Execution accuracy

**Calculation**: A prediction is deemed correct if it yields identical results to the reference query when executed on the knowledge graph.

**Interpretation**: Performance improves as more supervision is provided; zero-shot setting performs poorly but accuracy improves with added examples.

**Baseline Results**: Fine-tuning achieved the best performance for each of the models tested.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive information has been removed and replaced with fictitious content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
