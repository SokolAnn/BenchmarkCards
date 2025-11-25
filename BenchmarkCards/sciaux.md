# SciAux

## 📊 Benchmark Details

**Name**: SciAux

**Overview**: The SciAux dataset is designed to evaluate LLM reasoning under controlled informational stress by providing a set of helpful, irrelevant, and misleading context snippets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/billhdzhao/SciAux)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the reasoning capabilities of large language models under various types of auxiliary information.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the ScienceQA dataset by augmenting questions with auxiliary information.

**Size**: 6,828 examples

**Format**: JSON

**Annotation**: Generated additional information snippets using a language model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of questions for which the model correctly identified the index of the right answer among the multiple-choice options.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of the model in discerning helpful from misleading information.

**Validation**: Performance compared under controlled conditions with various auxiliary information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
