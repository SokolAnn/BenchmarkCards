# MDER (Method and Dataset Entity Recognition)

## 📊 Benchmark Details

**Name**: MDER (Method and Dataset Entity Recognition)

**Overview**: The paper proposes a novel entity recognition model called MDER, which is able to extract method and dataset entities from the main textual content of scientific papers. It evaluates the model on datasets constructed from various research areas in computer science.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision
- Data Mining
- Artificial Intelligence

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2010.13583)

## 🎯 Purpose and Intended Users

**Goal**: To propose and evaluate a novel model for extracting method and dataset entities from scientific literature with effective performance across different domains.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Datasets constructed from published papers of four research areas in computer science.

**Size**: 2,800 sentences per dataset

**Format**: N/A

**Annotation**: Manually tagged by graduate students following a standard process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Calculated as per standard definitions for precision, recall, and F1 score based on predicted and annotated entities.

**Interpretation**: An entity is considered correctly predicted if the label of every character of the entity is correctly predicted.

**Baseline Results**: N/A

**Validation**: The model was validated using training, validation, and testing allocations of the constructed datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
