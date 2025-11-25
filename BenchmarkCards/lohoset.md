# LoHoSet

## 📊 Benchmark Details

**Name**: LoHoSet

**Overview**: LoHoSet is designed for training the LoHoVLA model on long-horizon embodied tasks and consists of 20 long-horizon tasks with 1,000 expert demonstrations each, featuring visual observations, linguistic goals, sub-tasks, and robot actions.

**Data Type**: visual observations, linguistic goals, sub-tasks, and robot actions

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- LoHoRavens

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for training and evaluating a unified vision-language-action model for long-horizon embodied tasks.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- Industry Practitioners

**Tasks**:
- Long-Horizon Task Planning

**Limitations**: The precision of robot actions may be limited due to the discrete nature of commands.

## 💾 Data

**Source**: Ravens robot simulator

**Size**: 20 tasks with 1,000 expert demonstrations each

**Format**: N/A

**Annotation**: Automatically generated from simulation

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Success rate

**Calculation**: Scores are generated based on the proportion of correctly completed steps in each task.

**Interpretation**: A higher score indicates better performance in task completion.

**Baseline Results**: LoHoVLA outperformed both hierarchical and vanilla VLA models on various metrics.

**Validation**: Comparative analysis against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
