# CASE-Bench (Context-Aware Safety Benchmark)

## 📊 Benchmark Details

**Name**: CASE-Bench (Context-Aware Safety Benchmark)

**Overview**: CASE-Bench introduces a Context-Aware Safety Benchmark for evaluating large language models (LLMs) by integrating context into safety assessments, focusing on the responses to categorized queries. It aims to improve model safety alignments by considering various contexts in which queries are presented.

**Data Type**: query-context pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SORRY-Bench

**Resources**:
- [GitHub Repository](https://github.com/BriansIDP/CASEBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the context-aware safety judgment ability of large language models and to highlight the importance of context in LLM safety evaluations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from SORRY-Bench queries and supplemented with context generated and annotated by over 2000 participants.

**Size**: 900 query-context pairs with 47,000+ human annotations

**Format**: N/A

**Annotation**: Annotations were conducted by a diverse group of at least 21 annotators per task, employing statistical power analysis for sample size determination.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Statistical analysis

**Metrics**:
- Significance testing using z-test and Kruskal-Wallis test

**Calculation**: Determined based on the differences in human judgments across various context scenarios using statistical methods as mentioned.

**Interpretation**: Results indicate the substantial influence that context has on safety judgments made by LLMs.

**Baseline Results**: N/A

**Validation**: Power analysis was used to determine the required number of annotators in ensuring reliable safety judgment assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Decision bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Over-refusal leading to poor user experience in LLM interactions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from human annotators were anonymized, and privacy measures were in place.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all annotators prior to participation in the study.

**Compliance With Regulations**: Not Applicable
