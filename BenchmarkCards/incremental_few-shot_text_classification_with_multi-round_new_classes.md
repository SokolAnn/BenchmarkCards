# Incremental Few-shot Text Classification with Multi-round New Classes

## 📊 Benchmark Details

**Name**: Incremental Few-shot Text Classification with Multi-round New Classes

**Overview**: This work defines a new task in the NLP domain, incremental few-shot text classification, where the system incrementally handles multiple rounds of new classes with a limited number of labeled examples.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BANKING77
- FewRel

**Resources**:
- [GitHub Repository](https://github.com/congyingxia/IncrementalFSTC)

## 🎯 Purpose and Intended Users

**Goal**: To propose a new challenge in incremental few-shot text classification and to evaluate performance of models on this task.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Intent Detection
- Relation Classification

**Limitations**: N/A

## 💾 Data

**Source**: Created from the BANKING77 dataset for intent detection and FewRel for relation classification.

**Size**: 20 base classes, 50 new classes across 5 rounds, several thousand examples

**Format**: N/A

**Annotation**: Hand-annotated based on existing datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Model performance is evaluated based on accuracy and F1 score across different rounds and classes.

**Interpretation**: Higher scores indicate better classification performance across seen and unseen classes.

**Baseline Results**: Comparison with models like DNNC, Prototypical Network, DyFewShot.

**Validation**: N/A

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
