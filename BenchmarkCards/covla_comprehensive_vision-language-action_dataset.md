# CoVLA (Comprehensive Vision-Language-Action) Dataset

## 📊 Benchmark Details

**Name**: CoVLA (Comprehensive Vision-Language-Action) Dataset

**Overview**: CoVLA Dataset is a large-scale dataset for autonomous driving that includes 10,000 video clips, frame-level language captions describing driving scenarios, and future trajectory actions, designed to facilitate the training and evaluation of Vision-Language-Action models.

**Data Type**: video with language descriptions and trajectory annotations

**Domains**:
- Automotive
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- KITTI
- Waymo Open Dataset
- nuScenes

**Resources**:
- [Resource](https://turingmotors.github.io/covla-ad/)
- [Resource](https://huggingface.co/datasets/turing-motors/CoVLA-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training and evaluating Vision-Language-Action models in the context of autonomous driving, facilitating advanced reasoning and decision-making capabilities.

**Target Audience**:
- ML Researchers
- Autonomous Driving Practitioners
- Model Developers

**Tasks**:
- Trajectory Prediction
- Scene Description Generation
- Action Planning

**Limitations**: N/A

## 💾 Data

**Source**: Real-world driving data collected using vehicles equipped with cameras and sensors around Tokyo, Japan.

**Size**: 10,000 video clips, over 80 hours of driving footage, 6,000,000 video frames

**Format**: Video with captions in JSON

**Annotation**: Automatically generated captions and trajectories using sensor fusion and deep learning techniques.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Average Displacement Error (ADE)
- Final Displacement Error (FDE)

**Calculation**: ADE is calculated as the mean Euclidean distance between predicted trajectory points and ground truth points over all time steps. FDE measures the distance between the predicted final point and the ground truth final point.

**Interpretation**: Lower values of ADE and FDE indicate better trajectory prediction accuracy.

**Baseline Results**: N/A

**Validation**: The dataset was validated through systematic sampling and automated metric calculation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Human faces and license plates in the dataset images and videos were anonymized to protect privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
