# FLUX-Reason-6M & PRISM-Bench

## 📊 Benchmark Details

**Name**: FLUX-Reason-6M & PRISM-Bench

**Overview**: FLUX-Reason-6M is a massive dataset consisting of 6 million high-quality FLUX-generated images and 20 million bilingual (English and Chinese) descriptions designed to teach complex reasoning. PRISM-Bench offers a novel evaluation standard with seven distinct tracks for evaluating text-to-image models.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://flux-reason-6m.github.io)
- [GitHub Repository](https://github.com/rongyaofang/prism-bench)
- [Resource](https://huggingface.co/datasets/LucasFang/FLUX-Reason-6M)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, reasoning-focused dataset and a comprehensive evaluation benchmark for text-to-image generation models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text-to-Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: FLUX-generated images and bilingual captions

**Size**: 6 million images and 20 million captions

**Format**: N/A

**Annotation**: High-quality dense captioning with a structured reasoning framework.

## 🔬 Methodology

**Methods**:
- Automated evaluation using vision-language models
- Human-aligned assessment

**Metrics**:
- Alignment score
- Aesthetic score

**Calculation**: Scores based on model performance in seven categories.

**Interpretation**: High scores indicate effective image synthesis aligned with prompts.

**Baseline Results**: Results from evaluating 19 state-of-the-art models.

**Validation**: Extensive evaluation on multiple leading T2I models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Prompt injection attack
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
