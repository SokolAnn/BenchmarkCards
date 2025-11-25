# Skills Scaling Laws (Sloth)

## 📊 Benchmark Details

**Name**: Skills Scaling Laws (Sloth)

**Overview**: Sloth is a novel scaling law that leverages publicly available benchmark data to predict large language model (LLM) performance across multiple benchmarks by modeling low-dimensional latent skills and their correlation structure.

**Data Type**: benchmark scores

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Open LLM Leaderboard
- MMLU
- TruthfulQA
- HellaSwag
- GSM8K
- ARC
- MATH Lvl 5
- BBH
- GPQA
- MUSR
- MMLU-PRO
- Winogrande

**Resources**:
- [GitHub Repository](https://github.com/felipemaiapolo/sloth)

## 🎯 Purpose and Intended Users

**Goal**: To provide accurate and interpretable predictions of LLM performance across various benchmarks by utilizing existing scoring data without requiring extensive training on each model family.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Performance Prediction
- Benchmark Comparison

**Limitations**: The model depends on seeing data from at least one LLM from the family of interest for predictions to be reliable.

## 💾 Data

**Source**: Publicly available benchmark data from Open LLM Leaderboard v1/v2.

**Size**: 30 model families

**Format**: Raw benchmark scores in a structured format

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Regression analysis

**Metrics**:
- Mean Absolute Error (MAE)

**Calculation**: Predicted scores based on latent skills and input parameters like model size and training tokens.

**Interpretation**: Lower Mean Absolute Error indicates better predictive performance.

**Baseline Results**: Predictions versus actual scores across multiple benchmarks.

**Validation**: Cross-validation using leave-one-out schemes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
