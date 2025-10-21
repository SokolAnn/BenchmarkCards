# ENGDESIGN (Engineering Design Benchmark)

## 📊 Benchmark Details

**Name**: ENGDESIGN (Engineering Design Benchmark)

**Overview**: ENGDESIGN is the first benchmark for holistically evaluating LLMs on authentic, multi-domain engineering design challenges, requiring models to function as practicing engineers, producing functional solutions to real-world design problems.

**Data Type**: engineering design tasks

**Domains**:
- Natural Language Processing
- Robotics
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://agi4engineering.github.io/Eng-Design/)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the capabilities of LLMs in realistic, multi-domain engineering design scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Engineering Design
- Simulation-based Evaluation
- Performance Validation

**Limitations**: N/A

## 💾 Data

**Source**: Emerging tasks and simulation methods in engineering design.

**Size**: 101 tasks

**Format**: SPICE, MATLAB scripts

**Annotation**: Evaluated using automated evaluation scripts and numerical simulations.

## 🔬 Methodology

**Methods**:
- Simulation-based evaluation
- Automated metrics
- Structured outputs from LLMs

**Metrics**:
- Average Pass Rate
- Average Score
- Reasoning Robustness

**Calculation**: Pass rates are based on the percentage of design tasks where the model produces a valid solution that meets all design constraints, with scores averaged across trials.

**Interpretation**: Higher scores and pass rates indicate better performance in solving engineering design tasks.

**Baseline Results**: N/A

**Validation**: Multi-stage review process involving domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
