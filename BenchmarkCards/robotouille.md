# ROBOTOUILLE

## 📊 Benchmark Details

**Name**: ROBOTOUILLE

**Overview**: ROBOTOUILLE is a challenging benchmark environment designed to test LLM agents’ ability to handle long-horizon asynchronous scenarios through datasets that capture increasingly complex planning challenges requiring agents to manage overlapping tasks and interruptions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ALFWorld
- WebShop
- PlanBench

**Resources**:
- [Resource](https://arxiv.org/abs/2502.05227)

## 🎯 Purpose and Intended Users

**Goal**: To stress test LLM agents on synchronous, asynchronous, and multi-agent settings.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Asynchronous Planning
- Multi-Agent Planning

**Limitations**: N/A

## 💾 Data

**Source**: Procedurally generated tasks consisting of synchronous, asynchronous, and multi-agent datasets.

**Size**: 30 tasks with 10 procedurally generated instances each

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Success Rate

**Calculation**: Success rate is determined by reaching the goal within 1.5 times the optimal number of steps for the given instance.

**Interpretation**: Higher success rates on tasks indicate better performance by the LLM agents in effectively managing asynchronous planning.

**Baseline Results**: gpt4-o ReAct achieves 47% on synchronous tasks but only 11% on asynchronous tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
