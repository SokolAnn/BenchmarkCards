# Bench To the Future (BTF)

## 📊 Benchmark Details

**Name**: Bench To the Future (BTF)

**Overview**: BTF is a 'pastcasting' benchmark for evaluating the forecasting capabilities of Large Language Models (LLMs). It consists of 299 high-quality questions for which resolutions are known, allowing LLMs to provide forecasts on past events using a hermetic environment based on tens of thousands of web pages.

**Data Type**: forecasting questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Metaculus AI Forecasting Benchmark Series
- ForecastBench

**Resources**:
- [Resource](https://arxiv.org/abs/2506.21558)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM forecasting capabilities based on their ability to make accurate forecasts in a controlled environment.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Forecasting

**Limitations**: The initial question set is relatively small and is expected to evolve over time with more recent questions.

## 💾 Data

**Source**: Questions sourced from reputable prediction platforms, primarily Metaculus.

**Size**: 299 questions (effective size after correlation weighting is 178.8)

**Format**: N/A

**Annotation**: Questions expanded and processed into binary format, with weights assigned to manage inter-question correlations.

## 🔬 Methodology

**Methods**:
- ReAct Forecaster
- Fixed Evidence Forecaster
- Variable Evidence Forecaster
- No Evidence Forecaster

**Metrics**:
- Brier Score

**Calculation**: Brier score calculated as the squared difference between the forecast and the actual outcome.

**Interpretation**: Lower Brier scores indicate better forecasting accuracy.

**Baseline Results**: The baseline is a Brier score of 0.25, achieved by predicting 50% across all questions.

**Validation**: Inter-run variation assessed through repeated forecasts and comparisons to live forecasts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
