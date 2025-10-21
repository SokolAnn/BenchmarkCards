# Cin´ easte: A Fine-grained Contextual Movie Question Answering Benchmark

## 📊 Benchmark Details

**Name**: Cin´ easte: A Fine-grained Contextual Movie Question Answering Benchmark

**Overview**: Cin´ easte is a comprehensive benchmark for long-form movie understanding, comprising 3,119 multiple-choice question-answer pairs derived from 1,805 scenes across 200 diverse movies, testing fine-grained contextual reasoning across five novel categories.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Infinibench
- MovieQA
- CinePile

**Resources**:
- [Resource](https://arxiv.org/abs/2509.14227)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diagnostic benchmark for assessing the capacity of multi-modal large language models in fine-grained contextual understanding of long-form movie content.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Scenes from 200 English-language movies sourced from the YouTube channel MovieClips.

**Size**: 3,119 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated with a two-stage filtering process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the percentage of correctly answered questions among all question-answer pairs.

**Interpretation**: Higher accuracy indicates better model performance in understanding complex, narrative-driven video content.

**Baseline Results**: The top-performing model, GPT-4o, achieved an average accuracy of 75.89%.

**Validation**: The benchmark was validated using automated filtering to ensure context dependency and factual correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
