# SCPOS (Sentiment Text Classification and Part of Speech Dataset)

## 📊 Benchmark Details

**Name**: SCPOS (Sentiment Text Classification and Part of Speech Dataset)

**Overview**: The SCPOS dataset is created for Japanese sentiment analysis, providing sentiment polarity labels at both the text and word levels, addressing the lack of such datasets for Japanese.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- MARC-ja

**Resources**:
- [Resource](https://huggingface.co/ganchengguang/USA-7B-instruction-incontext-learning)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for sentiment analysis tasks in Japanese, supporting both text-level and word-level sentiment classification.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Manual annotation and rule-based matching using existing Japanese polarity dictionaries

**Size**: 2,500 samples

**Format**: JSON

**Annotation**: Manual annotation and automatic annotation via fine-tuned GPT-3.5 model

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct classifications among predicted samples.

**Interpretation**: Higher accuracy indicates better performance in sentiment classification.

**Baseline Results**: USA-7B model achieved highest accuracy at 91.50% in the Sentiment Related Word classification task.

**Validation**: The dataset was validated through testing different models against it.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
