# VideoConviction: A Multimodal Benchmark for Human Conviction and Stock Market Recommendations

## 📊 Benchmark Details

**Name**: VideoConviction: A Multimodal Benchmark for Human Conviction and Stock Market Recommendations

**Overview**: VideoConviction is a novel, expert-annotated multimodal dataset focused on financial discourse, derived from YouTube videos of financial influencers. The dataset includes 6,000+ expert annotations to benchmark multimodal large language models (MLLMs) and text-based large language models (LLMs) in extracting stock recommendations and assessing human conviction in their delivery.

**Data Type**: multimodal

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.1145/3711896.3737417)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark multimodal models in extracting financial insights from YouTube videos of finfluencers discussing U.S. stock market recommendations.

**Target Audience**:
- ML Researchers
- Finance Analysts
- Model Developers

**Tasks**:
- Ticker Extraction
- Action Classification
- Conviction Score Estimation

**Limitations**: N/A

## 💾 Data

**Source**: YouTube videos of financial influencers

**Size**: 6,063 expert-annotated segments

**Format**: CSV

**Annotation**: Manual annotation by expert human annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 scores were calculated based on the model predictions versus expert annotations across the segmentation tasks.

**Interpretation**: A higher F1 score indicates better model performance in correctly identifying stock recommendations and their conviction levels.

**Baseline Results**: Comparative baseline results are provided for multiple MLLMs and LLMs across full-length and segmented video inputs.

**Validation**: Five expert annotators conducted peer reviews, and a validation tool flagged inconsistencies in annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
