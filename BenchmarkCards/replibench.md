# RepliBench

## 📊 Benchmark Details

**Name**: RepliBench

**Overview**: RepliBench is a suite of evaluations designed to measure autonomous replication capabilities of language model agents across various tasks.

**Data Type**: task evaluations

**Domains**:
- Computer Security

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2504.18565)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the autonomous replication capabilities of language model agents.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Autonomous Replication Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated tasks based on autonomous capabilities of language models.

**Size**: 201 task families, 86 individual tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated scoring

**Metrics**:
- Pass Rate

**Calculation**: Pass@k scores computed for each task family based on success attempts.

**Interpretation**: A higher pass rate indicates better performance in executing the tasks.

**Validation**: Comparison of performance among different models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in prompt
- **Fairness**: Decision bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To minimize misuse and ensure responsible handling of capabilities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
