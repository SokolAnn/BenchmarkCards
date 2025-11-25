# Food-500 Cap (A Fine-Grained Food Caption Benchmark for Evaluating Vision-Language Models)

## 📊 Benchmark Details

**Name**: Food-500 Cap (A Fine-Grained Food Caption Benchmark for Evaluating Vision-Language Models)

**Overview**: Food-500 Cap is a newly proposed benchmark dataset consisting of 24,700 food images with fine-grained captions detailing food attributes and geographic origins. It aims to evaluate vision-language models in the food domain, addressing their performance and biases across different culinary cultures.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- ISIA Food-500

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the vision-language model's performance in the food domain and identify limitations and biases in culinary culture.

**Target Audience**:
- ML Researchers
- Computer Vision Researchers
- Food Technologists

**Tasks**:
- Food Classification
- Image-Text Retrieval
- Image Captioning
- Image Synthesis

**Limitations**: N/A

## 💾 Data

**Source**: ISIA Food-500 dataset, annotated by a data annotation company, with descriptions of fine-grained visual features and geographic origins.

**Size**: 24,700 images

**Format**: N/A

**Annotation**: Human-annotated fine-grained descriptions including color, shape, and geographic origin.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Probing tasks

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE
- CIDEr

**Calculation**: Metrics are calculated based on the performance of nine vision-language models on set tasks.

**Interpretation**: Models underperformed in food-related tasks compared to general benchmarks, revealing significant biases.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes annotations based on geographic regions, allowing for analysis of model performance across different culinary cultures.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
