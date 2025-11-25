# VISBIAS

## 📊 Benchmark Details

**Name**: VISBIAS

**Overview**: VISBIAS evaluates explicit and implicit social biases exhibited by Vision-Language Models (VLMs) through four distinct assessment scenarios.

**Data Type**: image-description pairs, personal information forms

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BiasDora
- BIGbench
- BiasLens
- SocialCounterfactuals

**Resources**:
- [GitHub Repository](https://github.com/uscnlp-lime/VisBias)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and evaluate both explicit and implicit social biases in Vision-Language Models.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- Model Developers

**Tasks**:
- Explicit Bias Assessment
- Implicit Bias Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Real-world images and crowdsourced personal information forms.

**Size**: 700 images, 400 personal information forms

**Format**: PNG, JSON

**Annotation**: Manual annotation with human input for bias evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Jensen-Shannon Divergence (JSD)
- Kullback-Leibler Divergence (KLD)

**Calculation**: Metrics are calculated based on response distributions of the models during bias evaluation.

**Interpretation**: JSD and KLD values indicate the degree of bias present in model outputs.

**Baseline Results**: Comparison to existing benchmark results not specified.

**Validation**: Quantitative results validated through human assessment and statistical analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes demographic breakdowns across gender and racial lines.

**Potential Harm**: The recognition of harmful stereotypes perpetuated by models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Images used are publicly available and were chosen to minimize privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collection procedures were transparent, and human evaluators were compensated.

**Compliance With Regulations**: Not Applicable
