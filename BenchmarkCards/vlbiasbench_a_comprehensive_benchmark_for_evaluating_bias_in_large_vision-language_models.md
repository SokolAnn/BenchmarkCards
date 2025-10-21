# VLBiasBench (A Comprehensive Benchmark for Evaluating Bias in Large Vision-Language Models)

## 📊 Benchmark Details

**Name**: VLBiasBench (A Comprehensive Benchmark for Evaluating Bias in Large Vision-Language Models)

**Overview**: VLBiasBench is a comprehensive benchmark designed to evaluate biases in Large Vision-Language Models (LVLMs) across multiple categories, using a dataset that includes 128,342 samples generated from 46,848 high-quality images and various questions.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Fairface
- UTKFace
- MS-COCO
- Flickr30k

**Resources**:
- [GitHub Repository](https://github.com/Xiangkui-Cao/VLBiasBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing biases in Large Vision-Language Models (LVLMs).

**Target Audience**:
- ML Researchers
- Domain Experts
- AI Practitioners

**Tasks**:
- Bias Evaluation
- Visual Question Answering

**Limitations**: Current benchmark may still lack comprehensive coverage of all bias categories.

## 💾 Data

**Source**: Generated synthetic data using Stable Diffusion XL model.

**Size**: 128,342 samples

**Format**: N/A

**Annotation**: Synthesized images matched with bias-related questions, categorized into open-ended and close-ended types.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Bias evaluation scores using VADER
- Accuracy

**Calculation**: Metrics are calculated based on sentiment analysis of the textual responses from LVLMs.

**Interpretation**: Higher scores indicate a greater degree of bias.

**Validation**: Results validated through extensive evaluations on multiple models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Evaluation includes various demographic factors across multiple bias categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Strict controls over prompt safety to prevent generation of NSFW or offensive content.

**Data Licensing**: Data utilized from CC-BY-NC-SA 4.0 licensed datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
