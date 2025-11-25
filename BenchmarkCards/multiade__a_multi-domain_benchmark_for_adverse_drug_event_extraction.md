# MultiADE: A Multi-domain benchmark for Adverse Drug Event extraction

## 📊 Benchmark Details

**Name**: MultiADE: A Multi-domain benchmark for Adverse Drug Event extraction

**Overview**: MultiADE is a multi-domain benchmark for adverse drug event extraction comprising several existing datasets sampled from different text types along with a newly created dataset CADECv2.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CADEC
- n2c2
- MADE
- PHEE
- PsyTAR

**Resources**:
- [Resource](https://data.csiro.au/collection/csiro:62387)

## 🎯 Purpose and Intended Users

**Goal**: To build a single model for adverse drug event extraction that works well on various text types.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Named Entity Recognition

**Limitations**: The generalisation of the trained models is far from perfect, making it infeasible to deploy models across different text types.

## 💾 Data

**Source**: Existing datasets from previous adverse drug event extraction works and a newly created dataset CADECv2.

**Size**: 3,548 online posts, 1,250 CADEC posts, 505 n2c2 summaries, 1,089 MADE records, 4,827 PHEE articles, and 3,147 PsyTAR posts.

**Format**: N/A

**Annotation**: Annotated by human annotators following detailed annotation guidelines.

## 🔬 Methodology

**Methods**:
- Fine-tuned span-based models
- LLM with in-context learning

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 scores calculated based on model predictions and ground truth annotations.

**Interpretation**: Higher F1 scores indicate better model performance on the task.

**Validation**: Tested against multiple datasets and compared using cross-domain generalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
