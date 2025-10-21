# Interplay

## 📊 Benchmark Details

**Name**: Interplay

**Overview**: Interplay is a novel dataset comprising thousands of interaction plans that cover long-horizon static and dynamic interaction tasks to evaluate human-object interaction synthesis.

**Data Type**: interaction plans

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://vlm-rmd.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enable systematic evaluation of a framework for synthesizing human-object interactions using Vision-Language Models.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Human-Object Interaction Synthesis

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset using high-quality 3D object assets from various existing datasets.

**Size**: 1,210 interaction plans

**Format**: Structured data (likely JSON)

**Annotation**: Automatically designed interactions without manual annotations.

## 🔬 Methodology

**Methods**:
- Goal-conditioned reinforcement learning
- VLM-guided planning

**Metrics**:
- Completion Rate
- Sub-step Completion Ratio
- Sub-step Precision

**Calculation**: Task-specific rewards and progress assessment based on actions executed by humanoid character.

**Interpretation**: Metrics reflect the effectiveness of interaction planning and execution across human-object scenarios.

**Validation**: Performance evaluated against several benchmarks through extensive experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
