# BLADE: Benchmarking Language Model Agents for Data-Driven Science

## 📊 Benchmark Details

**Name**: BLADE: Benchmarking Language Model Agents for Data-Driven Science

**Overview**: BLADE consists of 12 datasets and research questions drawn from existing scientific literature, with ground truth collected from independent analyses by expert data scientists and researchers to evaluate agents’ performances on open-ended research questions in data-driven scientific inquiries.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Finance
- Healthcare
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ARCADE
- DABench
- MLAgentBench
- DS-Agent

**Resources**:
- [GitHub Repository](https://github.com/behavioral-data/BLADE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating language model agents in the context of open-ended data-driven scientific questions.

**Target Audience**:
- ML Researchers
- Data Scientists
- Domain Experts

**Tasks**:
- Data Analysis
- Statistical Modeling
- Conceptual Variable Formulation

**Limitations**: N/A

## 💾 Data

**Source**: Existing scientific literature and datasets reconstructed for the purpose of evaluations in terms of complexity and analysis requirements.

**Size**: 12 datasets and 188 multiple choice questions

**Format**: JSON

**Annotation**: Ground truth analyses collected from expert data scientists and researchers.

## 🔬 Methodology

**Methods**:
- Expert Evaluations
- Automatic Evaluation Metrics

**Metrics**:
- Accuracy
- F1 Score
- Coverage@10

**Calculation**: Accuracy and F1 Score computed based on matching agent outputs to ground truth using a standardized set of criteria.

**Interpretation**: Performance is measured against a diverse set of analytical decisions reflecting both accuracy of responses and breadth of justifiable methods.

**Baseline Results**: Performance metrics for various language models evaluated against BLADE benchmark.

**Validation**: Multiple evaluations through expert analysis and automated scoring based on matching criteria.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
