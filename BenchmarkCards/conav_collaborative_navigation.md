# CoNav (Collaborative Navigation)

## 📊 Benchmark Details

**Name**: CoNav (Collaborative Navigation)

**Overview**: CoNav is a benchmark aimed at human-centered collaborative navigation, assessing the agent's intention prediction ability through understanding human behavior in indoor environments and enabling efficient collaboration between humans and robots.

**Data Type**: humanoid animations and navigation trajectories

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- Habitat 3.0

**Resources**:
- [GitHub Repository](https://github.com/Li-ChangHao/CoNav.git)

## 🎯 Purpose and Intended Users

**Goal**: To promote efficient human-robot collaboration by developing agents capable of understanding human intentions and navigating to assist effectively.

**Target Audience**:
- Researchers in robotics
- AI practitioners
- Developers of human-robot interaction systems

**Tasks**:
- Human-Centered Navigation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a combination of Large Language Models and motion generation models based on realistic indoor environments.

**Size**: 20,293 navigation episodes

**Format**: Custom format for humanoid simulations

**Annotation**: Automatically annotated based on the generated activity descriptions.

## 🔬 Methodology

**Methods**:
- Human observation-based navigation
- Imitation learning for agent training

**Metrics**:
- First-to-Arrive Success Rate (FASR)
- Robot-Arrive Success Rate (RASR)
- Collision Rate (CR)
- Average Steps (AS)

**Calculation**: Metrics are calculated based on successful navigation episodes and path lengths.

**Interpretation**: Higher values in FASR and RASR indicate better performance in predicting human intentions and safe navigation.

**Baseline Results**: Compared against various agents including pioneer and human-following agents on FASR and RASR metrics.

**Validation**: Cross-validation using training and validation splits of the CoNav dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Safety
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
