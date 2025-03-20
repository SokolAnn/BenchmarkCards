# M-HalDetect

## 📊 Benchmark Details

**Name**: M-HalDetect

**Overview**: M-HalDetect is a Multimodal Hallucination Detection Dataset designed to benchmark models for hallucination detection and prevention, consisting of fine-grained annotations on Visual Question Answering (VQA) examples.

**Data Type**: Image descriptions

**Domains**:
- Visual Question Answering

**Languages**:
- English

**Similar Benchmarks**:
- LRV dataset

**Resources**:
- [GitHub Repository](https://github.com/hendryx-scale/mhal-detect)

## 🎯 Purpose and Intended Users

**Goal**: To reduce hallucinations in large vision language models.

**Target Audience**:
- Research community
- Developers of vision-language models

**Tasks**:
- Hallucination detection
- Model optimization for hallucination prevention

**Limitations**: Improvements in hallucination rates may lead to less informative descriptions.

**Out of Scope Uses**:
- Non-VQA tasks
- Use with non-multimodal models

## 💾 Data

**Source**: COCO validation set (val2014)

**Size**: 16,000 annotation pairs

**Format**: Image-description pairs

**Annotation**: Fine-grained annotations at sub-sentence level.

## 🔬 Methodology

**Methods**:
- Fine-grained Direct Preference Optimization (FDPO)
- Rejection sampling

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Computed based on classification metrics.

**Interpretation**: Evaluated through correlation with human ratings.

**Validation**: Evaluated on a separate validation set of 50 images.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination risk

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
