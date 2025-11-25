# MME VALPRO

## 📊 Benchmark Details

**Name**: MME VALPRO

**Overview**: MME VALPRO is a multimodal benchmark designed to avoid Type-I errors in evaluating Large Multimodal Models (LMMs) through a trilogy evaluation pipeline, consisting of an original question, a perception question, and a knowledge anchor question. It demonstrates a more accurate reflection of LMM capabilities and fosters trustworthiness in evaluations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMMU
- ScienceQA
- MathVista

**Resources**:
- [Resource](https://mmevalpro.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To address issues in existing multimodal evaluation benchmarks and provide a more rigorous and trustworthy assessment of large multimodal models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MMMU (validation set), ScienceQA (image subset), MathVista (test mini set)

**Size**: 2,138 question triplets, 6,414 unique questions

**Format**: N/A

**Annotation**: Questions were manually labeled by human experts and sourced from existing benchmarks.

## 🔬 Methodology

**Methods**:
- Evaluation against existing benchmarks
- Human evaluation for validation

**Metrics**:
- Genuine Accuracy
- Average Accuracy
- Perception Accuracy
- Knowledge Accuracy
- Consistency Gap

**Calculation**: Genuine Accuracy is determined by whether the model answers the original question and both corresponding perception and knowledge questions correctly.

**Interpretation**: Higher Genuine Accuracy indicates better true understanding of multimodal capabilities.

**Validation**: The dataset was evaluated by graduate students, and a double-checking process was performed by independent reviewers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
