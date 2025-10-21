# FewVEX

## 📊 Benchmark Details

**Name**: FewVEX

**Overview**: FewVEX is a new dataset designed for entity-level Few-shot Visually-rich Document Entity Retrieval (VDER) tasks that reflects practical problems.

**Data Type**: document images with entity annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for Few-shot VDER tasks to facilitate research on task-personalized entity extraction.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Entity Recognition

**Limitations**: The derived dataset is based on the current open-source ones for document understanding, which are small in size and have a very limited amount of classes.

## 💾 Data

**Source**: Constructed from FUNSD and CORD datasets.

**Size**: 1,199 document images, containing 30 entity types.

**Format**: N/A

**Annotation**: Annotations based on entities present in the documents, focusing on few-shot occurrences.

## 🔬 Methodology

**Methods**:
- Meta-learning based methods
- Metric-based learning (ContrastProtoNet)
- Gradient-based learning (ANIL+HC)

**Metrics**:
- Precision
- Recall
- Micro F1-score
- AUROC

**Calculation**: Precision, recall and F1 score are calculated over meta-testing tasks, while AUROC is calculated based on in-task distribution (ITD) scores.

**Interpretation**: Higher F1 scores and AUROC indicate better performance and task specificity.

**Validation**: Evaluation is performed using meta-testing tasks generated from the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
