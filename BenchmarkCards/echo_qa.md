# ECHO QA

## 📊 Benchmark Details

**Name**: ECHO QA

**Overview**: ECHO QA is a benchmark spanning scientific, factual, and commonsense knowledge aimed at testing how well large language models (LLMs) can integrate their internal parametric knowledge with external contextual knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/sitaocheng/Knowledge Interplay)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the interplay between parametric knowledge and contextual knowledge in large language models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: LLMs struggle to fully leverage their parametric knowledge when contextual knowledge is present.

## 💾 Data

**Source**: Adapted from existing datasets including ALCUNA, ConflictQA, MuSiQue, and OpenBookQA.

**Size**: N/A

**Format**: N/A

**Annotation**: Constructed knowledge is based on structured relationships and types designed for various reasoning scenarios.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Memorization Ratio
- Unknown Ratio

**Calculation**: Metrics are calculated based on the relationship between parametric knowledge and contextual knowledge, evaluating how well LLMs answered questions requiring both types of knowledge.

**Interpretation**: Accuracy reflects the model's correct answer rate; memorization ratio indicates how often the model recalls parametric knowledge, and unknown ratio shows the frequency of 'unknown' responses.

**Baseline Results**: N/A

**Validation**: Evaluated through human evaluations regarding the quality of constructed knowledge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
