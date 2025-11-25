# PLACEIT3D

## 📊 Benchmark Details

**Name**: PLACEIT3D

**Overview**: PLACEIT3D is a benchmark for language-guided placement of 3D assets in real 3D scenes, enabling evaluation of multi-modal large language models (MLLMs) on this task, which involves handling one-to-many placement ambiguities, geometric reasoning, and language understanding.

**Data Type**: 3D placement examples

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ScanNet

**Resources**:
- [Resource](https://nianticlabs.github.io/placeit3d/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundation for evaluating and advancing multi-modal large language models (MLLMs) in the task of 3D object placement based on natural language instructions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Language-Guided Object Placement
- 3D Scene Understanding

**Limitations**: The benchmark currently focuses on placing objects on horizontal surfaces only and relies on synthetic rule-based optimization without complete human verification for edge cases.

## 💾 Data

**Source**: 3D reconstructed scenes from ScanNet and assets from PartObjaverse-Tiny.

**Size**: 100,505 training examples, 3,500 evaluation examples

**Format**: N/A

**Annotation**: Annotated with all valid placements that can be used for training MLLMs.

## 🔬 Methodology

**Methods**:
- Evaluation protocol comparing predicted placements against constraints
- Rule-based systems for checking validity of placements

**Metrics**:
- Global Constraint Accuracy
- Complete Placement Success
- Language Adherence Success

**Calculation**: Metrics are computed based on the percentage of constraints satisfied across the dataset.

**Interpretation**: Higher scores indicate better adherence to constraints and placement accuracy.

**Baseline Results**: PLACEWIZARD, the proposed method, outperforms baseline methods with improved accuracy in following language instructions.

**Validation**: Tested against the benchmark evaluation protocol.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
