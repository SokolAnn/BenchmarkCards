# DiffuSyn Bench: Evaluating Vision-Language Models on Real-World Complexities with Diffusion-Generated Synthetic Benchmarks

## 📊 Benchmark Details

**Name**: DiffuSyn Bench: Evaluating Vision-Language Models on Real-World Complexities with Diffusion-Generated Synthetic Benchmarks

**Overview**: This study assesses the ability of Large Vision-Language Models (LVLMs) to differentiate between AI-generated and human-generated images, introducing a new automated benchmark construction method for this evaluation.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MM-Vet
- HallusionBench
- humor understanding benchmarks
- MMMU
- VisIT-Bench
- VASR

**Resources**:
- [Resource](https://arxiv.org/abs/2406.04470)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Large Vision-Language Models' ability to understand and interpret images through a novel automated benchmark system.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Error Recognition

**Limitations**: Inherent limitations exist in both text-to-image models and large language models, particularly in producing erroneous images accurately.

## 💾 Data

**Source**: 2000 images from a mix of AI-generated and human-created visuals, standardized to a resolution of 512x512 pixels.

**Size**: 2000 images

**Format**: image files (with accompanying text descriptions)

**Annotation**: Manually curated and automatically generated prompts with errors embedded.

## 🔬 Methodology

**Methods**:
- Automated benchmark generation
- Statistical analysis
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy measures the proportion of correctly predicted instances relative to total predictions; F1 Score is calculated as 2 * (Precision * Recall) / (Precision + Recall).

**Interpretation**: An accuracy of 88.1% signifies good performance, while lower scores for LVLMs indicate limitations in distinguishing image authenticity.

**Baseline Results**: Humans achieved 88.45% accuracy; LVLMs' highest accuracy was 66.1% from the Fuyu-8B model.

**Validation**: Validation through comparison with human scores and consistency checks against other benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
