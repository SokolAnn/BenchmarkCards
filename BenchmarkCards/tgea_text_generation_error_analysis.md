# TGEA (Text Generation Error Analysis)

## 📊 Benchmark Details

**Name**: TGEA (Text Generation Error Analysis)

**Overview**: TGEA is an error-annotated dataset with multiple benchmark tasks for text generation from pretrained language models (PLMs), aimed at diagnosing and understanding text generation capabilities and errors.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://download.mindspore.cn/dataset/TGEA/)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the capability of pretrained language models in text generation and to provide a dataset for automatic error detection and correction.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Erroneous Sentence Detection
- Erroneous Span Detection
- Error Type Classification
- Error Correction
- Error Rationale Generation

**Limitations**: N/A

## 💾 Data

**Source**: Machine-generated texts from a Chinese GPT-2 model using carefully crafted prompts.

**Size**: 47,058 sentences

**Format**: JSON

**Annotation**: Manual annotation by crowdsourced workers, including error types and rationales.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on predictions made by models against true labels.

**Interpretation**: Results are interpreted as indicative of model performance in accurately detecting and correcting errors.

**Baseline Results**: Results provided for models including BERT, RoBERTa, and ALBERT on various tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
