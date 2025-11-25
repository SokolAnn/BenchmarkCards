# ViPlan (Visual Planning with Symbolic Predicates and Vision-Language Models)

## 📊 Benchmark Details

**Name**: ViPlan (Visual Planning with Symbolic Predicates and Vision-Language Models)

**Overview**: ViPlan is the first open-source benchmark for Visual Planning with symbolic predicates and Vision-Language Models (VLMs), featuring tasks in Blocksworld and a household robotics environment.

**Data Type**: visual planning tasks

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/merlerm/ViPlan)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation of VLMs for planning tasks using symbolic predicates.

**Target Audience**:
- Machine Learning Researchers
- AI Practitioners

**Tasks**:
- Planning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: ViPlan features a collection of visual planning tasks in Blocksworld and household robotics using the iGibson simulator.

**Size**: 50 tasks (25 each for Blocksworld and Household)

**Format**: PDDL

**Annotation**: Tasks are procedurally generated with varying levels of complexity.

## 🔬 Methodology

**Methods**:
- VLM-as-planner
- VLM-as-grounder

**Metrics**:
- Success Rate
- Accuracy

**Calculation**: Success rate based on the fraction of tasks completed successfully per model.

**Interpretation**: Higher success rates indicate better planning capabilities of VLMs.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
