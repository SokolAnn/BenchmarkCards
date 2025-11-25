# SM3-Text-to-Query (Synthetic Multi-Model Medical Text-to-Query Benchmark)

## 📊 Benchmark Details

**Name**: SM3-Text-to-Query (Synthetic Multi-Model Medical Text-to-Query Benchmark)

**Overview**: SM3-Text-to-Query is the first multi-model medical Text-to-Query benchmark that provides data representations for relational databases, document stores, and graph databases, allowing evaluations across four query languages: SQL, MQL, Cypher, and SPARQL.

**Data Type**: question-query pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMICSQL
- MIMIC-SPARQL
- EHRSQL
- Spider

**Resources**:
- [GitHub Repository](https://github.com/jf87/SM3-Text-to-Query)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Text-to-Query systems across multiple core database models and query languages in a medical context.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text-to-Query

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic patient data generated from Synthea.

**Size**: 40,000 question/query pairs

**Format**: N/A

**Annotation**: Systematically and manually developed template questions augmented with values to construct diverse question/query pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Execution Accuracy (EA)

**Calculation**: EA is calculated as the fraction of questions where the outcomes of predicted and ground-truth queries yield identical results.

**Interpretation**: Higher EA indicates better translation of natural language questions to query statements across different database models.

**Baseline Results**: N/A

**Validation**: Dataset was developed with input from medical professionals to ensure relevance and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was generated synthetically, thus there are no privacy risks.

**Data Licensing**: Dataset and code to be released under CC-BY-SA license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
