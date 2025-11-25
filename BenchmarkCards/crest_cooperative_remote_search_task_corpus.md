# CReST (Cooperative Remote Search Task) Corpus

## 📊 Benchmark Details

**Name**: CReST (Cooperative Remote Search Task) Corpus

**Overview**: This paper introduces a novel two-step framework leveraging large language models (LLMs) for generating annotations of team dialogues to track shared mental models (SMMs) and detect discrepancies in team member mental states. It presents a dataset of human and LLM annotations and a reproducible evaluation framework for SMM coherence.

**Data Type**: dialogue annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the Theory of Mind (ToM) capabilities of large language models by assessing their ability to annotate and detect discrepancies in team dialogues.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Annotation of Mental States
- Discrepancy Detection

**Limitations**: N/A

## 💾 Data

**Source**: CReST corpus consisting of task-based dialogues from human teams engaged in search tasks.

**Size**: 30 annotated dialogues with 1,142 utterances

**Format**: JSON

**Annotation**: Annotated by naive LLMs and humans; includes belief, goal, and commitment updates.

## 🔬 Methodology

**Methods**:
- LLM-based Annotation
- Discrepancy Analysis

**Metrics**:
- Weighted Discrepancy Score

**Calculation**: Discrepancies are categorized and counted based on types (belief contradictions, omissions, unsupported beliefs, false beliefs) for each model and dialogue.

**Interpretation**: Higher scores indicate better alignment with ground truth annotations, meaning fewer discrepancies.

**Baseline Results**: N/A

**Validation**: Discrepancy validation analyses revealed LLMs' performances in identifying discrepancies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

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
