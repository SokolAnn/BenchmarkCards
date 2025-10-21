# CUTE (Character-level Understanding of Tokens Evaluation)

## 📊 Benchmark Details

**Name**: CUTE (Character-level Understanding of Tokens Evaluation)

**Overview**: We propose a new benchmark, CUTE, which features a collection of tasks designed to test the orthographic knowledge of LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian

**Similar Benchmarks**:
- LMentry

**Resources**:
- [GitHub Repository](https://github.com/Leukas/CUTE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Large Language Models on their understanding of token composition, orthographic similarity, and ability to manipulate text sequences.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spelling
- Orthographic Similarity
- Manipulation Tasks

**Limitations**: Performance of all models would increase after fine-tuning.

## 💾 Data

**Source**: Synthetic tasks generated from existing corpora and frequency datasets.

**Size**: 1000 tasks

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Few-shot prompting
- Prompt-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Percentage of correct responses for each task.

**Interpretation**: Higher accuracy indicates better understanding of orthographic knowledge.

**Validation**: Tested on multiple state-of-the-art LLMs ranging from 7B to 132B parameters.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of performance for English and Russian models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
