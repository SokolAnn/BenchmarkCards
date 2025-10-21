# PET: An Annotated Dataset for Process Extraction from Natural Language Text Tasks

## 📊 Benchmark Details

**Name**: PET: An Annotated Dataset for Process Extraction from Natural Language Text Tasks

**Overview**: The paper presents the PET dataset, a corpus of business process descriptions annotated with activities, gateways, actors, and flow information, together with an annotation schema, guidelines, and baselines to benchmark the difficulty and challenges of business process extraction from text.

**Data Type**: text (annotated business process descriptions)

**Domains**:
- Natural Language Processing
- Business Process Management

**Resources**:
- [Resource](https://pdi.fbk.eu/pet-dataset)
- [Resource](https://huggingface.co/datasets/patriziobellan/PET)

## 🎯 Purpose and Intended Users

**Goal**: Provide a new reference corpus, annotation schema, and guidelines for annotating business process models in running text; and quantify the difficulty of fundamental information extraction tasks for process model extraction by deploying a variety of baselines on the annotated data.

**Target Audience**:
- Research community
- Natural Language Processing researchers
- Business Process Management researchers

**Tasks**:
- Information Extraction
- Named Entity Recognition
- Relation Extraction
- Process Model Extraction from Text

**Limitations**: N/A

## 💾 Data

**Source**: Collection of textual process descriptions initially used by Friedrich et al. [3]; annotated with process elements and relations according to the authors' annotation schema.

**Size**: 45 documents (413 sentences; average 9.27 sentences per document; average 18.15 words per sentence)

**Format**: N/A

**Annotation**: Manual annotation by three experts using the Inception tool, followed by an automatic rule-based annotation fixing step and a reconciliation phase to obtain a gold-standard annotation set.

## 🔬 Methodology

**Methods**:
- Conditional Random Fields (CRF) models
- Rule-Based (RB) approaches
- 5-fold cross-validation
- Inter-annotator agreement computation and reconciliation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics (Precision, Recall, F1) computed per entity and relation. CRF baseline results obtained via 5-fold cross-validation and averaged. Inter-annotator agreement measured using the F1 measure following the methodology in [4].

**Interpretation**: High Precision indicates correct detections while lower Recall indicates missed elements; F1 is used as an overall performance measure. Authors note that detection of all elements (recall) is more challenging than detecting elements correctly (precision).

**Baseline Results**: Inter-annotator agreement (entities) Overall F1 = 0.85; inter-annotator agreement (relations) Overall F1 = 0.81. Baseline 1 (CRF, entities) Overall F1 = 0.74. Baseline 2 (Rule-Based with gold entities, relations) Overall F1 = 0.90. Baseline 3 (CRF entities + Rule-Based relations) Overall F1 = 0.61.

**Validation**: Gold standard produced via inter-annotator agreement computation and reconciliation; baselines evaluated using 5-fold cross-validation with averaged results.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
