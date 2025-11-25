# PRECOG (Performance forecasting from text descriptions)

## 📊 Benchmark Details

**Name**: PRECOG (Performance forecasting from text descriptions)

**Overview**: PRECOG is a corpus of redacted description–performance pairs spanning diverse tasks, domains, and metrics. It aims to estimate a model's score from a redacted task description and intended configuration, supporting systematic evaluation of LLM performance before running experiments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JJumSSu/PRECOG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic method for performance forecasting in LLM tasks, enabling researchers to prioritize configurations and determine dataset sizes before running full evaluations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Performance Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: arXiv experimental records curated through semi-automated methods.

**Size**: 767 instances

**Format**: N/A

**Annotation**: Redacted descriptions created with the help of LLMs and human validation.

## 🔬 Methodology

**Methods**:
- Zero-shot prediction
- Regression analysis
- Literature retrieval

**Metrics**:
- Mean Absolute Error (MAE)
- Pearson correlation

**Calculation**: Predictions are normalized to a 0–100 scale based on reports from scientific literature.

**Interpretation**: MAE measures absolute accuracy across heterogeneous metrics, while Pearson correlation assesses whether predictions preserve the relative ordering of tasks/configurations.

**Baseline Results**: MAE of 14.0 achieved with GPT-5 with search retrieval.

**Validation**: The method is validated through calibration tests and comparison with human predictions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
