# SURDS (Benchmarking Spatial Understanding and Reasoning in Driving Scenarios with Vision Language Models)

## 📊 Benchmark Details

**Name**: SURDS (Benchmarking Spatial Understanding and Reasoning in Driving Scenarios with Vision Language Models)

**Overview**: SURDS is a large-scale benchmark designed to systematically evaluate the spatial reasoning capabilities of vision language models (VLMs) through 41,080 training instances and 9,250 evaluation samples spanning six spatial categories: orientation, depth estimation, pixel-level localization, pairwise distance, lateral ordering, and front–behind relations.

**Data Type**: vision–question–answer pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/XiandaGuo/Drive-MLLM)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and improve the spatial reasoning capabilities of vision language models (VLMs) in realistic driving scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Distance Estimation
- Front/Behind Determination
- Left/Right Determination
- Depth Range Determination
- Yaw Angle Determination
- Pixel Location Estimation

**Limitations**: N/A

## 💾 Data

**Source**: The nuScenes dataset, which is a large-scale public dataset specifically designed for autonomous driving research.

**Size**: 41,080 training instances and 9,250 evaluation instances

**Format**: N/A

**Annotation**: Multi-stage filtering pipeline including label-based and description-based strategies.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Reinforcement Learning

**Metrics**:
- Overall score
- Centerness-based metric for Pixel Localization

**Calculation**: Scores are determined based on average performance across defined tasks.

**Interpretation**: An overall score of VLMs is considered good if it significantly exceeds prior models, as shown in benchmark evaluations.

**Baseline Results**: Qwen2.5-VL-72B-SFT-GRPO achieved a score of 40.80, outperforming models like GPT-4o and Gemini.

**Validation**: Extensive comparative and ablation experiments demonstrate the performance of existing models against SURDS.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
