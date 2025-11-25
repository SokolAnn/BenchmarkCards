# Embodied Planning Dataset

## 📊 Benchmark Details

**Name**: Embodied Planning Dataset

**Overview**: The dataset consists of 67K instruction instances aimed at enhancing embodied instruction planning for robotic agents. It is specifically designed to improve the logical validity and execution of long-term decisions in instruction following tasks.

**Data Type**: instruction instances

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ALFRED

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance long-term decision making in robotics by integrating LLM capabilities with domain-specific expertise through a high-quality dataset.

**Target Audience**:
- Robotics Researchers
- AI Researchers

**Tasks**:
- Instruction Following
- Embodied Planning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from ALFRED dataset and augmented with self-instruction mechanisms.

**Size**: 67,000 examples

**Format**: N/A

**Annotation**: Template feedback-based self-instruction method

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Template feedback for data generation

**Metrics**:
- Success Rate (SR)
- Goal-Condition Success (GC)
- High-Level Planning Accuracy (HLP ACC)

**Calculation**: Metrics are calculated based on effectively completed tasks and the accuracy of planned subgoals.

**Interpretation**: Higher metrics indicate improved planning efficiency and task completion.

**Baseline Results**: Comparison with existing methods like Prompter and LLM-Planner shows significant improvements across different metrics.

**Validation**: The dataset's efficacy is validated through performance on the ALFRED benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
