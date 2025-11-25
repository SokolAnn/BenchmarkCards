# CETVEL

## 📊 Benchmark Details

**Name**: CETVEL

**Overview**: CETVEL is a comprehensive benchmark designed to evaluate large language models (LLMs) in Turkish. It addresses gaps in existing benchmarks by combining a broad range of both discriminative and generative tasks, ensuring content that reflects the linguistic and cultural richness of the Turkish language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Similar Benchmarks**:
- TurkishMMLU
- TR-MMLU
- TUMLU
- XGLUE
- XTREME

**Resources**:
- [GitHub Repository](https://github.com/KUIS-AI/cetvel)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CETVEL is to provide a culturally grounded evaluation suite for advancing the development and assessment of LLMs in Turkish.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Language Model Developers

**Tasks**:
- Extractive Question Answering
- Multiple Choice Question Answering
- Text Classification
- Natural Language Inference
- Summarization
- Machine Translation
- Grammatical Error Correction

**Limitations**: CETVEL is limited to open-weight models with up to 70B parameters; it does not include proprietary models restricted by API changes.

## 💾 Data

**Source**: A combination of publicly available datasets, specifically curated datasets, and adapted versions of existing datasets.

**Size**: 10,000 examples

**Format**: Various formats including JSON and CSV

**Annotation**: Crowdsourced and manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-2
- Exact Match

**Calculation**: Metrics are calculated based on standard performance measures tailored to each task type.

**Interpretation**: Higher scores indicate better model performance; specific thresholds for good vs. poor performance depend on task definitions.

**Baseline Results**: Llama-3.3-70B-Instruct provides the strongest overall performance across evaluated tasks.

**Validation**: The benchmark is validated through extensive experimental evaluations against a variety of LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: CETVEL includes assessments for model performance across diverse Turkish linguistic and cultural contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Most datasets are licensed under CC BY-SA, MIT, or other open licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
