# SimBench

## 📊 Benchmark Details

**Name**: SimBench

**Overview**: SimBench is a benchmark designed to evaluate the proficiency of student large language models (S-LLMs) in generating digital twins (DTs) for simulators, enabling ranking based on their ability to produce high-quality DTs.

**Data Type**: dialogue interactions

**Domains**:
- Robotics
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uwsbel/SimBench)

## 🎯 Purpose and Intended Users

**Goal**: To measure the ability of student large language models to generate effective digital twins for simulation scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Multi-turn Interaction
- Digital Twin Generation

**Limitations**: N/A

## 💾 Data

**Source**: A dataset with 102 exemplary demonstrations categorized into 34 distinct physical systems, manually curated by simulation experts.

**Size**: 102 demonstrations

**Format**: N/A

**Annotation**: Manually curated by experts

## 🔬 Methodology

**Methods**:
- Automated evaluation using a rule-based judge LLM (J-LLM)

**Metrics**:
- pass@1
- CodeBLEU
- ROUGE-LSUM

**Calculation**: Metrics are calculated based on the correctness of generated digital twins compared to expert-provided ground truth.

**Interpretation**: Higher pass@1 scores indicate better performance in generating accurate digital twins.

**Validation**: Evaluation framework is optimized using expert feedback on ground truth code.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
