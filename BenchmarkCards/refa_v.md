# RefA V

## 📊 Benchmark Details

**Name**: RefA V

**Overview**: RefA V is a large-scale dataset of 10,000 diverse natural language queries that describe complex multi-agent interactions relevant to motion planning derived from 1000 driving logs in the Argoverse 2 Sensor dataset. It evaluates a model’s ability to find a visual 'needle in a haystack'.

**Data Type**: natural language queries

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- nuScenes
- KITTI

**Resources**:
- [GitHub Repository](https://github.com/cainand/RefAV)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate scenario mining methods using vision-language models on 3D scene understanding and spatio-temporal localization.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Scenario Mining
- Referential Multi-Object Tracking

**Limitations**: The quality of the scenario mining dataset is limited by the quality of the ground truth perception labels in AV2.

## 💾 Data

**Source**: Argoverse 2 (AV2) Sensor dataset

**Size**: 10,000 queries

**Format**: N/A

**Annotation**: Combination of manual annotations and procedural generation using large language models (LLMs).

## 🔬 Methodology

**Methods**:
- Referential Tracking by Program Synthesis (RefProg)
- Track Filtering by Referred Class
- Referential Track Inflation
- Referential Track Classification

**Metrics**:
- HOTA
- HOTA-Temporal
- HOTA-Track
- Log Balanced Accuracy
- Timestamp Balanced Accuracy

**Calculation**: Metrics are calculated by evaluating the accuracy of object detection, association, and localization against ground truth.

**Interpretation**: Higher HOTA values indicate better tracking performance.

**Baseline Results**: RefProg achieved significant improvements over traditional methods, indicating effectiveness in scenario mining.

**Validation**: Validation conducted through manual inspection of true positive log-prompt matches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
