# CLEVA

## 📊 Benchmark Details

**Name**: CLEVA

**Overview**: CLEVA is a user-friendly platform designed to holistically evaluate Chinese Large Language Models (LLMs) across various dimensions. It employs a standardized workflow, mitigates contamination risks through data curation, and features a competitive leaderboard.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Machine Learning

**Languages**:
- Chinese

**Similar Benchmarks**:
- HELM
- C-Eval
- M3KE
- CMMLU
- GAOKAO-Bench
- MMCU

**Resources**:
- [GitHub Repository](https://github.com/LaVi-Lab/CLEVA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating Chinese LLMs based on diverse metrics and prompt evaluation.

**Target Audience**:
- Researchers
- Developers
- Data Scientists

**Tasks**:
- Model evaluation across various NLP tasks
- Performance comparison among different LLMs
- Holistic assessment of LLM capabilities

**Limitations**: Performance may vary based on language models' ability to understand prompts.

**Out of Scope Uses**:
- Evaluation of non-Chinese LLMs

## 💾 Data

**Source**: Collected and curated through manual annotation and existing datasets.

**Size**: 370K test instances from 84 datasets, resulting in over 9 million queries after augmentation.

**Format**: Text

**Annotation**: Data includes a variety of prompts and is structured to ensure consistency in evaluation.

## 🔬 Methodology

**Methods**:
- Performance metrics based on diverse NLP tasks
- Robustness and fairness evaluation
- Regular updates on testing to avoid contamination

**Metrics**:
- Accuracy
- Calibration and uncertainty
- Robustness
- Fairness
- Bias and stereotypes
- Toxicity
- Efficiency
- Diversity
- Privacy

**Calculation**: Metrics are calculated based on model predictions evaluated against reference outputs.

**Interpretation**: Metrics provide insights into the model's performance, biases, and robustness against various evaluation criteria.

**Validation**: Various validation methods including testing against known benchmarks and expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy Risk
- Data Laws Risk
- Privacy Risk
- Fairness Risk
- Robustness Risk

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in prompt
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Carefully managed with no sensitive information collected, with full informed consent from participants.

**Data Licensing**: All collected data is used responsibly and complies with relevant data protection regulations.

**Consent Procedures**: Participants were informed about data usage during the manual collection process.

**Compliance With Regulations**: Followed ethical guidelines for data collection and testing.
