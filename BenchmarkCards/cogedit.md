# CogEdit

## 📊 Benchmark Details

**Name**: CogEdit

**Overview**: CogEdit is a novel benchmark designed to evaluate MLLMs’ meta-cognitive knowledge editing abilities across three levels: Counterfactual-Driven Editing, Boundary Constraint Editing, and Noise-Robust Editing.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.05714)

## 🎯 Purpose and Intended Users

**Goal**: To assess the meta-cognitive capabilities of multimodal knowledge editing.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Meta-cognitive Editing

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various multimodal QA datasets, specifically 1,174 VQA questions spanning sports, arts, science, and everyday activities.

**Size**: 1,174 examples

**Format**: N/A

**Annotation**: Manual data curation and validation processes were employed.

## 🔬 Methodology

**Methods**:
- Evaluation of editing success under various conditions

**Metrics**:
- Reliability
- Generality
- Locality
- Fidelity
- Adaptability
- Compliance
- Clarity@K

**Calculation**: Each metric is calculated based on the model's ability to maintain accuracy and adapt to edits under specific scenarios.

**Interpretation**: Higher scores indicate better performance in accurately maintaining knowledge and adapting to new inputs under various constraints.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
