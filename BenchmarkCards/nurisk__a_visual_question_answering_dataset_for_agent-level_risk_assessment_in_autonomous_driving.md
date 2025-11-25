# NuRisk: A Visual Question Answering Dataset for Agent-Level Risk Assessment in Autonomous Driving

## 📊 Benchmark Details

**Name**: NuRisk: A Visual Question Answering Dataset for Agent-Level Risk Assessment in Autonomous Driving

**Overview**: NuRisk is a comprehensive Visual Question Answering (VQA) dataset comprising 2.9K scenarios and 1.1M agent-level samples, built on real-world data from nuScenes and Waymo, completed with safety-critical scenarios from the CommonRoad simulator, enabling spatio-temporal reasoning.

**Data Type**: image-sequence with risk annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- nuScenes
- Waymo Open Motion
- CommonRoad

**Resources**:
- [Resource](https://NuRisk.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enable agent-level quantitative risk reasoning in autonomous driving through a comprehensive VQA dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from nuScenes, Waymo scenarios, and synthetic scenarios from the CommonRoad simulator.

**Size**: 2.9K scenarios and 1.1M agent-level samples

**Format**: N/A

**Annotation**: Physics-based risk annotations based on distance to collision and time to collision metrics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Mean Absolute Error (MAE) for risk predictions; Quadratic Weighted Kappa (QWK) for agreement; standard metrics for evaluation.

**Interpretation**: Lower MAE and higher QWK indicate better performance in risk assessment.

**Baseline Results**: Peak accuracy of proprietary models was 33%, improved to 41% with fine-tuned models.

**Validation**: Validation through automated quality checks and human validation on sampled data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
