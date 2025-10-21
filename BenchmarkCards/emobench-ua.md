# EMOBENCH-UA

## 📊 Benchmark Details

**Name**: EMOBENCH-UA

**Overview**: EMOBENCH-UA is the first manually annotated benchmark dataset for emotion detection in Ukrainian texts created through a crowdsourcing annotation pipeline.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Ukrainian

**Resources**:
- [Resource](https://huggingface.co/datasets/ukr-detect/ukr-emotions-binary)
- [Resource](https://huggingface.co/datasets/ukr-detect/ukr-emotions-intensity)
- [Resource](https://huggingface.co/datasets/ukr-detect/ukr-emotions-per-annotator)
- [Resource](https://huggingface.co/ukr-detect/ukr-emotions-classifier)
- [GitHub Repository](https://github.com/dardem/emobench-ua)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for emotion detection in Ukrainian texts to encourage the development of Ukrainian-specific models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Emotion Detection

**Limitations**: The dataset is restricted to basic emotions and does not include nuanced or implicit emotional states.

## 💾 Data

**Source**: Publicly available Ukrainian tweets corpus

**Size**: 4,949 examples

**Format**: JSON

**Annotation**: Crowdsourced annotation through the Toloka.ai platform with multiple quality control measures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Classifier performance evaluation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: F1 Score computed per emotion and overall using Precision and Recall.

**Interpretation**: Higher F1 Score indicates better performance in classifying emotions correctly.

**Validation**: The dataset was validated through majority voting from multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All texts were anonymized to avoid personal and sensitive information disclosure.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
