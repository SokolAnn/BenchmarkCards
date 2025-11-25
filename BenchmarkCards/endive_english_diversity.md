# ENDIVE (English Diversity)

## 📊 Benchmark Details

**Name**: ENDIVE (English Diversity)

**Overview**: ENDIVE is a benchmark designed to evaluate five large language models across 12 natural language understanding tasks translated into five underrepresented dialects, highlighting performance disparities and promoting fairness in NLP.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- Multi-VALUE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating dialectal robustness in large language models across diverse NLP tasks.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Language Model Developers

**Tasks**:
- Natural Language Understanding
- Algorithmic Reasoning
- Mathematics
- Logic

**Limitations**: ENDIVE's selected tasks do not cover all aspects of dialectal variation.

## 💾 Data

**Source**: Derived from 12 established datasets covering various reasoning categories.

**Size**: 12 tasks across 5 dialects

**Format**: N/A

**Annotation**: Human evaluation and few-shot prompting with examples from eWAVE.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM preference tests

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE Diversity Score

**Calculation**: Metrics are calculated based on comparisons of responses to dialectal and Standard American English (SAE) inputs.

**Interpretation**: Higher scores indicate better performance on dialectal tasks compared to SAE.

**Baseline Results**: Established baseline comparisons against Multi-VALUE's rule-based translations.

**Validation**: Validation through human assessments of translation quality and fluency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of dialect-specific performance disparities.

**Potential Harm**: ['Perpetuation of biases against non-standard dialects']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
