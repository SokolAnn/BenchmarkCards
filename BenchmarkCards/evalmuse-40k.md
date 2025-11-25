# EvalMuse-40K

## 📊 Benchmark Details

**Name**: EvalMuse-40K

**Overview**: EvalMuse-40K collects 40K image-text pairs with comprehensive fine-grained human annotations for evaluating image-text alignment metrics for Text-to-Image generation models.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- DrawBench
- GenAI-Bench
- T2I-CompBench

**Resources**:
- [Resource](https://shh-han.github.io/EvalMuse-project/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable and fine-grained benchmark for evaluating image-text alignment in Text-to-Image generation models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image-Text Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Image-text pairs generated using various diffusion-based T2I models and real user prompts from DiffusionDB.

**Size**: 40,000 image-text pairs

**Format**: N/A

**Annotation**: Manual annotations by human evaluators for image-text alignment and structural problems in generated images.

## 🔬 Methodology

**Methods**:
- End-to-end fine-tuning
- Positive-Negative Visual Question Answering (VQA)

**Metrics**:
- Alignment Scores

**Calculation**: Alignment scores are calculated by evaluating the match between generated images and the corresponding text prompts based on human annotations.

**Interpretation**: Higher alignment scores indicate better correspondence between generated images and input prompts.

**Validation**: Evaluations performed used split datasets with no overlaps between training and test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
