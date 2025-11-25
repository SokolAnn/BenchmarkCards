# CYBER SECEVAL (Cybersecurity Evaluation Suite for Language Models)

## 📊 Benchmark Details

**Name**: CYBER SECEVAL (Cybersecurity Evaluation Suite for Language Models)

**Overview**: CYBER SECEVAL is a comprehensive benchmark developed to help bolster the cybersecurity of Large Language Models (LLMs) employed as coding assistants, evaluating their propensity to generate insecure code and their compliance when asked to assist in cyberattacks.

**Data Type**: text

**Domains**:
- Cybersecurity
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/PurpleLlama/tree/main/CybersecurityBenchmarks)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for assessing the cybersecurity risks of LLMs.

**Target Audience**:
- ML Researchers
- Cybersecurity Professionals
- Model Developers

**Tasks**:
- Insecure Code Detection
- Cyberattack Compliance Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Open source codebases and static analysis rules.

**Size**: N/A

**Format**: N/A

**Annotation**: Automated test case generation and evaluation pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Static analysis
- LLM-based evaluation

**Metrics**:
- Precision
- Recall

**Calculation**: Metrics calculated using an Insecure Code Detector for insecure coding practices and compliance evaluation against cyberattack prompts.

**Interpretation**: Higher precision and recall indicate better detection of insecure code and compliance with malicious requests.

**Baseline Results**: N/A

**Validation**: Manual inspection of random test case responses for accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Misuse**: Nonconsensual use, Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: Evaluation of models that may generate insecure or harmful code.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
