# LaMPilot-Bench

## 📊 Benchmark Details

**Name**: LaMPilot-Bench

**Overview**: LaMPilot-Bench is the first benchmark dataset specifically designed to quantitatively evaluate the efficacy of language model programs in autonomous driving (AD). Each scenario in the benchmark consists of a task described in natural language, along with a simulated environment for comprehensive evaluation.

**Data Type**: traffic scene scenarios

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PurdueDigitalTwin/LaMPilot)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction-following capabilities of LLM-based agents in autonomous driving.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Following
- Autonomous Driving Simulation

**Limitations**: N/A

## 💾 Data

**Source**: The LaMPilot dataset consists of semi-human-annotated traffic scenes obtained from Road and Traffic simulation environments.

**Size**: 4,900 scenarios

**Format**: N/A

**Annotation**: Semi-human annotation

## 🔬 Methodology

**Methods**:
- Simulator-based evaluation
- Automated metrics calculation

**Metrics**:
- Time-to-Collision (TTC)
- Speed Variance (SV)
- Time Efficiency (TE)

**Calculation**: Metrics are calculated based on the performance of LLM-generated policies in the simulated environment.

**Interpretation**: Higher scores indicate better performance in safety (TTC), stability (SV), and efficiency (TE).

**Baseline Results**: N/A

**Validation**: Evaluated against heuristic baselines and off-the-shelf large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
