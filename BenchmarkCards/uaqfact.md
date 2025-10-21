# UAQFact

## 📊 Benchmark Details

**Name**: UAQFact

**Overview**: UAQFact is a bilingual dataset designed to evaluate LLMs’ ability to handle unanswerable questions (UAQs) by providing auxiliary factual knowledge. It supports two new tasks measuring the utilization of internal and external factual knowledge.

**Data Type**: unanswerable question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/cytan17726/UAQ_Fact)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' ability to utilize factual knowledge when handling unanswerable questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Discriminating between Unanswerable Questions and Answerable Questions
- Evaluating LLMs’ ability to utilize internal factual knowledge in handling UAQ
- Evaluating LLMs’ ability to utilize external factual knowledge in handling UAQ

**Limitations**: N/A

## 💾 Data

**Source**: Generated from a Knowledge Graph, specifically sampled factual triples from Wikidata.

**Size**: 13,970 questions

**Format**: N/A

**Annotation**: Questions generated using templates that incorporate factual knowledge.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Refusal Rate
- Accuracy
- Knowledge Pass Rate (KPR)
- Knowledge-aware Refusal Rate (KRR)

**Calculation**: Refusal rates are calculated using lexical matching based on key indicators of denial, while accuracy is measured via exact match against the provided answer list.

**Interpretation**: Higher refusal rates and lower accuracy indicate challenges in handling UAQs effectively. Improved KRR indicates better utilization of factual knowledge.

**Baseline Results**: N/A

**Validation**: Manual inspection confirmed 99.2% of questions meet quality standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
