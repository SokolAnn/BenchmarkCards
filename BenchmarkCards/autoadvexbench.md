# AutoAdvExBench

## 📊 Benchmark Details

**Name**: AutoAdvExBench

**Overview**: AutoAdvExBench is a benchmark to evaluate if large language models (LLMs) can autonomously exploit defenses to adversarial examples. It evaluates the ability of LLMs to automatically implement adversarial attack algorithms that break defenses designed to be robust to adversarial examples.

**Data Type**: code implementations

**Domains**:
- Natural Language Processing
- Machine Learning Security

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/ethz-spylab/AutoAdvExBench)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a challenging benchmark for evaluating LLM capabilities in breaking adversarial example defenses.

**Target Audience**:
- AI Researchers
- Machine Learning Security Practitioners
- Security Experts

**Tasks**:
- Adversarial Attack Generation
- Evaluation of Defense Mechanisms

**Limitations**: The dataset may contain benchmark contamination as some defenses have known published breaks.

## 💾 Data

**Source**: Crawled from arXiv papers relating to adversarial machine learning, filtered to include only defenses with code implementations.

**Size**: 51 implementations

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated Evaluation
- Human Evaluation

**Metrics**:
- Attack Success Rate

**Calculation**: Success rate is calculated as the percentage of defenses whose robust accuracy falls below a specific threshold.

**Interpretation**: A lower robust accuracy indicates a higher attack success rate.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
