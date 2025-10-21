# CogBench

## 📊 Benchmark Details

**Name**: CogBench

**Overview**: CogBench is a new benchmark specifically designed for the Multimodal Retrieval Augmented Generation Planning (MRAG Planning) task, facilitating the integration of lightweight CogPlanner with resource-efficient multimodal language models (MLLMs).

**Data Type**: text and image query-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MRAG-Bench
- MMSearch

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the decision-making capabilities related to Multimodal Retrieval Augmented Generation Planning and to evaluate the performance of MLLMs in real-world multimodal querying scenarios.

**Target Audience**:
- ML Researchers
- Practitioners
- Model Developers

**Tasks**:
- Multimodal Retrieval Augmented Generation Planning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from web-sourced screenshots and manual user interaction simulations.

**Size**: 7,000 examples

**Format**: N/A

**Annotation**: Human-annotated based on the decision-making process of MRAG Planning.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score

**Calculation**: Metrics are calculated by measuring token overlap and precision/recall of claims against ground truth.

**Interpretation**: A higher F1 Score indicates a better performance of the MRAG Planning system.

**Baseline Results**: CogPlanner demonstrated significant improvements over existing MRAG approaches, achieving more than 15% gains.

**Validation**: The benchmark has been thoroughly tested against various models to validate its effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
