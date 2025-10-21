# InstructVul

## 📊 Benchmark Details

**Name**: InstructVul

**Overview**: InstructVul is a new instruction-based dataset for vulnerability identification and repair system with a description and code comment generation. It consists of diverse prompts tailored to security concerns of source code vulnerabilities in C/C++.

**Data Type**: instruction-data pairs

**Domains**:
- Software Development
- Cybersecurity

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2401.03374)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate developers in identifying and repairing vulnerabilities in code with comprehensive descriptions.

**Target Audience**:
- Software Developers
- Cybersecurity Researchers
- Machine Learning Researchers

**Tasks**:
- Vulnerability Identification
- Vulnerability Repair
- Vulnerability Description
- Code Comment Generation

**Limitations**: N/A

## 💾 Data

**Source**: VulDeelocator dataset and additional handcrafted examples.

**Size**: 18,086 entities

**Format**: JSON

**Annotation**: Manual annotation by security experts.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Human Evaluation

**Metrics**:
- BLEU Score
- Rouge-L
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Metrics are calculated based on generated outputs compared to reference outputs.

**Interpretation**: Higher scores indicate better performance in identifying and describing vulnerabilities.

**Validation**: Random sampling of generated outputs by security experts for quality evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security Risks
- Code Quality Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
