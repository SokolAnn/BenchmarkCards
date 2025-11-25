# WIKES (Wiki Entity Summarization Benchmark)

## 📊 Benchmark Details

**Name**: WIKES (Wiki Entity Summarization Benchmark)

**Overview**: WIKES is a comprehensive benchmark for entity summarization that combines graph algorithms and NLP models using data from Wikidata and Wikipedia, allowing for automatic summary generation without human annotation.

**Data Type**: entity-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ESBM (Entity Summarization Benchmark)

**Resources**:
- [GitHub Repository](https://github.com/msorkhpar/wiki-entity-summarization)

## 🎯 Purpose and Intended Users

**Goal**: To foster research on entity summarization and provide a tool to generate arbitrary-size datasets for evaluating summarization models.

**Target Audience**:
- NLP Researchers
- Knowledge Graph Researchers

**Tasks**:
- Entity Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Data generated from Wikidata and Wikipedia XML dump files.

**Size**: Over 500,000 entities in various dataset sizes (small, medium, large).

**Format**: CSV

**Annotation**: Automatically generated using Wikipedia abstracts.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score
- Mean Average Precision (MAP)

**Calculation**: F1 Score is calculated based on precision and recall; MAP measures the ranking quality of predicted summaries.

**Interpretation**: Higher F1 and MAP scores indicate better performance in entity summarization.

**Baseline Results**: Evaluated against existing benchmarks like ESBM.

**Validation**: Datasets are validated using a train-test-validation split of 70%-15%-15%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
