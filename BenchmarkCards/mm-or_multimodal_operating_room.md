# MM-OR (Multimodal Operating Room)

## 📊 Benchmark Details

**Name**: MM-OR (Multimodal Operating Room)

**Overview**: MM-OR is a realistic and large-scale multimodal spatio-temporal dataset designed to advance operating room modeling and enable multimodal scene graph generation.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/egeozsoy/MM-OR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for studying robotic-assisted surgical workflows and advance operating room modeling.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Robotics Engineers

**Tasks**:
- Scene Graph Generation
- Sterility Breach Detection
- Next Action Anticipation
- Robot Phase Prediction

**Limitations**: MM-OR includes only total and partial knee replacements in one OR, which may limit generalization.

## 💾 Data

**Source**: Recorded multimodal data from robotic total and partial knee replacement surgeries.

**Size**: 92,983 timepoints with 25,277 annotated entries totaling 500GB of data

**Format**: Various formats including RGB-D video, audio, robotic logs

**Annotation**: Manually annotated with panoptic segmentations and scene graphs by trained annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Macro F1-score for evaluation across multiple predicates in scene graph generation.

**Interpretation**: Higher scores indicate better performance in recognizing and predicting surgical actions and interactions.

**Baseline Results**: F1 Score of 0.529 for scene graph generation.

**Validation**: Models evaluated using F1-scores across various configurations of modality utilization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Invasive procedures might introduce risks such as infections or incorrect placements.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization processes were implemented during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
