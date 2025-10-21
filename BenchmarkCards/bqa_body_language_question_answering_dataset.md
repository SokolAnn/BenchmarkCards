# BQA (Body Language Question Answering Dataset)

## 📊 Benchmark Details

**Name**: BQA (Body Language Question Answering Dataset)

**Overview**: A body language question answering dataset that evaluates whether Video Large Language Models (VideoLLMs) can correctly interpret emotions from videos of body language comprising 26 emotion labels.

**Data Type**: video-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- BoLD (Body Language Dataset)

**Resources**:
- [Resource](https://huggingface.co/datasets/naist-nlp/BQA)

## 🎯 Purpose and Intended Users

**Goal**: To validate whether VideoLLMs can correctly interpret emotions from body language in videos.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the Body Language Dataset (BoLD) and designed for evaluation of VideoLLMs.

**Size**: 7,632 videos

**Format**: N/A

**Annotation**: Crowdsourced annotation of emotions on a 10-point scale.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Performance metrics calculated based on the predictions made by VideoLLMs against the annotated categories.

**Interpretation**: Higher accuracy indicates better understanding of emotions expressed through body language.

**Validation**: Dataset validation involved human evaluation across various demographics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Yes, includes metadata on gender, age, and ethnicity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
