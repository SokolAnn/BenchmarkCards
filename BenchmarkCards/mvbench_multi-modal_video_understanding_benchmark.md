# MVBench (Multi-modal Video understanding Benchmark)

## 📊 Benchmark Details

**Name**: MVBench (Multi-modal Video understanding Benchmark)

**Overview**: MVBench aims at comprehensively evaluating the temporal perception capabilities of multi-modal large language models (MLLMs) in the open world, covering 20 challenging video tasks that require temporal understanding.

**Data Type**: multiple-choice Question-Answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SEED-Bench
- VideoChatGPT

**Resources**:
- [GitHub Repository](https://github.com/OpenGVLab/Ask-Anything)
- [Resource](https://huggingface.co/spaces/OpenGVLab/MVBench_Leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MVBench is to evaluate the temporal understanding capabilities of MLLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Action Sequence
- Action Prediction
- Action Antonym
- Fine-grained Action
- Unexpected Action
- Object Existence
- Object Interaction
- Object Shuffle
- Moving Direction
- Action Localization
- Scene Transition
- Action Count
- Moving Count
- Moving Attribute
- State Change
- Fine-grained Pose
- Character Order
- Egocentric Navigation
- Episodic Reasoning
- Counterfactual Inference

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 11 existing public video datasets, including STAR, PAXION, and CLEVRER.

**Size**: 1.1 million video annotations

**Format**: JSON

**Annotation**: Automatic annotation through large language models.

## 🔬 Methodology

**Methods**:
- QA generation using automatic annotation
- Evaluation with multiple-choice QA

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the proportion of correct answers.

**Interpretation**: Higher accuracy indicates better temporal understanding performance by the models.

**Baseline Results**: VideoChat2 achieved an accuracy of 66.0%, outperforming leading models by over 15%.

**Validation**: Comprehensive evaluations against various MLLMs are conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
