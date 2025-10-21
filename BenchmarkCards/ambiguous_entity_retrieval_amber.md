# Ambiguous Entity Retrieval (AmbER)

## 📊 Benchmark Details

**Name**: Ambiguous Entity Retrieval (AmbER)

**Overview**: We introduce AmbER sets, a benchmark for evaluating the entity disambiguation capabilities of retrievers across multiple NLP tasks. Each AmbER set is a collection of queries about entities that share a name, helping assess the role of entity popularity in disambiguation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/anthonywchen/AmbER-Sets)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the entity disambiguation capabilities of retrievers in open-domain NLP tasks.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Fact Checking
- Slot Filling
- Question Answering

**Limitations**: The pipeline relies on Wikipedia and Wikidata, which may result in ambiguous queries if a property is missing from Wikidata.

## 💾 Data

**Source**: Wikidata knowledge graph

**Size**: 80,000 queries

**Format**: JSON

**Annotation**: Automatically generated through a pipeline designed to create AmbER sets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated as the percentage of retrieved documents that are correct.

**Interpretation**: Higher accuracy indicates better entity disambiguation capabilities of the retrievers.

**Validation**: Validated through systematic studies on retrieval systems with varying performance on heads vs. tails.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
