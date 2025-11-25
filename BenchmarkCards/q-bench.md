# Q-Bench+

## 📊 Benchmark Details

**Name**: Q-Bench+

**Overview**: Q-Bench+ is designed to evaluate the low-level visual abilities of Multi-modality Large Language Models (MLLMs) with three main tasks: low-level visual perception, low-level visual description, and quality assessment of images. The benchmark includes both single images and image pairs for comprehensive evaluation.

**Data Type**: image-question pairs, text descriptions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Q-Future/Q-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark to evaluate the low-level visual skills of MLLMs across various tasks, simulating human-like understanding of images.

**Target Audience**:
- ML Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Image Captioning
- Image Quality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from diverse image sources including in-the-wild, artificially distorted, and AI-generated images.

**Size**: 2,990 single images and 1,999 image pairs for LLVisionQA+, 499 single images and 450 image pairs for LLDescribe+

**Format**: Images and text files

**Annotation**: Expert annotations for descriptions, automated generation of questions and answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- GPT-assisted evaluation
- Quantitative analysis through softmax pooling

**Metrics**:
- Accuracy
- SRCC (Spearman's Rank-Order Correlation Coefficient)
- PLCC (Pearson Linear Correlation Coefficient)

**Calculation**: Metrics are calculated based on model predictions compared to human evaluations, using scores derived from softmax probabilities.

**Interpretation**: Performance is evaluated based on the alignment of MLLM outputs with human judgments on low-level image characteristics.

**Baseline Results**: Performance metrics on open-source models with specific accuracy rates on each benchmark task.

**Validation**: Validation through comparison with human assessments and through comprehensive dataset design.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
