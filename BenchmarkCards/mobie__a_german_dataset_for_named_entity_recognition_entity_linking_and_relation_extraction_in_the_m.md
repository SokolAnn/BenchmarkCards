# MobIE: A German Dataset for Named Entity Recognition, Entity Linking and Relation Extraction in the Mobility Domain

## 📊 Benchmark Details

**Name**: MobIE: A German Dataset for Named Entity Recognition, Entity Linking and Relation Extraction in the Mobility Domain

**Overview**: MobIE is a German-language dataset that combines annotations for Named Entity Recognition (NER), Entity Linking (EL), and Relation Extraction (RE) specifically in the context of mobility-related events such as traffic obstructions and public transport issues.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- German

**Resources**:
- [GitHub Repository](https://github.com/dfki-nlp/mobie)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the MobIE dataset is to facilitate joint and multi-task learning of fundamental information extraction tasks in the mobility domain, specifically for NER, EL, and RE.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Named Entity Recognition
- Entity Linking
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is collected from German Twitter messages and RSS feeds related to mobility events.

**Size**: 3,232 documents

**Format**: AVRO, JSONL

**Annotation**: Human-annotated with experts validating the labels and weakly-supervised annotations generated using the Snorkel framework.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Weak supervision

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated using standard evaluation methods for classification tasks.

**Interpretation**: High F1 scores and accuracy indicate better performance in entity recognition, linking, and relation extraction.

**Baseline Results**: N/A

**Validation**: The dataset includes a standard Train/Dev/Test split to ensure data quality for evaluating event extraction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is freely available under a CC-BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
