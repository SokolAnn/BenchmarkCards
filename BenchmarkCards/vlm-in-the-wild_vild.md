# VLM-in-the-Wild (ViLD)

## 📊 Benchmark Details

**Name**: VLM-in-the-Wild (ViLD)

**Overview**: ViLD is a comprehensive framework for evaluating Vision-Language Models on operational enterprise requirements, introducing ten business-critical tasks and a novel BlockWeaver Algorithm for enhanced assessment.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Japanese
- Spanish
- Arabic
- Portuguese
- Thai
- French
- Korean
- Hindi
- Indonesian
- Turkish
- Chinese
- Vietnamese

**Similar Benchmarks**:
- MME
- MMBench
- POPE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the gap between academic evaluation and enterprise deployment requirements for Vision-Language Models.

**Target Audience**:
- Enterprise AI Practitioners
- ML Researchers
- Model Developers

**Tasks**:
- Logo Detection
- OCR
- Object Detection
- Human Presence and Demographic Analysis
- Human Activity and Appearance Analysis
- Scene Detection
- Camera Perspective and Media Quality Assessment
- Dominant Color Extraction
- Comprehensive Description
- NSFW Detection

**Limitations**: N/A

## 💾 Data

**Source**: Stratified sampling from a corpus of one million real-world images and videos.

**Size**: 7,500 samples (5,509 images and 1,889 videos)

**Format**: JSON

**Annotation**: Ground truth annotations generated using a proprietary VLM guided by structured prompts.

## 🔬 Methodology

**Methods**:
- Entity Matching
- Human Analysis
- Logo Detection Evaluation
- OCR Evaluation
- Media Description Evaluation

**Metrics**:
- Accuracy
- F1 Score
- Character Error Rate (CER)
- Word Error Rate (WER)

**Calculation**: Metrics calculated based on the correspondence between predicted and ground truth outputs, employing novel semantic matching techniques.

**Interpretation**: Results interpreted through precision, recall, contextual accuracy, and compliance with detailed annotations.

**Validation**: Internal evaluation against benchmarks provided by leading Vision-Language Models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
