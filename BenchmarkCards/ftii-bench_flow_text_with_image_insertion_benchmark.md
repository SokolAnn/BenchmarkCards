# FTII-Bench (Flow Text with Image Insertion Benchmark)

## 📊 Benchmark Details

**Name**: FTII-Bench (Flow Text with Image Insertion Benchmark)

**Overview**: FTII-Bench is designed to comprehensively assess the performance of existing large vision-language models (LVLMs) on a complex task of selecting suitable images for insertion into flowing text, requiring image comprehension, instruction understanding, and long-text interpretation.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- MMLU
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/IAAR-Shanghai/FTIIBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation resource for assessing the performance of large vision-language models on the Flow Text with Image Insertion task.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Image Insertion
- Image Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected from news articles, specifically from Xinhua News and BBC News.

**Size**: 625 articles

**Format**: N/A

**Annotation**: High-quality image-text sequences based on professional news reporting.

## 🔬 Methodology

**Methods**:
- Evaluation of models via accuracy metrics, including the accuracy when images are inserted and not inserted.

**Metrics**:
- Accuracy

**Calculation**: Calculated by comparing the predicted image insertion order against the ground truth sequences.

**Interpretation**: Higher accuracy indicates better performance of the vision-language model in selecting suitable images.

**Validation**: Evaluated performance of 9 open-source LVLMs and 2 closed-source LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
