# AGENT SAFE

## 📊 Benchmark Details

**Name**: AGENT SAFE

**Overview**: AGENT SAFE is the first comprehensive benchmark for evaluating the safety of embodied VLM agents under hazardous instructions, featuring a risk-aware instruction dataset and evaluating agents across perception, planning, and action stages using 45 adversarial scenarios and 1,350 hazardous tasks.

**Data Type**: instruction sets

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of AGENT SAFE is to systematically evaluate the safety vulnerabilities of embodied VLM agents against hazardous instructions in simulated environments.

**Target Audience**:
- ML Researchers
- Robotics Engineers
- AI Safety Practitioners

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from real-world inspired instructions categorized into benign and risk-aware instructions.

**Size**: 9,900 instructions

**Format**: N/A

**Annotation**: Hybrid data generation protocol combining manual and model-assisted generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-Judge for safety evaluation

**Metrics**:
- Perception Accuracy
- Planning Rejection Rate
- Planning Success Rate
- Execution Success Rate

**Calculation**: The metrics are evaluated through a three-stage evaluation process: perception, planning, and action.

**Interpretation**: Higher values in metrics like Planning Success Rate and Execution Success Rate indicate better performance, while lower values in Planning Rejection Rate indicate a reluctance to accept harmful commands.

**Baseline Results**: N/A

**Validation**: The benchmark is validated through extensive experiments to reveal vulnerabilities in safety mechanisms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Decision bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset and evaluation sandbox will be released under a research-only license with explicit terms prohibiting misuse.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
