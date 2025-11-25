# PitVQA

## 📊 Benchmark Details

**Name**: PitVQA

**Overview**: PitVQA is a novel dataset specifically designed for Visual Question Answering (VQA) in endonasal pituitary surgery, comprising 25 procedural videos and extensive question-answer pairs spanning surgical aspects.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EndoVis18-VQA

**Resources**:
- [GitHub Repository](https://github.com/mobarakol/PitVQA)

## 🎯 Purpose and Intended Users

**Goal**: To improve intra-operative decision-making and facilitate intuitive surgeon-AI interaction using the PitVQA dataset.

**Target Audience**:
- Medical Researchers
- Surgeons
- Machine Learning Researchers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 25 procedural videos of endoscopic pituitary surgeries from The National Hospital of Neurology and Neurosurgery, London, UK.

**Size**: 884,242 question-answer pairs

**Format**: JSON

**Annotation**: Annotated collaboratively by 2 neurosurgical residents with operative experience and checked by an attending neurosurgeon.

## 🔬 Methodology

**Methods**:
- Balanced Accuracy
- F1 Score
- Accuracy

**Metrics**:
- Balanced Accuracy
- F1 Score
- Accuracy

**Calculation**: Balanced accuracy is computed by equally weighting the contribution of each class, particularly effective for imbalanced datasets.

**Interpretation**: Higher balanced accuracy indicates better model performance across various classes.

**Baseline Results**: Balanced accuracy of 58.82% on PitVQA dataset, showing improvements over previous models.

**Validation**: Validated against both the PitVQA dataset and EndoVis18-VQA dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patients provided informed consent, and the study was registered with the local governance committee.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all patients.

**Compliance With Regulations**: Not Applicable
