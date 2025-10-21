# ALIGN BENCH

## 📊 Benchmark Details

**Name**: ALIGN BENCH

**Overview**: ALIGN BENCH is a comprehensive multi-dimensional benchmark for evaluating LLMs’ alignment in Chinese, designed to fill the gap in effective alignment evaluation for emerging Chinese LLMs by creating a human-in-the-loop data curation pipeline and automating the evaluation with an LLM-as-Judge approach.

**Data Type**: real-scenario usage inquiries

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- CMMLU

**Resources**:
- [GitHub Repository](https://github.com/THUDM/AlignBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the alignment capabilities of different large language models (LLMs) in handling real-world user scenarios in Chinese.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Mathematics
- Open-ended Questions
- Logical Reasoning
- Writing Ability
- Task-oriented Role Play
- Professional Knowledge

**Limitations**: N/A

## 💾 Data

**Source**: Real-user scenario queries collected through a human-in-the-loop pipeline.

**Size**: 683 examples

**Format**: N/A

**Annotation**: Human-verified references provided for each query.

## 🔬 Methodology

**Methods**:
- LLM-as-Judge
- Human evaluation
- Automated metrics

**Metrics**:
- Factual Correctness
- User Satisfaction
- Logical Coherence
- Completeness

**Calculation**: Scores from evaluations are aggregated from multi-dimensional assessments against human-verified references.

**Interpretation**: Scores reflect a dimensional analysis of model performance on various tasks, where higher scores indicate better alignment with human intentions.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
