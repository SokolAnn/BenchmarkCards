# ComprehendEdit

## 📊 Benchmark Details

**Name**: ComprehendEdit

**Overview**: ComprehendEdit is a comprehensive benchmark comprising eight diverse tasks from multiple datasets to evaluate multimodal knowledge editing techniques. It introduces two novel metrics: Knowledge Generalization Index (KGI) and Knowledge Preservation Index (KPI) to address current evaluation limitations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMEdit
- KEBench

**Resources**:
- [GitHub Repository](https://github.com/yaohui120/ComprehendEdit)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for multimodal knowledge editing and establish a baseline method.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Recognition
- Object Attributes
- Object Counting
- Object Existence
- Scene Information
- Spatial Relationship
- Text Recognition
- Numerical Inference

**Limitations**: N/A

## 💾 Data

**Source**: Multiple datasets including GQA, TallyQA, VSR, TextVQA, and MathVista.

**Size**: 17,932 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Hierarchical In-Context Editing (HICE)

**Metrics**:
- Knowledge Generalization Index (KGI)
- Knowledge Preservation Index (KPI)

**Calculation**: Metrics are calculated based on model performance before and after editing using defined indicators.

**Interpretation**: KGI assesses the improvement on previously misclassified samples, while KPI evaluates correctness on previously correct samples post-editing.

**Validation**: The benchmark validates editing techniques across multiple metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
