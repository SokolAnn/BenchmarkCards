# VLAS (Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation)

## 📊 Benchmark Details

**Name**: VLAS (Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation)

**Overview**: This paper presents VLAS, a novel end-to-end Vision-Language-Action model that integrates speech recognition directly into the robot policy model, allowing robots to understand spoken commands and perform manipulation tasks. Additionally, two datasets, SQA (Speech Question Answering) and CSI (CALVIN with Speech Instructions), are introduced to support the training and evaluation of VLAS.

**Data Type**: question-answering pairs, audio-speech instruction pairs

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/whichwhichgone/VLAS)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of this benchmark is to evaluate the effectiveness of the VLAS model in robot manipulation tasks using speech instructions, enabling customized interactions between humans and robots.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Robotics Developers

**Tasks**:
- Robot Manipulation
- Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: SQA and CSI datasets

**Size**: 185,000 examples for SQA, 194,000 examples for CSI

**Format**: CSV, JSON

**Annotation**: Speech instructions were generated using text-to-speech synthesis from textual instructions paired with images.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the success rate of the VLAS model in performing robot manipulation tasks.

**Interpretation**: Higher accuracy represents better performance in correctly executing tasks based on speech instructions.

**Baseline Results**: VLAS was evaluated against existing VLA models on the CALVIN benchmark, showing improved performance in handling speech instructions.

**Validation**: Evaluation through extensive experimental results on custom benchmarks for robot manipulation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
