# MEGAVERSE

## 📊 Benchmark Details

**Name**: MEGAVERSE

**Overview**: MEGAVERSE is a comprehensive benchmark to evaluate the multilingual capabilities of State-of-the-Art (SoTA) Large Language Models (LLMs) and Multimodal Models across 22 datasets covering 83 languages, including low-resource languages. The benchmark also includes a thorough study on data contamination affecting these evaluations.

**Data Type**: text, multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Spanish
- French
- German
- Arabic
- Italian
- Hindi
- Korean
- Japanese
- Russian
- Vietnamese
- Swahili
- Turkish
- Bengali
- Punjabi
- Malay
- Thai
- Zulu
- Yoruba
- Wolof
- Kinyarwanda
- Twi
- Amharic
- Igbo
- Hausa

**Similar Benchmarks**:
- BIG-Bench
- HELM
- MEGA

**Resources**:
- [Resource](https://arxiv.org/abs/2311.07463)

## 🎯 Purpose and Intended Users

**Goal**: The main goal of MEGAVERSE is to provide a detailed evaluation of the multilingual and multimodal capabilities of recent LLMs and multimodal models, allowing researchers to improve these models and understand their capabilities across diverse languages.

**Target Audience**:
- ML Researchers
- Model Developers
- Industrial Practitioners

**Tasks**:
- Natural Language Inference
- Question Answering
- Sentiment Analysis
- Multimodal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark includes 22 datasets covering various multilingual and multimodal tasks, curated from existing open-source resources and new contributions.

**Size**: 22 datasets, covering 83 languages

**Format**: Mixed formats including JSON for text and specific image formats for multimodal datasets.

**Annotation**: Datasets include manual annotations and native speaker verifications for quality control.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Cross-lingual studies
- Task-oriented evaluations

**Metrics**:
- Accuracy
- F1 Score
- BLEU
- ROUGE-L
- Success Rate

**Calculation**: Metrics are computed based on standard practices for each task, including average scores across languages.

**Interpretation**: Results are interpreted in the context of model performance on multilingual tasks, with comparisons to SoTA benchmarks.

**Baseline Results**: Comparisons to models including GPT-4, PaLM2, and Llama2 across various tasks and language families.

**Validation**: The benchmark validates models against comprehensive tasks spanning various languages and modalities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Datasets have undergone ethical reviews and ensure participant anonymity where applicable.

**Data Licensing**: The datasets are released under compliant licenses, with respect to data usage policies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
