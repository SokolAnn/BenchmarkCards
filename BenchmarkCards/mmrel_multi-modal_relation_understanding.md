# MMRel (Multi-Modal Relation Understanding)

## 📊 Benchmark Details

**Name**: MMRel (Multi-Modal Relation Understanding)

**Overview**: MMRel is a benchmark that features large-scale, high-quality, and diverse data on inter-object relations, containing over 22K question-answer pairs and specifically designed to evaluate Multi-Modal Large Language Models (MLLMs) on their relation understanding capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://niejiahao1998.github.io/MMRel)

## 🎯 Purpose and Intended Users

**Goal**: To gauge the capabilities of existing Multi-Modal Large Language Models (MLLMs) in understanding inter-object relations and to enhance their performance through fine-tuning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Relation Understanding
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MMRel contains data collected from Visual Genome (VG) and synthetic images generated via SDXL and Dall-E.

**Size**: 22,500 question-answer pairs

**Format**: N/A

**Annotation**: Data is generated using a semi-automatic pipeline with human verification to ensure annotation accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Evaluation metrics are calculated based on the Yes/No question pairs and generative open-ended evaluations.

**Interpretation**: Higher metrics indicate better model performance in relation understanding tasks.

**Validation**: Extensive experiments conducted to verify the effectiveness of the benchmark and improvement in MLLM performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
