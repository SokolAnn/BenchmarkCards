# LongTasks

## 📊 Benchmark Details

**Name**: LongTasks

**Overview**: LongTasks is a dataset specifically created to evaluate planning ability on complex long-horizon tasks, which includes more task goals, longer action sequences, and a greater variety and quantity of objects compared to existing datasets.

**Data Type**: task planning tasks

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wuyike2000/MLDT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging dataset for evaluating complex long-horizon robotic task planning capabilities.

**Target Audience**:
- ML Researchers
- Robotics Researchers

**Tasks**:
- Robotic Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing datasets extended by LID and included additional challenging task constructions.

**Size**: 1,154 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate (SR)
- Executability (Exe)

**Calculation**: Metrics are calculated based on the execution of plans to determine if they achieve task goals and are executable.

**Interpretation**: Higher SR indicates better performance in achieving task goals, while higher Exe indicates the executability of the plans.

**Baseline Results**: N/A

**Validation**: Evaluated using various LLMs on the constructed and extended datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
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
