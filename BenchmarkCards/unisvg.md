# UniSVG

## 📊 Benchmark Details

**Name**: UniSVG

**Overview**: UniSVG is the first large-scale, multi-task, open-source SVG-centric dataset designed for unified SVG generation (from textual prompts and images) and SVG understanding, supporting MLLM training and evaluation.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- SVGEditBench
- VGBench
- SVG-Stack

**Resources**:
- [Resource](https://ryanlijinke.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate SVG generation and understanding in the era of MLLMs and evaluate MLLM performance on SVG tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image to SVG Generation
- Text to SVG Generation
- SVG Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Cleaned SVG codes collected from online open-source SVG resources.

**Size**: 525,000 examples

**Format**: SVG, PNG

**Annotation**: Manual annotation through refinement and rendering techniques.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Structural Similarity Index (SSIM)
- Learned Perceptual Image Patch Similarity (LPIPS)
- CLIP score

**Calculation**: Metrics for SVG generation tasks are evaluated based on the similarity of generated SVG images to ground-truth SVG images and the correctness of model outputs in understanding tasks.

**Interpretation**: A higher score indicates better performance in generating and understanding SVGs, while lower scores in pixel-level metrics indicate a need for visual detail and structural accuracy.

**Baseline Results**: N/A

**Validation**: Data cleaning and rigorous evaluation metrics applied to ensure dataset and model integrity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
