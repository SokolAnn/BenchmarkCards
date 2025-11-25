# ChronoSense

## 📊 Benchmark Details

**Name**: ChronoSense

**Overview**: ChronoSense is a new benchmark for evaluating LLMs’ temporal understanding, including 16 tasks that identify the Allen relation between two temporal events and temporal arithmetic.

**Data Type**: True/False question pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TimeBench
- TGQA
- TRACIE
- TEMPREASON
- TRAM

**Resources**:
- [GitHub Repository](https://github.com/duyguislakoglu/chronosense)

## 🎯 Purpose and Intended Users

**Goal**: Assess LLMs’ ability to compare event timelines using Allen relations and perform temporal arithmetic.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Temporal Reasoning
- Temporal Arithmetic

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata

**Size**: 5,000 examples

**Format**: N/A

**Annotation**: Extracted from real-world event pairs

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the ratio of correct answers to total questions for temporal understanding tasks.

**Interpretation**: A higher accuracy indicates better performance in understanding temporal relationships and arithmetic.

**Baseline Results**: N/A

**Validation**: Evaluated on standard LLMs across various prompting strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
