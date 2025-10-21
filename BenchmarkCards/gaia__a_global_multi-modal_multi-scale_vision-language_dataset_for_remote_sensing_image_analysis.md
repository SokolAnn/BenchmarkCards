# GAIA: A Global, Multi-modal, Multi-scale Vision-Language Dataset for Remote Sensing Image Analysis

## 📊 Benchmark Details

**Name**: GAIA: A Global, Multi-modal, Multi-scale Vision-Language Dataset for Remote Sensing Image Analysis

**Overview**: GAIA is a novel dataset designed for multi-scale, multi-sensor, and multi-modal remote sensing image analysis. It includes 205,150 meticulously curated RS image-text pairs, covering various remote sensing applications and ensuring scientific accuracy in textual descriptions.

**Data Type**: image-text pairs

**Domains**:
- Remote Sensing

**Languages**:
- English

**Similar Benchmarks**:
- RS5M
- RSTeller
- SkyScript

**Resources**:
- [GitHub Repository](https://github.com/Orion-AI-Lab/GAIA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the GAIA dataset is to advance remote sensing image analysis and improve the performance of vision-language models by providing a high-quality, diverse dataset specifically tailored for this domain.

**Target Audience**:
- Researchers in Remote Sensing
- ML Researchers
- Model Developers

**Tasks**:
- Image Captioning
- Cross-modal Retrieval
- Image Classification

**Limitations**: N/A

## 💾 Data

**Source**: Web-scraped images and text from reputable remote sensing sources, with synthetic captions generated using GPT-4o.

**Size**: 205,150 pairs

**Format**: N/A

**Annotation**: Automatically generated captions and metadata.

## 🔬 Methodology

**Methods**:
- Fine-tuning of CLIP models
- Fine-tuning of BLIP2
- Cross-modal retrieval evaluations

**Metrics**:
- Accuracy
- Recall
- BLEU Score
- ROUGE-1
- ROUGE-2
- ROUGE-L
- METEOR

**Calculation**: Metrics calculated to assess model performance on image classification and captioning tasks, comparing baseline results with fine-tuned models.

**Interpretation**: Higher metrics indicate better performance in classifying and retrieving remote sensing images and generating contextually relevant captions.

**Baseline Results**: Baseline results indicated poor performance of zero-shot CLIP models on remote sensing tasks without fine-tuning, with significant improvements observed post fine-tuning.

**Validation**: Validation involved assessments against standard RS benchmarks to measure improvements and effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate geographic grounding of captions', 'Over-reliance on specific automated captioning methods']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
