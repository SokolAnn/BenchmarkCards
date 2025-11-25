# MC-MKE (Multimodal Knowledge Editing)

## 📊 Benchmark Details

**Name**: MC-MKE (Multimodal Knowledge Editing)

**Overview**: MC-MKE is a fine-grained multimodal knowledge editing benchmark that emphasizes modality consistency to evaluate the performance of various knowledge editing methods on correcting misreading and misrecognition errors in multimodal large language models.

**Data Type**: multimodal knowledge editing data

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMEdit
- KEBench
- MIKE

**Resources**:
- [Resource](https://arxiv.org/abs/2406.13219)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and fine-grained evaluation of multimodal knowledge editing methods, particularly focusing on consistency across different modalities.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Knowledge Editing

**Limitations**: Limited to the knowledge editing methods evaluated within the scope of this benchmark.

## 💾 Data

**Source**: Derived from MQuAKE with additional filtering and multimodal knowledge pairing.

**Size**: 111,904 examples for training, 44,118 examples for testing

**Format**: Custom multimodal format combining visual and textual edits.

**Annotation**: Automated generation with validation by large language models.

## 🔬 Methodology

**Methods**:
- Human assessment of knowledge edits
- Automated metrics for reliability, locality, generality, and consistency

**Metrics**:
- Reliability
- Locality
- Generality
- Consistency

**Calculation**: Performance is measured based on the success of edits for different multimodal knowledge components.

**Interpretation**: High scores indicate successful and consistent editing across modalities.

**Baseline Results**: Comparison against previously established benchmarks like MMEdit and KEBench.

**Validation**: Validated through extensive testing across various multimodal knowledge editing scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
