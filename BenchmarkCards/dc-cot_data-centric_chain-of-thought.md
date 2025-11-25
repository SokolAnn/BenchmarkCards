# DC-CoT (Data-Centric Chain-of-Thought)

## 📊 Benchmark Details

**Name**: DC-CoT (Data-Centric Chain-of-Thought)

**Overview**: DC-CoT is the first data-centric benchmark designed to investigate data manipulation in chain-of-thought (CoT) distillation from method, model, and data perspectives, systematically assessing the effectiveness of various distillation approaches.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQA
- CSQA
- ARC
- GSM8K
- MATH
- ANLI
- Webarena
- Visual-CoT

**Resources**:
- [Resource](https://arxiv.org/abs/2505.18759)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate how data-centric strategies improve the distillation of reasoning capabilities from larger models to smaller, more efficient student models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Textual Reasoning
- Agentic Reasoning
- Visual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Various reasoning datasets including SQA, CSQA, ARC, GSM8K, MATH, ANLI, and others.

**Size**: Multiple datasets with varying sizes, including 100,000+ examples for training.

**Format**: N/A

**Annotation**: Generated through various augmentation techniques and filtering methods.

## 🔬 Methodology

**Methods**:
- Data Augmentation
- Data Filtering
- Data Mixing

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on performance evaluations using various reasoning tasks.

**Interpretation**: Higher accuracy indicates better performance of the student models in reasoning tasks.

**Validation**: Extensive experiments across diverse teacher–student pairs, tasks, and datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Various licenses including MIT, Apache, CC BY-NC, etc.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
