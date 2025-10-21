# A Benchmark for the Detection of Metalinguistic Disagreements between LLMs and Knowledge Graphs

## 📊 Benchmark Details

**Name**: A Benchmark for the Detection of Metalinguistic Disagreements between LLMs and Knowledge Graphs

**Overview**: The paper proposes a benchmark for evaluating the detection of factual and metalinguistic disagreements between LLMs and knowledge graphs.

**Data Type**: fact-checking instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SHROOM
- WildHallucinations

**Resources**:
- [GitHub Repository](https://github.com/bradleypallen/trex-metalinguistic-disagreement)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark for assessing metalinguistic disagreements between LLMs and knowledge graphs.

**Target Audience**:
- ML Researchers
- Knowledge Engineers

**Tasks**:
- Fact Checking

**Limitations**: N/A

## 💾 Data

**Source**: T-REx knowledge alignment dataset

**Size**: 250 triples

**Format**: JSON

**Annotation**: Human-annotated examples for metalinguistic disagreement detection

## 🔬 Methodology

**Methods**:
- Zero-shot classification
- Human evaluation

**Metrics**:
- Accuracy
- False negative rate

**Calculation**: Calculated based on the agreement between LLM outputs and annotated examples.

**Interpretation**: Indicators of metalinguistic disagreement versus factual disagreement.

**Baseline Results**: N/A

**Validation**: Need for human validation of LLM defined disagreements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
