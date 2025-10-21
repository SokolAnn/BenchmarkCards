# Temporal Knowledge Graph Question Answering (TKGQA)

## 📊 Benchmark Details

**Name**: Temporal Knowledge Graph Question Answering (TKGQA)

**Overview**: The paper proposes a novel semantic-parsing-based framework called Prog-TQA for Temporal Knowledge Graph Question Answering (TKGQA), which leverages large language models for program generation and incorporates self-improvement strategies.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiTQ
- CronQuestions

**Resources**:
- [Resource](https://arxiv.org/abs/2404.01720)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the understanding of temporal questions in TKGQA through the Prog-TQA framework and improve performance in answering such questions.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MultiTQ and CronQuestions datasets

**Size**: 386,787 examples (MultiTQ), 350,000 examples (CronQuestions)

**Format**: N/A

**Annotation**: Manually annotated examples and program drafts

## 🔬 Methodology

**Methods**:
- Draft generation using in-context learning
- Linking and execution of generated programs

**Metrics**:
- Hits@1
- Hits@10

**Calculation**: Hits@1 is the proportion of queries where the correct answer is ranked first, and Hits@10 is the proportion where the correct answer is within the top ten results.

**Interpretation**: Higher Hits@1 and Hits@10 indicate better performance in answering questions correctly.

**Validation**: The framework's performance is validated against multiple baselines including embedding-based and semantic-parsing-based methods.

## ⚠️ Targeted Risks

**Risk Categories**:
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
