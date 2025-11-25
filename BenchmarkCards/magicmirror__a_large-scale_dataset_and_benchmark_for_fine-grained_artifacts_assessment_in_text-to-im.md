# MAGICMIRROR: A LARGE-SCALE DATASET AND BENCHMARK FOR FINE-GRAINED ARTIFACTS ASSESSMENT IN TEXT-TO-IMAGE GENERATION

## 📊 Benchmark Details

**Name**: MAGICMIRROR: A LARGE-SCALE DATASET AND BENCHMARK FOR FINE-GRAINED ARTIFACTS ASSESSMENT IN TEXT-TO-IMAGE GENERATION

**Overview**: MagicMirror is a comprehensive framework for systematically evaluating physical artifacts in text-to-image generation. It introduces MagicData340K, the first human-annotated large-scale dataset with fine-grained artifact labels, and MagicBench, an automated benchmark for evaluating artifacts in T2I models.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://wj-inf.github.io/MagicMirror-page/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for assessing artifacts in text-to-image generation models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Image Quality Assessment
- Artifact Detection

**Limitations**: N/A

## 💾 Data

**Source**: MagicData340K - a collection of 340,000 generated image-text pairs annotated with fine-grained artifact labels.

**Size**: 340,000 images

**Format**: N/A

**Annotation**: Manual annotation by human experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on true positives, false positives, and false negatives across multiple artifact categories.

**Interpretation**: Higher precision and recall indicate better performance in detecting and assessing image artifacts.

**Validation**: Validation conducted through comparisons with existing models and evaluation on a test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack, Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
