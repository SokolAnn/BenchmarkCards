# MMR (Multi-target and Multi-granularity Reasoning)

## 📊 Benchmark Details

**Name**: MMR (Multi-target and Multi-granularity Reasoning)

**Overview**: The MMR dataset provides 194K complex and implicit question-answer pairs that cover multi-target, object-level, and part-level reasoning segmentation, enhancing diverse and context-aware interactions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ReasonSeg
- MUSE

**Resources**:
- [GitHub Repository](https://github.com/jdg900/MMR)

## 🎯 Purpose and Intended Users

**Goal**: To overcome the limitations of current reasoning segmentation datasets by addressing both multi-target and part-level reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reasoning Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: PACO-LVIS dataset

**Size**: 194,398 question-answer pairs

**Format**: JSON

**Annotation**: Generated using GPT-4V API with oversight from human inspectors

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- gIoU
- cIoU

**Calculation**: The overall loss is formulated as a combination of text generation loss and mask generation loss.

**Interpretation**: Higher gIoU and cIoU scores indicate better segmentation performance.

**Baseline Results**: M2SA-7B outperforms various baseline models in multi-target and multi-granularity reasoning segmentation tasks.

**Validation**: Data quality validated through rigorous human inspection and filtering.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is constructed based on publicly available data, minimizing privacy concerns.

**Data Licensing**: Creative Commons Attribution 4.0 (CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
