# CloudEval-YAML

## 📊 Benchmark Details

**Name**: CloudEval-YAML

**Overview**: CloudEval-YAML is the first hand-written benchmark for cloud configuration generation targeting YAML, consisting of 1011 practical problems that are based on realistic scenarios in cloud-native applications.

**Data Type**: YAML configuration problems

**Domains**:
- Cloud Computing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HumanEval
- MBPP
- WikiSQL

**Resources**:
- [GitHub Repository](https://github.com/alibaba/CloudEval-YAML)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in generating cloud-native YAML configuration files.

**Target Audience**:
- ML Researchers
- Software Developers
- Cloud Engineers

**Tasks**:
- Code Generation

**Limitations**: The benchmark focuses on YAML generation only and does not cover other configuration formats extensively.

## 💾 Data

**Source**: Hand-written problems from official documentation, StackOverflow, and blog posts related to cloud-native applications.

**Size**: 1011 problems

**Format**: YAML

**Annotation**: Manually annotated with unit tests and reference solutions.

## 🔬 Methodology

**Methods**:
- Unit Testing
- Text-level Evaluation Metrics (e.g., BLEU, Edit Distance)
- YAML-aware Evaluation Metrics (e.g., Key-Value Exact Match)

**Metrics**:
- BLEU Score
- Edit Distance
- Exact Match
- Key-Value Exact Match
- Key-Value Wildcard Match

**Calculation**: Metrics are calculated based on the similarity between generated YAML files and reference solutions, as well as the functional correctness verified by unit tests.

**Interpretation**: Higher scores indicate better accuracy and functional correctness, with specific thresholds for passing unit tests.

**Baseline Results**: GPT-4 achieved the highest score across all metrics.

**Validation**: Performance validated through automated unit tests in a cloud simulated environment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Includes bilingual support to cater to cloud operation teams using English and Chinese.

**Potential Harm**: Efforts are made to avoid unintentional biases in dataset creation and evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
