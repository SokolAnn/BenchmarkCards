# ZOFIE (Zero-shot Open-source Fine-grained Image Editing)

## 📊 Benchmark Details

**Name**: ZOFIE (Zero-shot Open-source Fine-grained Image Editing)

**Overview**: ZOFIE is the first diffusion-based image editing benchmark that incorporates both human subjective and automatic objective machine evaluations, assessing image quality, controllability of fine-grained edits, image-text consistency, background preservation, and semantic disentanglement.

**Data Type**: image editing examples

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- TEDBench
- PIEBench

**Resources**:
- [Resource](https://anonymous.com/anonymous/EMS-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for fine-grained image editing that incorporates both human and automatic evaluations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available benchmark dataset with human annotations and automatic metrics.

**Size**: 576 images

**Format**: image files

**Annotation**: Human annotations and automatic metrics for editing evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- PSNR
- LPIPS
- SSIM
- CLIPScore
- MLLM-VQA score

**Calculation**: Metrics are calculated based on the differences between images during editing and their effectiveness in achieving the editing goals.

**Interpretation**: Higher scores indicate better editing performance and more accurate semantic adjustments.

**Validation**: Empirical validation through various editing tasks and extensive user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
