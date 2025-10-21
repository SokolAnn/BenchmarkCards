# WINOVIS (WSC-Adapted Multimodal Dataset)

## 📊 Benchmark Details

**Name**: WINOVIS (WSC-Adapted Multimodal Dataset)

**Overview**: WINOVIS is a dataset designed to probe text-to-image models on pronoun disambiguation within multimodal contexts, consisting of 500 scenarios for evaluating these models' common-sense reasoning abilities.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- WSC (Winograd Schema Challenge)
- Winogrande
- KnowRef

**Resources**:
- [GitHub Repository](https://github.com/bpark2/WinoVis)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the pronoun disambiguation capabilities of text-to-image models and advance understanding of multimodal common-sense reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Pronoun Disambiguation

**Limitations**: Entity separation challenges can occur, particularly with semantically similar entities.

## 💾 Data

**Source**: Generated using GPT-4 with manual filtering.

**Size**: 500 scenarios

**Format**: JSON

**Annotation**: Manually reviewed for clarity and relevance for the disambiguation task.

## 🔬 Methodology

**Methods**:
- Manual Annotation
- Heatmap Analysis

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the model's pronoun-to-entity associations.

**Interpretation**: The results are interpreted in terms of model's ability to accurately associate pronouns with the correct entities.

**Validation**: The effectiveness of the dataset was validated through systematic evaluation against different model versions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

**Demographic Analysis**: Not explicitly analyzed.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
