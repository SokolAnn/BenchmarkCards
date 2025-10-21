# HomeEmergency

## 📊 Benchmark Details

**Name**: HomeEmergency

**Overview**: The HomeEmergency dataset is aimed at enabling researchers to create embodied agents capable of responding to emergency situations in the home. It benchmarks the abilities of embodied AI agents to identify emergencies based on audio signals.

**Data Type**: audio-visual navigation scenarios

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2504.01089)

## 🎯 Purpose and Intended Users

**Goal**: To enable home robots to respond to emergency scenarios in the home, preventing injuries and deaths.

**Target Audience**:
- Roboticists
- AI Researchers
- Machine Learning Researchers

**Tasks**:
- Emergency Detection
- Navigation
- Audio Classification

**Limitations**: The assumption of an existing human heatmap and the lack of significant auditory background noise in both simulation and real-world environments are notable limitations.

## 💾 Data

**Source**: The dataset is created using the ThreeDWorld simulator to generate household emergency scenarios based on audio signals.

**Size**: 1152 episodes

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Probabilistic Dynamic Scene Graph (P-DSG)
- Audio Perception Module
- Emergency Identification Module

**Metrics**:
- AudioGoal Success Rate (AG SR)
- AudioGoal Success Rate weighted by Inverse Path Length (AG SPL)
- Emergency Detection False Negative Rate (EDFNR)
- Emergency Detection False Positive Rate (EDFPR)

**Calculation**: Metrics are calculated based on the fraction of episodes where the agent successfully navigates to and identifies the emergency audio source.

**Interpretation**: Higher success rates and lower false negative rates indicate better performance of the agent in detecting emergencies.

**Baseline Results**: Agent's AG SR of 0.75 for falls and 0.86 for fires, outperforming baseline methods.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy concerns connected to developing and storing a heatmap of user activity in the home.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
