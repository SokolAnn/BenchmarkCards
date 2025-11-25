# EASG-Bench

## 📊 Benchmark Details

**Name**: EASG-Bench

**Overview**: EASG-Bench is a question-answering benchmark for egocentric videos where question-answer pairs are created from spatio-temporally grounded dynamic scene graphs, capturing actions and relationships among the camera wearer and objects.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EgoSchema
- EgoThink
- QAEgo4D
- MultiHop-EgoQA
- EgoTempo
- AMEGO

**Resources**:
- [GitHub Repository](https://github.com/fpv-iplab/EASG-bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing question answering in egocentric video contexts, focusing on temporal and spatial reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from Egocentric Action Scene Graphs (EASGs) using a robust filtering strategy.

**Size**: 1,807 question-answer pairs

**Format**: N/A

**Annotation**: Automatically generated with a multi-stage filtering process to ensure uniqueness and specificity.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge for answer evaluation
- Automated questions generation from EASGs

**Metrics**:
- Relative Score based on LLM performance

**Calculation**: Adjusted scores based on comparison to ground truth responses across multiple iterations.

**Interpretation**: Scores are given based on helpfulness, relevance, accuracy, and detail of answers.

**Baseline Results**: N/A

**Validation**: Results have been validated through comparison with various LLM models across defined question categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
