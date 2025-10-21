# CAPability (Comprehensive Visual Caption Benchmark)

## 📊 Benchmark Details

**Name**: CAPability (Comprehensive Visual Caption Benchmark)

**Overview**: CAPability is a comprehensive multi-view benchmark for evaluating visual captioning across 12 dimensions spanning six critical views. It assesses both the correctness and thoroughness of visual captions using nearly 11K human-annotated images and videos.

**Data Type**: image and video with visual element annotations

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MS-COCO
- DetailCaps
- Dream-1K
- VDC

**Resources**:
- [Resource](https://arxiv.org/abs/2502.14914)

## 🎯 Purpose and Intended Users

**Goal**: To provide a holistic analysis of multimodal large language models’ (MLLMs) capabilities in generating detailed visual captions, identifying their strengths and weaknesses across various dimensions.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated images and videos curated from various datasets and collected via web crawling.

**Size**: 11,000 examples

**Format**: Custom annotations in multiple formats

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Hit
- Know but cannot tell (K¯T)

**Calculation**: Precision is calculated as the number of correct annotations over the total number of evaluated annotations. Hit measures the coverage of visual elements in the generated captions based on annotated examples.

**Interpretation**: Higher precision indicates better caption correctness, while higher hit indicates thoroughness in capturing visual elements.

**Validation**: Cross-validation with multiple models to ensure reliability of the evaluation framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misinformation', 'Perpetuation of biases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data used is governed by various licenses: CC-BY-4.0, Apache-2.0, etc.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
