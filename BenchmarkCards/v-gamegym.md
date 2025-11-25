# V-GameGym

## 📊 Benchmark Details

**Name**: V-GameGym

**Overview**: V-GameGym is a multimodal benchmark for evaluating code LLMs in visual game generation, comprising 2,219 high-quality samples sourced from 2,190 distinct repositories and organized into 100 thematic clusters.

**Data Type**: code samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Python

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the multimodal capabilities of code language models for game development.

**Target Audience**:
- ML Researchers
- Game Developers

**Tasks**:
- Code Generation
- Game Development

**Limitations**: N/A

## 💾 Data

**Source**: 2,190 distinct Pygame repositories sourced from OpenCoder and The Stack v2.

**Size**: 2,219 samples

**Format**: Python files

**Annotation**: Manually verified by human annotators ensuring code quality and correctness.

## 🔬 Methodology

**Methods**:
- Automated code evaluation using LLM
- Human evaluation for validation

**Metrics**:
- Execution Success Rate
- Code Quality Score (0-100)
- Visual Quality Score (0-100)
- Dynamic Behavior Analysis Score (0-100)

**Calculation**: Scores are averaged across functionality, code quality, game logic, visual completeness, UI design, interaction logic, etc.

**Interpretation**: Scores closer to 100 indicate better performance in code generation and game development tasks.

**Baseline Results**: N/A

**Validation**: Human validation of samples post-automated evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
