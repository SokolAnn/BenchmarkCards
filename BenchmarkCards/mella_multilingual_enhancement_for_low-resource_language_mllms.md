# MELLA (Multilingual Enhancement for Low-resource Language MLLMs)

## 📊 Benchmark Details

**Name**: MELLA (Multilingual Enhancement for Low-resource Language MLLMs)

**Overview**: MELLA is a multimodal, multilingual dataset designed to enhance both linguistic capability and cultural groundedness for low-resource language models, consisting of 6.8 million image-text pairs tailored for effective MLLM training.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Arabic
- Czech
- Hungarian
- Korean
- Russian
- Serbian
- Thai
- Vietnamese

**Resources**:
- [Resource](https://opendatalab.com/applyMultilingualCorpus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that enhances the performance of multimodal large language models by integrating linguistic capability and cultural knowledge for low-resource languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Image Captioning
- Multimodal Learning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from native web alt-text and MLLM-generated captions.

**Size**: 6,800,000 image-text pairs

**Format**: N/A

**Annotation**: Automatically collected and annotated; dual-source approach.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Automated metrics

**Metrics**:
- Keyword Accuracy
- BLEU Score
- ROUGE-L
- METEOR

**Calculation**: Metrics are calculated based on outputs compared to ground truth annotations.

**Interpretation**: Higher scores indicate better performance in generating culturally appropriate and linguistically coherent descriptions.

**Baseline Results**: N/A

**Validation**: Performance validated through experiments across various MLLM architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Cultural Awareness
- Linguistic Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of performance across various low-resource languages highlighting capability variations.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
