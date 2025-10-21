# Towards Inclusive NLP: Assessing Compressed Multilingual Transformers across Diverse Language Benchmarks

## 📊 Benchmark Details

**Name**: Towards Inclusive NLP: Assessing Compressed Multilingual Transformers across Diverse Language Benchmarks

**Overview**: This work benchmarks the performance of multilingual and monolingual Large Language Models (LLMs) across Arabic, English, and Indic languages, with particular emphasis on the effects of model compression strategies such as pruning and quantization.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- English
- Kannada

**Similar Benchmarks**:
- ArabicMMLU
- EnglishMMLU
- Kannada-ARC-C-2.5K

**Resources**:
- [Resource](https://huggingface.co/datasets/Indic-Benchmark/kannada-arc-c-2.5k)

## 🎯 Purpose and Intended Users

**Goal**: To provide rigorous cross-lingual evaluations of LLMs while focusing on the impact of compression strategies on their performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The study does not consider advanced pruning strategies nor human-annotated task evaluations.

## 💾 Data

**Source**: ArabicMMLU, EnglishMMLU, and Kannada-ARC-C-2.5K benchmarks

**Size**: 14,575 multiple-choice questions for ArabicMMLU, 15,908 questions for EnglishMMLU, and around 2,500 questions for Kannada-ARC-C-2.5K

**Format**: JSON, CSV

**Annotation**: Manually collected and curated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the ratio of correct responses in all tasks.

**Interpretation**: Accuracy measures the performance of the models across the benchmarks.

**Baseline Results**: BLOOMZ-7.1B achieved the highest accuracy at 41.7% in ArabicMMLU.

**Validation**: Performance was evaluated against controlled benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The study indicates challenges in producing equitable models across diverse languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
