# MVL-SIB (Massively Multilingual Vision-Language Benchmark)

## 📊 Benchmark Details

**Name**: MVL-SIB (Massively Multilingual Vision-Language Benchmark)

**Overview**: MVL-SIB is a massively multilingual vision-language benchmark that evaluates cross-modal and text-only topical matching across 205 languages. It addresses the need for evaluation data for low-resource languages, significantly extending the number of languages covered by existing benchmarks.

**Data Type**: cross-modal and text-only topic matching tasks (image-sentence and sentence-image pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- 205 languages (including low-resource languages)

**Similar Benchmarks**:
- SIB-200

**Resources**:
- [Resource](https://arxiv.org/abs/2502.12852)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MVL-SIB is to provide a comprehensive benchmark for evaluating large vision-language models (LVLMs) in cross-modal topic matching across a wide array of languages, particularly focusing on low-resource languages.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Cross-modal Topic Matching
- Text-only Topic Matching

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is derived from Flores and SIB-200, professionally translated into 205 languages, with associated images for each topic.

**Size**: 3,012 instances

**Format**: N/A

**Annotation**: Hand-selected images associated with manually curated topic labels.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Relaxed Accuracy

**Calculation**: Metrics are computed based on the proportion of correct responses provided by the models when selecting appropriate text or images for given prompts.

**Interpretation**: Higher accuracy reflects better topical matching performance by the models across different languages, especially in low-resource settings.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
