# CoXQL (Conversational Explanation Query Language)

## 📊 Benchmark Details

**Name**: CoXQL (Conversational Explanation Query Language)

**Overview**: CoXQL is the first dataset in the NLP domain for user intent recognition in Conversational Explainable AI (ConvXAI), covering 31 intents and supporting a variety of XAI operations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CoSQL
- Spider

**Resources**:
- [GitHub Repository](https://github.com/DFKI-NLP/CoXQL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for explanation request parsing in ConvXAI systems and to improve explanation intent recognition.

**Target Audience**:
- ML Researchers
- ConvXAI Developers

**Tasks**:
- Intent Recognition
- Text-to-SQL Parsing

**Limitations**: The current complexity of user questions might be lower compared to other text-to-SQL datasets that involve complex SQL grammar.

## 💾 Data

**Source**: Manually created and augmented user questions and SQL-like queries based on existing studies and datasets.

**Size**: 1,179 pairs

**Format**: JSON

**Annotation**: Annotated by three authors with a token-level inter-annotator agreement of Fleiss’ κ= 0.87.

## 🔬 Methodology

**Methods**:
- Multi-prompt Parsing
- Guided Decoding
- Nearest Neighbor

**Metrics**:
- Exact Match Parsing Accuracy

**Calculation**: Measured by comparing generated SQL-like queries with gold parses.

**Interpretation**: High accuracy indicates better performance in intent recognition.

**Baseline Results**: Baseline achieved 44.25% accuracy using Nearest Neighbor.

**Validation**: Evaluation conducted on various state-of-the-art LLMs and performance compared using different parsing strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
