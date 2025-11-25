# HLB (Humanlikeness Benchmark)

## 📊 Benchmark Details

**Name**: HLB (Humanlikeness Benchmark)

**Overview**: This benchmark evaluates the humanlikeness of language models through 10 psycholinguistic experiments analyzing core linguistic aspects including sound, word, syntax, semantics, and discourse. It employs a comprehensive comparison between outputs from language models and human responses to assess the extent to which these models replicate human language patterns.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and comprehensive evaluation of how closely large language models align with human linguistic behavior.

**Target Audience**:
- ML Researchers
- Model Developers
- Psycholinguists

**Tasks**:
- Linguistic Evaluation

**Limitations**: While the benchmark covers a wide range of linguistic tasks, it may not encompass the full complexity of human language use.

## 💾 Data

**Source**: Responses collected from over 2,000 human participants and outputs from 20 large language models.

**Size**: 200,000 responses

**Format**: N/A

**Annotation**: Responses were analyzed using a coding algorithm that identifies language use patterns.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Humanlikeness score (HS) based on Jensen-Shannon divergence

**Calculation**: Humanlikeness scores are calculated by comparing response distributions between human participants and language models.

**Interpretation**: Scores reflect the degree of alignment between model outputs and human language patterns.

**Baseline Results**: Scores from human participants serve as the baseline for evaluation.

**Validation**: Responses validated through statistical methods to ensure accuracy of coding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of demographic factors, focusing on native English speakers from the UK and US.

**Potential Harm**: Identifying areas where models diverge from human-like language patterns, particularly in complex linguistic tasks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided consent prior to participating in the experiments.

**Compliance With Regulations**: Not Applicable
