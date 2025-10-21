# Q-Bench

## 📊 Benchmark Details

**Name**: Q-Bench

**Overview**: Q-Bench is a benchmark constructed to systematically evaluate the low-level visual perception, description, and quality assessment abilities of Multi-modality Large Language Models (MLLMs). It includes tasks such as answering questions based on visual attributes, generating descriptions for images, and aligning predictions with human opinion scores.

**Data Type**: image-question-answer pairs, image-description pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://q-future.github.io/Q-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the low-level visual abilities of MLLMs, aiming to bridge the gap in understanding low-level visual perception and related attributes.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning
- Image Quality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: LLVisionQA and LLDescribe datasets

**Size**: 3,489 images (2,990 for perception, 499 for description, 81,284 from existing IQA datasets)

**Format**: N/A

**Annotation**: LLVisionQA contains questions and answers derived from human sources, while LLDescribe includes expert-written descriptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- GPT-assisted evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of MLLMs against the gold standard of human-written answers and descriptions.

**Interpretation**: Higher scores indicate better alignment with human opinion and understanding of low-level visual attributes.

**Baseline Results**: MLLM performance on each task, compared to human performance.

**Validation**: Testing across multiple MLLMs to observe variations in low-level visual tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
