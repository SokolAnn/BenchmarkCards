# Visual Grounding with Diverse Language in 3D (ViGiL3D)

## 📊 Benchmark Details

**Name**: Visual Grounding with Diverse Language in 3D (ViGiL3D)

**Overview**: ViGiL3D is a diagnostic dataset for evaluating visual grounding methods against a diverse set of language patterns in 3D scenes to determine their strengths and weaknesses in grounding targets based on different linguistic phenomena.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ScanRefer
- Nr3D
- Sr3D
- Multi3DRefer

**Resources**:
- [Resource](https://3dlg-hcvc.github.io/vigil3d/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse diagnostic benchmark for evaluating visual grounding methods in 3D scenes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Grounding

**Limitations**: Dataset is relatively small, which may affect the power of conclusions.

## 💾 Data

**Source**: Annotated prompts generated based on scenes from ScanNet and ScanNet++ datasets.

**Size**: 350 prompts

**Format**: N/A

**Annotation**: Manually annotated with a focus on linguistic diversity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on ground truth bounding boxes and predicted boxes with IoU thresholds.

**Interpretation**: Performance is indicated by accuracy and F1 score on the 3D visual grounding task.

**Baseline Results**: Baseline performances are based on results from methods evaluated on existing datasets such as ScanRefer.

**Validation**: Details were compared against manually annotated prompts to assess the accuracy of the pipeline.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
