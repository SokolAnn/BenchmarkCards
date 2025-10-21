# ELBA-Bench (Efficient Learning Backdoor Attacks Benchmark for Large Language Models)

## 📊 Benchmark Details

**Name**: ELBA-Bench (Efficient Learning Backdoor Attacks Benchmark for Large Language Models)

**Overview**: ELBA-Bench provides a comprehensive and unified framework for evaluating backdoor attacks on large language models (LLMs) through parameter efficient fine-tuning or without fine-tuning strategies. It incorporates over 1300 experiments, 12 attack methods, 18 datasets, and 12 LLMs, providing insights into attack performance and metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BackdoorLLM

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified platform for assessing backdoor attack methodologies and enhancing security measures against them in large language models.

**Target Audience**:
- ML Researchers
- Security Researchers
- Model Developers

**Tasks**:
- Backdoor Attack Evaluation
- Adversarial Robustness Testing

**Limitations**: Current works lack robust support for defensive strategies against backdoor attacks.

## 💾 Data

**Source**: ELBA-Bench includes a wide range of datasets including SST-2, SMS, DBpedia, Advbench, GSM8K, MATH, and more for evaluating different tasks.

**Size**: Over 1300 experiments

**Format**: N/A

**Annotation**: Dataset is prepared from various sources including public datasets and has been used in structured evaluations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Clean Accuracy (CACC)
- Attack Success Rate (ASR)
- False Trigger Rate (FTR)
- Refusal Rate (RR)
- Pass Rate (PassR)

**Calculation**: Metrics are calculated based on model performance on different datasets with clean and poisoned samples.

**Interpretation**: A higher ASR indicates a more effective attack, while clean accuracy reflects the model's ability to perform well on untainted data.

**Baseline Results**: N/A

**Validation**: The benchmark validations involved comprehensive evaluations across multiple attack methods and datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
