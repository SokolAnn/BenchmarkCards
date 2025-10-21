# McBE (Multi-task Chinese Bias Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: McBE (Multi-task Chinese Bias Evaluation Benchmark)

**Overview**: McBE is a Multi-task Chinese Bias Evaluation Benchmark that includes 4,077 bias evaluation instances, covering 12 single bias categories and introducing 5 evaluation tasks to measure biases in large language models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CHbias
- CBBQ

**Resources**:
- [Resource](https://arxiv.org/abs/2507.02088)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for measuring biases in Chinese large language models.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- Model Developers

**Tasks**:
- Bias Classification
- Preference Computation
- Scenario Selection
- Bias Analysis
- Bias Scoring

**Limitations**: N/A

## 💾 Data

**Source**: The data was collected from Chinese social media platforms, personal experiences through surveys and interviews, and existing bias evaluation datasets.

**Size**: 4,077 examples

**Format**: N/A

**Annotation**: Manual annotation by 30 native Chinese graduate students, with multiple rounds of review and discussion to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Bias Score
- Accuracy

**Calculation**: Various scoring methods based on model outputs compared against human annotations.

**Interpretation**: Higher scores indicate lower bias, while lower scores indicate higher bias severity.

**Validation**: Constructed using normative standards for quality reviews and annotation processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Bias instances categorized across 12 single bias categories reflecting diverse societal groups in China.

**Potential Harm**: ['Potential reinforcement of harmful stereotypes and biases in societal discourse.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All participant data was anonymized, and ethical review measures were taken to mitigate risks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all participants involved in surveys and interviews.

**Compliance With Regulations**: The study adhered to applicable ethical guidelines and legal standards for research.
