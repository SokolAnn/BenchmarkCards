# SuperEmotion

## 📊 Benchmark Details

**Name**: SuperEmotion

**Overview**: The SuperEmotion dataset addresses the gap in standardized, large-scale emotion classification resources by harmonizing diverse text sources into a unified framework based on Shaver’s empirically validated emotion taxonomy. It enables more consistent cross-domain emotion recognition research.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MELD
- GoEmotions
- TwitterEmotion
- ISEAR
- SemEval
- CrowdFlower

**Resources**:
- [Resource](https://huggingface.co/datasets/cirimus/super-emotion)

## 🎯 Purpose and Intended Users

**Goal**: To contribute to emotion recognition research by providing a large-scale, harmonized dataset that follows a psychologically grounded taxonomy for improved emotion classification.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Emotion Classification

**Limitations**: Dataset biases, contextual limitations, annotation quality issues, and privacy considerations are acknowledged.

## 💾 Data

**Source**: Aggregated from multiple existing emotion datasets including MELD, GoEmotions, TwitterEmotion, ISEAR, SemEval, and CrowdFlower.

**Size**: 519,812 samples

**Format**: N/A

**Annotation**: Managed through label harmonization based on Shaver’s emotion taxonomy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on label harmonization and sample distributions across defined emotion categories.

**Interpretation**: Good performance indicates robust emotion classification across diverse datasets, while poor performance may signal issues with label harmonization.

**Baseline Results**: N/A

**Validation**: The dataset was validated through stratified partitioning and consistency checks during preprocessing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets excluded personally identifiable information, but privacy considerations remain when deploying models.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
