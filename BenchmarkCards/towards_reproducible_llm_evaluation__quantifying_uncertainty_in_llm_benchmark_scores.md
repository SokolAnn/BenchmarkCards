# Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores

## 📊 Benchmark Details

**Name**: Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores

**Overview**: This paper explores benchmarking methods for Large Language Models (LLMs) focusing on quantifying uncertainty in benchmark scores. It provides methodologies for effective experimental repetition to measure and reduce variability in the mean scores of LLMs' performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.03492)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to assess the stochastic behavior of LLMs and improve the reproducibility of LLM evaluations by quantifying uncertainty in benchmark results.

**Target Audience**:
- ML Researchers
- Model Evaluators

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Developed benchmarks on spatial reasoning questions about cardinal directions.

**Size**: 100 questions for Small benchmark, 5760 questions for Large benchmark

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Experimental repeats
- Statistical significance testing

**Metrics**:
- Mean score
- Prediction intervals

**Calculation**: Mean score is calculated over experimental repeats and prediction intervals are calculated to quantify uncertainty.

**Interpretation**: A lower prediction interval width indicates greater confidence in the benchmark scores.

**Baseline Results**: Results from the Large and Small benchmarks vary by model and settings used.

**Validation**: Statistical tests, including two-sample t-tests, are used to determine significant differences between model scores.

## ⚠️ Targeted Risks

**Risk Categories**:
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
