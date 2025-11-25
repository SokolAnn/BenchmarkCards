# PARAPHRASUS

## 📊 Benchmark Details

**Name**: PARAPHRASUS

**Overview**: PARAPHRASUS is a multi-faceted evaluation benchmark for paraphrase detection models, comprising ten parts with eight repurposed datasets and two newly annotated datasets, aiming to capture diverse paraphrase phenomena.

**Data Type**: paraphrase sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/impresso/paraphrasus)

## 🎯 Purpose and Intended Users

**Goal**: To enable a multi-dimensional assessment of paraphrase detection models and facilitate the selection of models for different paraphrase challenges.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Paraphrase Detection

**Limitations**: N/A

## 💾 Data

**Source**: PARAPHRASUS includes 10 parts sourced from various NLP datasets along with newly annotated examples.

**Size**: 35,782 examples across different datasets

**Format**: JSON

**Annotation**: Manual annotation by experts and crowdsourcing methods for new datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Classification error percentage

**Calculation**: The classification error percentage is calculated as the ratio of wrong predictions for the datasets in each challenge.

**Interpretation**: Lower error percentages indicate better performance in identifying paraphrases correctly.

**Baseline Results**: N/A

**Validation**: Average performance based on multiple model checkpoints to reduce variance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
