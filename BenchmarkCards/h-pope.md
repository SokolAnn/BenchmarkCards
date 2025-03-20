# H-POPE

## 📊 Benchmark Details

**Name**: H-POPE

**Overview**: H-POPE is a coarse-to-fine-grained benchmark that systematically assesses hallucination in object existence and attributes in large vision-language models (LVLMs). It builds on the existing POPE framework to include evaluations on the fine-grained details, specifically how LVLMs may hallucinate attributes of objects depicted in images.

**Data Type**: Images and attributes

**Domains**:
- Vision-language models

**Languages**:
- N/A

**Similar Benchmarks**:
- CHAIR
- POPE

**Resources**:
- [Resource](LSA dataset)
- [Resource](MSCOCO dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations regarding object existence and attributes in large vision-language models.

**Target Audience**:
- Researchers in AI and machine learning
- Developers of vision-language models

**Tasks**:
- Assessing hallucination in LVLMs
- Evaluating model accuracy on object and attribute recognition

**Limitations**: Only a few types of attributes are considered; mutual exclusion in attributes limits the extension to some attribute types.

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: MSCOCO (val. 2014) dataset and LSA dataset

**Size**: 994 images for random, popular, and frequency-based adversarial sampling; 926 images for image-based adversarial sampling.

**Format**: Images and attribute annotations

**Annotation**: Includes ground-truth objects and attributes, leveraging datasets for comprehensive evaluation.

## 🔬 Methodology

**Methods**:
- Hierarchical probing with coarse and fine-grained questions
- Negative sampling strategies for objects and attributes

**Metrics**:
- Accuracy
- F1-score
- Precision
- Recall

**Calculation**: Computed via binary classification metrics across various sampling strategies.

**Interpretation**: Models evaluated on how accurately they can identify the presence of objects and their attributes.

**Validation**: Internal consistency checked by comparing performance with and without context.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination
- Model performance reliability

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
