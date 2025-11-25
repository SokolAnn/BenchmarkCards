# SETI (Systematicity Evaluation of Textual Inference)

## 📊 Benchmark Details

**Name**: SETI (Systematicity Evaluation of Textual Inference)

**Overview**: SETI offers three different NLI tasks and corresponding datasets to evaluate various types of systematicity in reasoning processes for pre-trained language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2305.15045)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the systematicity capabilities of pre-trained language models in Natural Language Inference.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Inference

**Limitations**: SETI only considers veridical inference and natural inference. The benchmark can be flexibly extended to more varied reasoning patterns.

## 💾 Data

**Source**: Constructed from existing NLI datasets and experiments.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Standard accuracy is used to evaluate the PLMs on the SETI tasks.

**Interpretation**: High accuracy indicates strong systematicity generalization capabilities.

**Baseline Results**: Performance was evaluated on six widely used PLMs.

**Validation**: Test accuracy was compared across different training configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
