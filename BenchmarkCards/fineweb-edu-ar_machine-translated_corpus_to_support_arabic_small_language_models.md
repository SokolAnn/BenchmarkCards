# FineWeb-Edu-Ar (Machine-translated Corpus to Support Arabic Small Language Models)

## 📊 Benchmark Details

**Name**: FineWeb-Edu-Ar (Machine-translated Corpus to Support Arabic Small Language Models)

**Overview**: FineWeb-Edu-Ar is the largest publicly available machine-translated Arabic dataset created from the English FineWeb-Edu dataset to support the training of small language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- English

**Similar Benchmarks**:
- FineWeb-Edu

**Resources**:
- [Resource](https://huggingface.co/datasets/kaust-generative-ai/fineweb-edu-ar)

## 🎯 Purpose and Intended Users

**Goal**: To support the development of small language models for the Arabic language by providing a quality dataset through machine translation.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Machine Translation

**Limitations**: The dataset may contain inaccuracies due to translation errors and may not sufficiently cover culturally specific knowledge for Arabic-speaking countries.

## 💾 Data

**Source**: Machine-translated from the deduplicated English FineWeb-Edu dataset.

**Size**: 202B tokens

**Format**: JSONL

**Annotation**: Automatically generated through machine translation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Translation Accuracy
- Fluency
- Grammar and Syntax

**Calculation**: Utilizing the LLM-as-a-Judge approach for automatic assessment, with scores averaged from multiple evaluation passes.

**Interpretation**: Scores range from 0 to 24 based on accuracy, grammar, syntax, and fluency.

**Baseline Results**: N/A

**Validation**: Validation performed using a micro-benchmark with repeated evaluations across multiple models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
