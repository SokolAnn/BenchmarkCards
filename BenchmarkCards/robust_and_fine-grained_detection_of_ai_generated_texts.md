# Robust and Fine-Grained Detection of AI Generated Texts

## 📊 Benchmark Details

**Name**: Robust and Fine-Grained Detection of AI Generated Texts

**Overview**: This paper introduces a new dataset of over 2.4M human-LLM co-authored texts aimed at training models for token classification to detect machine-generated content.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Chinese
- Czech
- Dutch
- English
- French
- German
- Greek
- Hebrew
- Hindi
- Indonesian
- Italian
- Japanese
- Korean
- Persian
- Polish
- Portuguese
- Romanian
- Russian
- Spanish
- Turkish
- Ukrainian
- Vietnamese

**Similar Benchmarks**:
- CoAuthor
- MixSet
- RoFT
- MultiTude
- M4GTD
- Beemo

**Resources**:
- [Resource](https://raid-bench.xyz/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust dataset for detecting AI-generated texts across various domains and languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Token Classification

**Limitations**: No detector can guarantee 100% accuracy, and models are meant for human-in-the-loop scenarios.

## 💾 Data

**Source**: An extensive collection of human-machine co-authored texts from various popular LLMs.

**Size**: 2,447,221 examples

**Format**: N/A

**Annotation**: Automatically generated with human oversight where necessary.

## 🔬 Methodology

**Methods**:
- Token Classification

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the models' predictions and majority voting.

**Interpretation**: Higher metrics indicate better performance in detecting AI-generated content.

**Baseline Results**: F1 score of 0.79 against adversarial inputs.

**Validation**: Models were validated across unseen domains and generators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
