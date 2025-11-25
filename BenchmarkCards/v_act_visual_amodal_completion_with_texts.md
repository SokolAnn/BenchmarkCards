# V ACT (Visual Amodal Completion with Texts)

## 📊 Benchmark Details

**Name**: V ACT (Visual Amodal Completion with Texts)

**Overview**: V ACT is a benchmark designed to evaluate the inference capabilities of large vision-language models on text-based tasks related to amodal completion. It uses a two-choice question–answer format, classifying amodal completion scenarios based on Basic Formal Ontology.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Japanese
- English

**Resources**:
- [Resource](https://www.biorxiv.org/content/early/2024/07/10/2024.07.07.602347)

## 🎯 Purpose and Intended Users

**Goal**: The goal of the V ACT benchmark is to identify strengths and weaknesses in LVLMs' understanding of amodal completion through a systematic classification of perceptual descriptions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Image data were sourced from Pixabay, with additional modifications and extensions of a previous dataset from Nishida et al. (2024).

**Size**: 122 questions

**Format**: N/A

**Annotation**: The dataset was annotated based on Basic Formal Ontology categories corresponding to the entities being amodally completed.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Zero-shot evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the number of correctly answered questions divided by the total number of questions.

**Interpretation**: Higher accuracy reflects better understanding and interpretation of amodal completions.

**Baseline Results**: Baseline results were compared against human accuracy rates.

**Validation**: The benchmark was validated through human responses, ensuring that correct answers were easily identifiable.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
