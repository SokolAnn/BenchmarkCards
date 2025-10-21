# PBLBench

## 📊 Benchmark Details

**Name**: PBLBench

**Overview**: PBLBench is a novel benchmark designed to evaluate complex reasoning grounded in domain-specific knowledge and long-context understanding for STEM-based Project-Based Learning (PBL) outcomes.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Education
- Science
- Technology
- Engineering
- Mathematics

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- STEM
- SCIENCEQA

**Resources**:
- [Resource](https://arxiv.org/abs/2505.17050)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of state-of-the-art multimodal large language models (MLLMs) in assessing multi-modal STEM-based Project-Based Learning outcomes.

**Target Audience**:
- ML Researchers
- Educators
- AI Developers

**Tasks**:
- Project Evaluation
- Complex Reasoning

**Limitations**: The overall scale of the dataset remains limited, necessitating the collection of additional samples.

## 💾 Data

**Source**: Constructed from over 500 multimodal PBL projects.

**Size**: 500 projects

**Format**: N/A

**Annotation**: Evaluation criteria derived using the Analytic Hierarchy Process (AHP) with expert-driven pairwise comparisons.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Automated metrics

**Metrics**:
- Rank accuracy
- Average scores

**Calculation**: Rank accuracy calculated based on model's performance compared to human evaluators.

**Interpretation**: Models should closely match human scores to be considered effective.

**Baseline Results**: The highest ranked model achieved only 59% rank accuracy.

**Validation**: Results validated against human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: Models exhibit significant hallucinations and instability leading to inaccurate evaluations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
