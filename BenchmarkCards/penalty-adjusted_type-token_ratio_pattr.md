# Penalty-Adjusted Type-Token Ratio (PATTR)

## 📊 Benchmark Details

**Name**: Penalty-Adjusted Type-Token Ratio (PATTR)

**Overview**: PATTR is a diversity metric designed to mitigate the inherent bias of conventional metrics towards shorter responses by incorporating task-specific target response lengths.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.15092)

## 🎯 Purpose and Intended Users

**Goal**: To enhance diversity measurement in generated texts and facilitate synthetic data curation for language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation

**Limitations**: The proposed method requires a task-specific target length and primarily focuses on lexical diversity.

## 💾 Data

**Source**: Generated synthetic corpus from multiple models including LLaMA and OLMo.

**Size**: 20,000,000 words

**Format**: Raw text files

**Annotation**: Diversity measurements are included for the synthetic corpus.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Penalty-Adjusted Type-Token Ratio (PATTR)
- Moving-Average TTR (MATTR)
- Compression Ratio (CR)

**Calculation**: PATTR incorporates a penalty based on the difference from a target response length, adjusting conventional TTR scores.

**Interpretation**: Higher PATTR scores indicate greater lexical diversity, accounting for the task's target response length.

**Validation**: Evaluated through comparative analysis against MATTR and CR metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
