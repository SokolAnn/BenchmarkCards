# Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models

## 📊 Benchmark Details

**Name**: Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models

**Overview**: This paper examines logical preference consistency in Large Language Models (LLMs), proposing a universal evaluation framework based on three properties: transitivity, commutativity, and negation invariance. It introduces a data refinement and augmentation technique called REPAIR to enhance logical consistency.

**Data Type**: pairwise comparison data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.02205)

## 🎯 Purpose and Intended Users

**Goal**: To improve logical preference consistency in LLMs for enhanced reliability and trustworthiness in decision-making applications.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Preference Ranking
- Logical Consistency Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Datasets used include SummEval, NovelEval, and CaTeRS for measuring logical consistency in various tasks.

**Size**: 30,000 pairs after augmentation

**Format**: N/A

**Annotation**: Generated from pairwise human evaluations of summary candidates and document relevance.

## 🔬 Methodology

**Methods**:
- Pairwise comparisons
- Logical consistency evaluation metrics
- REPAIR framework

**Metrics**:
- Transitivity
- Commutativity
- Negation Invariance

**Calculation**: Metrics are calculated using defined logical relations and evaluated through pairwise comparison consistency.

**Interpretation**: Higher values in transitivity and commutativity indicate better logical consistency and objective alignment with human preferences.

**Baseline Results**: N/A

**Validation**: Results validated through comparisons against human judgement and diverse LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Logical inconsistencies in decision-making can lead to erroneous conclusions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
