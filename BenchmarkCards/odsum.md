# ODSum

## 📊 Benchmark Details

**Name**: ODSum

**Overview**: ODSum is a novel dataset designed for Open-Domain Multi-Document Summarization (ODMDS) tasks, constructed from existing QMSum and SQuALITY datasets to better represent realistic querying needs.

**Data Type**: query-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuALITY
- QMSum

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/ODSum)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that reflects real-world challenges in retrieving and summarizing information across diverse document collections in ODMDS tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-Document Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing datasets SQuALITY and QMSum, along with a customized data collection pipeline.

**Size**: 1,190 documents for ODSum-story, 232 documents for ODSum-meeting

**Format**: JSON

**Annotation**: Queries and summaries were generated and reviewed by multiple annotators for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE
- BERTScore
- G-E VAL

**Calculation**: Metrics calculated based on word overlap for ROUGE and BERTScore; G-E VAL uses a contextual scoring based on LLM outputs.

**Interpretation**: Higher scores indicate better summarization quality, with G-E VAL providing a more nuanced evaluation of retrieval impact.

**Validation**: Extensive experiments comparing different retrieval and summarization strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
