# Colossal Clean Crawled Corpus (C4)

## 📊 Benchmark Details

**Name**: Colossal Clean Crawled Corpus (C4)

**Overview**: The paper provides documentation and analysis for the Colossal Clean Crawled Corpus (C4), which is a dataset created by applying a series of filters to a snapshot of the Common Crawl. It aims to inform the creation and documentation of web-scale datasets by providing insights about included and excluded data, provenance, and biases present in the text.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Common Crawl

**Resources**:
- [GitHub Repository](https://github.com/allenai/c4-documentation)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Colossal Clean Crawled Corpus (C4) documentation is to provide insights into the dataset's composition, the filtering processes it underwent, and how these affect data representation, usability, and biases.

**Target Audience**:
- ML Researchers
- Data Scientists
- Ethics Researchers

**Tasks**:
- Text Classification
- Natural Language Understanding

**Limitations**: The documentation highlights limitations related to representational harms and biases inherent in the dataset.

**Out of Scope Uses**:
- Using the dataset without considering biases and the impact of applied filters.

## 💾 Data

**Source**: Collected from a snapshot of the Common Crawl, filtered to remove non-English text and specific unwanted content.

**Size**: 2.3TB

**Format**: JSON

**Annotation**: Automatically processed with filters applied to remove undesirable content.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Document presence analysis
- Bias assessment

**Calculation**: Text was analyzed for sources, composition of included text, and biases associated with exclusions.

**Interpretation**: Analysis of biases and representational harms across different demographic identities present in the data.

**Baseline Results**: N/A

**Validation**: The dataset was validated through a comparative analysis with the original unfiltered Common Crawl data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The study provides evidence that texts associated with minority identities are disproportionately excluded due to filtering mechanisms.

**Potential Harm**: ['Representational harms by disproportionately affecting segments of the population in text representation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
