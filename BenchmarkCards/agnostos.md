# AGNOSTOS

## 📊 Benchmark Details

**Name**: AGNOSTOS

**Overview**: AGNOSTOS is a novel simulation benchmark designed to rigorously evaluate cross-task zero-shot generalization in manipulation, comprising 23 unseen manipulation tasks that differ from common training task distributions.

**Data Type**: task-action pairs

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://jiaming-zhou.github.io/AGNOSTOS)
- [GitHub Repository](https://github.com/jiaming-zhou/X-ICM)

## 🎯 Purpose and Intended Users

**Goal**: To assess the limits of vision-language-action (VLA) models in zero-shot generalization for robotic manipulation.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Robotic Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: RLBench simulation environment

**Size**: 3600 demonstrations for 18 seen tasks and 23 unseen tasks for testing

**Format**: N/A

**Annotation**: Data collected from demonstrations of robotic manipulation tasks

## 🔬 Methodology

**Methods**:
- Systems evaluation
- Cross-task zero-shot testing

**Metrics**:
- Success Rate

**Calculation**: Mean and standard deviation of success rates over multiple trials.

**Interpretation**: Higher success rates indicate better generalization of VLA models to unseen tasks.

**Baseline Results**: Comparison against existing VLA models, including performance metrics reported.

**Validation**: Evaluation on 23 unseen manipulation tasks categorized by difficulty.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
