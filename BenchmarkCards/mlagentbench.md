# MLAgentBench

## 📊 Benchmark Details

**Name**: MLAgentBench

**Overview**: MLAgentBench is a general framework for specifying well-scoped executable tasks and automatically evaluating agents on these tasks in the context of machine learning experimentation. It includes 13 tasks ranging from improving model performance on datasets like CIFAR-10 to recent research problems.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- WebArena

**Resources**:
- [GitHub Repository](https://github.com/snap-stanford/MLAgentBench/)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate language models as agents for performing machine learning experimentation effectively.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Model Improvement
- Hyperparameter Tuning
- Automated ML Experimentation

**Limitations**: N/A

## 💾 Data

**Source**: Various machine learning datasets: CIFAR-10, imdb, ogbn-arxiv, house-price, spaceship-titanic, etc.

**Size**: 13 tasks

**Format**: CSV, JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Classification accuracy
- Mean absolute error
- Mean square error

**Calculation**: Each task assigns a performance metric score based on the final submission against a baseline.

**Interpretation**: Success is defined as achieving at least a 10% improvement over the baseline.

**Baseline Results**: Baseline accuracy on CIFAR-10 was 52.53%

**Validation**: Agents are evaluated across multiple tasks with varying difficulties to assess their generalizability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
