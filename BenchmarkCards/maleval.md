# MalEval

## 📊 Benchmark Details

**Name**: MalEval

**Overview**: MalEval is a comprehensive evaluation framework for fine-grained Android malware auditing, designed to assess how effectively LLMs can support behavior auditing under real-world constraints.

**Data Type**: malware and benign samples with behavior reports

**Domains**:
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ZhengXR930/MalEval.git)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLMs in fine-grained Android malware auditing.

**Target Audience**:
- Security Analysts
- AI Researchers

**Tasks**:
- Function Prioritization
- Evidence Attribution
- Behavioral Synthesis
- Sample Discrimination

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset of malware samples and benign apps with manually verified reports.

**Size**: 255 samples (222 malware, 33 benign)

**Format**: JSON

**Annotation**: Manual verification of behavior reports and sensitive API lists.

## 🔬 Methodology

**Methods**:
- Systematic evaluation using ground truth reports
- Expert-guided tasks for real-world audit scenarios

**Metrics**:
- Workload Reduction Score (WRS)
- Fidelity Score (FS)
- Coverage-of-Selected Rate (CSR)
- Report Quality (RQ)
- Evidence Authenticity Score (EAS)
- Syntax Authenticity Score (SAS)

**Calculation**: Metrics are calculated based on model performance in detecting malicious behaviors and generating credible reports.

**Interpretation**: Higher scores indicate better performance in accurately identifying and synthesizing malware behavior.

**Baseline Results**: Evaluation of seven widely used LLMs including Claude-3.7-sonnet, which achieved 50.67% WRS.

**Validation**: Cross-validation through expert analysis of generated reports.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
