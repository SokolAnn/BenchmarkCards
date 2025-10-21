# TMMLU (Taiwan Massive Multitask Language Understanding)

## 📊 Benchmark Details

**Name**: TMMLU (Taiwan Massive Multitask Language Understanding)

**Overview**: The proposed benchmarks assess the capabilities of tasks related to contextual question answering, world knowledge, summarization, classification, and table understanding. In terms of evaluating world knowledge, we further propose a new dataset - Taiwan Massive Multitask Language Understanding (TMMLU) - encompassing exams from high school entrance exams to vocational exams across 55 subjects in total.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Traditional Chinese

**Similar Benchmarks**:
- DRCD
- TTQA
- CMDQA
- FGC

**Resources**:
- [GitHub Repository](https://github.com/mtkresearch/MR-Models)

## 🎯 Purpose and Intended Users

**Goal**: To advance the evaluation of language models in Traditional Chinese and stimulate further research in this field.

**Target Audience**:
- ML Researchers
- Language Model Developers

**Tasks**:
- Contextual Question Answering
- Summarization
- Classification
- Table Understanding
- World Knowledge Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Existing Traditional Chinese and English datasets, specifically translated or adapted for Traditional Chinese.

**Size**: 55 subjects in total across multiple disciplines

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- ROUGE-2

**Calculation**: Metrics are calculated based on the evaluations of language models on specific tasks.

**Interpretation**: Higher scores in EM indicate better performance in question answering tasks, while ROUGE-2 scores indicate the quality of generated summaries.

**Baseline Results**: Model 7-C achieves performance comparable to GPT-3.5 on specific evaluated capabilities.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
