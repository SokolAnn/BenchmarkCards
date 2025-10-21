# MPBench

## 📊 Benchmark Details

**Name**: MPBench

**Overview**: MPBench is a comprehensive, multi-task, multimodal benchmark designed to systematically assess the effectiveness of process-level reward models (PRMs) in diverse reasoning scenarios, specifically targeting step correctness, answer aggregation, and reasoning process search.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ProcessBench
- PRMBench

**Resources**:
- [Resource](https://mpbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of multimodal process-level reward models in enhancing reasoning accuracy during both training and inference.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Step Correctness
- Answer Aggregation
- Reasoning Process Search

**Limitations**: MPBench may contain inaccurate labels of error locations, particularly for complex math problems.

## 💾 Data

**Source**: Curated from M3CoT, a multimodal dataset comprising science knowledge, mathematics, and commonsense reasoning.

**Size**: 9,745 examples

**Format**: JSON

**Annotation**: Crowdsourced via human verification and automated checks using GPT-4.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Matthews Correlation Coefficient (MCC)
- RM-Score

**Calculation**: Metrics are calculated based on the correctness of reasoning steps and the ability to aggregate answers and guide reasoning processes.

**Interpretation**: Scores are interpreted as measures of correctness, analyzing the reliability and performance of reasoning capabilities across various tasks.

**Validation**: The benchmark was validated through a human verification process with high inter-rater reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
