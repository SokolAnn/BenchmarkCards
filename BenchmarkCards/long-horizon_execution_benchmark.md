# Long-Horizon Execution Benchmark

## 📊 Benchmark Details

**Name**: Long-Horizon Execution Benchmark

**Overview**: This benchmark isolates the execution capability of large language models on long-horizon tasks, measuring the number of steps they can reliably execute in a controlled setting.

**Data Type**: task execution sequences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.09677)

## 🎯 Purpose and Intended Users

**Goal**: To measure and benchmark the long-horizon execution capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Task Execution

**Limitations**: The benchmark does not reflect real-world complexities and errors involved in agentic tasks with variable actions.

## 💾 Data

**Source**: Synthetic data generated using an in-house method to create key-value pairs.

**Size**: 50,000 execution data points

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Controlled experiments

**Metrics**:
- Task Accuracy
- Step Accuracy
- Turn Accuracy
- Horizon Length

**Calculation**: Metrics are calculated based on the fraction of correct executions over multiple turns.

**Interpretation**: Higher metrics indicate a model's ability to execute longer tasks effectively.

**Validation**: Validation against existing language model capabilities and extensive empirical results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
