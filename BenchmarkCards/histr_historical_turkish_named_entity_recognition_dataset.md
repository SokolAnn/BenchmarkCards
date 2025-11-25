# HisTR (Historical Turkish Named Entity Recognition Dataset)

## 📊 Benchmark Details

**Name**: HisTR (Historical Turkish Named Entity Recognition Dataset)

**Overview**: The first named entity recognition (NER) dataset for historical Turkish, consisting of 812 sentences annotated to identify PERSON and LOCATION entities from historical Turkish texts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Similar Benchmarks**:
- OTA-BOUN (Universal Dependencies Treebank for Historical Turkish)

**Resources**:
- [Resource](https://huggingface.co/datasets/bucolin/HisTR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational resource for named entity recognition in historical Turkish texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is created from historical sentences sampled from the Servet-i Funun journal and additional historical documents.

**Size**: 812 sentences

**Format**: CoNLL-2003 format

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Fine-tuning of transformer-based models

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the identified entities in the test datasets compared to manual annotations.

**Interpretation**: Higher precision indicates fewer false positives; higher recall indicates fewer false negatives.

**Validation**: Evaluated on development and test sets with cross-validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
