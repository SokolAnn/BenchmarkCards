# RDMM (Robotics Decision-Making Models)

## 📊 Benchmark Details

**Name**: RDMM (Robotics Decision-Making Models)

**Overview**: The RDMM framework utilizes Robotics Decision-Making Models for on-device robotic decision making with enhanced contextual awareness in specific domains. The framework includes a new dataset of 27,514 planning instances and 1,300 annotated samples aimed at improving the planning and decision-making abilities of robots.

**Data Type**: text-image annotated samples and planning instances

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shadynasrat/RDMM)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the autonomous decision-making capabilities of robots by integrating knowledge of their skills and personal information.

**Target Audience**:
- ML Researchers
- Robotics Engineers
- AI Developers

**Tasks**:
- Planning
- Robotic Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Created from tasks and rules of the RoboCup@Home competition.

**Size**: 27,514 examples

**Format**: JSON

**Annotation**: Manually annotated examples

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated as the ratio of correct planning instances to the total number of planning instances.

**Interpretation**: Higher accuracy indicates better planning and decision-making capability of the robot.

**Baseline Results**: The RDMM-8B model achieved 92.98% accuracy, significantly outperforming its base model which had 44.34%.

**Validation**: Evaluated during the RoboCup@Home competition.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
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
