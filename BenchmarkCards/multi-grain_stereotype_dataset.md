# Multi-Grain Stereotype Dataset

## 📊 Benchmark Details

**Name**: Multi-Grain Stereotype Dataset

**Overview**: This work introduces the Multi-Grain Stereotype Dataset, which includes 52,751 instances of gender, race, profession and religion stereotypic text aimed at improving text-based stereotype detection and evaluation of biased outputs in large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-Pairs

**Resources**:
- [GitHub Repository](https://github.com/981526092/Towards-Auditing-Large-Language-Models)

## 🎯 Purpose and Intended Users

**Goal**: To establish a robust and practical framework for auditing and evaluating the stereotypic bias in large language models.

**Target Audience**:
- ML Researchers
- Ethical AI Practitioners

**Tasks**:
- Stereotype Detection
- Bias Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from two crowdsourced sources: StereoSet and CrowS-Pairs.

**Size**: 52,751 instances

**Format**: N/A

**Annotation**: Manually annotated with three labeling categories: 'stereotype', 'anti-stereotype', and 'unrelated'.

## 🔬 Methodology

**Methods**:
- Fine-tuning Distil-BERT models
- Explainability techniques: SHAP, LIME, BERTViz

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on multi-class vs single-class settings in the classification task.

**Interpretation**: Higher values in Precision, Recall, and F1 Score indicate better stereotype detection performance.

**Validation**: Training and testing are done with an 80:20 split using stratified sampling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
