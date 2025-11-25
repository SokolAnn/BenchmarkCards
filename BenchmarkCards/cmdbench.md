# CMDBench

## 📊 Benchmark Details

**Name**: CMDBench

**Overview**: CMDBench is a benchmark modeling the complexity of enterprise data platforms that evaluates coarse- and fine-grained data discovery and task execution performance for multimodal data retrievers in compound AI systems.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Data Management

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/CMDBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multimodal discovery performance of data retrievers in compound AI systems operating on siloed enterprise data.

**Target Audience**:
- Research Scientists
- Industry Practitioners
- Data Analysts

**Tasks**:
- Data Discovery
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from Wikipedia documents, WikiSQL tables, and Wikidata for knowledge graphs in the NBA domain.

**Size**: 8314 documents, 1076 tables, 6265 nodes and 21556 relations

**Format**: N/A

**Annotation**: Manual verification and annotation of questions and sources by the authors.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- R-precision

**Calculation**: Metrics calculated based on the performance of retrieval models against ground truth sources.

**Interpretation**: Higher accuracy and R-precision indicate better discovery and task performance.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through manual annotation and cross-verification of task questions and answers by multiple authors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
