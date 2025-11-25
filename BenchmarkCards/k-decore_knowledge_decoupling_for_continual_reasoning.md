# K-DECORE (Knowledge DEcoupling for COntinual REasoning)

## 📊 Benchmark Details

**Name**: K-DECORE (Knowledge DEcoupling for COntinual REasoning)

**Overview**: K-DECORE is a novel framework for Continual Structured Knowledge Reasoning (CSKR) that addresses various challenges of catastrophic forgetting and parameter growth across heterogeneous structured knowledge environments by leveraging knowledge decoupling, enabling efficient knowledge transfer across diverse tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- ComplexWebQuestions (CWQ)
- GrailQA
- MTOP

**Resources**:
- [Resource](https://arxiv.org/abs/2509.16929v2)

## 🎯 Purpose and Intended Users

**Goal**: To propose a continual framework for structured knowledge reasoning that facilitates knowledge transfer across diverse tasks while mitigating issues like catastrophic forgetting.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Structured Knowledge Reasoning

**Limitations**: Due to time and cost constraints, reasoning-based LLMs (like QWQ 32B) were not employed as the backbone for the framework.

## 💾 Data

**Source**: Four structured knowledge reasoning benchmarks curated for experimental tasks.

**Size**: 4 datasets

**Format**: Various formats depending on the dataset (e.g., JSON, SQL queries for DB reasoning, SPARQL queries for KG reasoning)

**Annotation**: The data has been extracted from structured knowledge benchmarks.

## 🔬 Methodology

**Methods**:
- Evaluation against existing continual learning methods and baselines

**Metrics**:
- Accuracy
- BWT (Backward Transfer)
- FWT (Forward Transfer)

**Calculation**: Metrics are calculated based on the accuracy scores from various tasks before and after training.

**Interpretation**: Higher accuracy indicates better performance while lower forgetting rates (BWT) and higher knowledge transfer (FWT) suggest more effective continual learning.

**Baseline Results**: K-DECORE shows superior performance compared to multiple state-of-the-art continual learning methods.

**Validation**: Extensive experiments conducted over multiple metrics across different structured knowledge reasoning tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
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
