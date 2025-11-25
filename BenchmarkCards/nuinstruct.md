# NuInstruct

## 📊 Benchmark Details

**Name**: NuInstruct

**Overview**: NuInstruct is a novel dataset with 91K multi-view video-QA pairs across 17 subtasks, designed to provide holistic information for autonomous driving by aligning language and driving logic.

**Data Type**: multi-view video question-answer pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Nuscenes-QA

**Resources**:
- [GitHub Repository](https://github.com/xmed-lab/NuInstruct)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive language-driving dataset that captures temporal, multi-view, and spatial interactions in autonomous driving scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Perception
- Prediction
- Risk
- Planning with Reasoning

**Limitations**: The current dataset lacks traffic light information and tasks related to 3D object detection.

## 💾 Data

**Source**: Constructed from the NuScenes dataset, consisting of 850 videos.

**Size**: 91,355 pairs

**Format**: JSON

**Annotation**: Generated using a novel SQL-based method for automated instruction-response pair generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Absolute Error (MAE)
- Accuracy
- Mean Average Precision (MAP)
- BLEU Score

**Calculation**: Metrics are calculated based on the evaluation of different autonomous driving tasks as specified.

**Interpretation**: Higher scores indicate better task performance, with specific metrics tailored for various task types.

**Baseline Results**: Multiple models were evaluated on the NuInstruct test set, showcasing significant improvements with BEV-InMLLM.

**Validation**: Models were validated against held-out dataset splits for performance assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
