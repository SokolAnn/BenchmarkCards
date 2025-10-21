# LoHoRavens (Long-Horizon Language-Conditioned Benchmark for Robotic Tabletop Manipulation)

## 📊 Benchmark Details

**Name**: LoHoRavens (Long-Horizon Language-Conditioned Benchmark for Robotic Tabletop Manipulation)

**Overview**: LoHoRavens is a long-horizon language-conditioned simulated benchmark for robotic tabletop manipulation tasks, covering various long-horizon reasoning aspects spanning color, size, space, arithmetics, and reference.

**Data Type**: demonstration instances

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://cisnlp.github.io/lohoravens-webpage/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a public benchmark for testing the long-horizon reasoning capabilities of language-conditioned robots.

**Target Audience**:
- Robotics Researchers
- ML Researchers

**Tasks**:
- Robotic Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated demonstrations from a simulator using an oracle agent.

**Size**: 1,000 demonstrations for training, 200 for validation, 200 for testing per task.

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Evaluating average task performance based on task completion score.

**Metrics**:
- Success rate (%)

**Calculation**: Scores range from 0 (fail) to 100 (success) based on the number of completed steps vs. total required.

**Interpretation**: Higher scores indicate better performance in completing long-horizon tasks.

**Baseline Results**: Initial performance on unseen tasks is notably reduced compared to seen tasks.

**Validation**: The benchmark evaluates long-horizon reasoning in various conditions with perturbations to simulate real-world complexities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
