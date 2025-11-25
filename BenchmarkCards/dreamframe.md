# DreamFrame

## 📊 Benchmark Details

**Name**: DreamFrame

**Overview**: DreamFrame is a novel framework for generating video instruction tuning datasets that includes style-consistent keyframes and corresponding question-answer pairs for enhancing video understanding in large vision-language models.

**Data Type**: keyframe-like videos and question-answer pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ActivityNet
- TVQA
- FunQA

**Resources**:
- [Resource](https://deaddawn.github.io/DreamFrame)

## 🎯 Purpose and Intended Users

**Goal**: To generate high-quality, style-consistent video instruction datasets that enhance the performance of vision-language models for video understanding tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering
- Video Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated from structured movie plots using an LLM and diffusion models.

**Size**: 1,000 stylized videos and 100,000 diverse QA pairs

**Format**: N/A

**Annotation**: Automatically generated without manual labor.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Mean Average Precision (MAP)

**Calculation**: Performance is validated against existing benchmarks on multi-modal video understanding tasks.

**Interpretation**: Higher scores indicate better alignment between video and question answering.

**Baseline Results**: DreamFrame-7B surpasses previous LVLMs (e.g., VideoLLaVA-7B) by an average margin of 2.2% on MVBench.

**Validation**: Experimental validation on various existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
