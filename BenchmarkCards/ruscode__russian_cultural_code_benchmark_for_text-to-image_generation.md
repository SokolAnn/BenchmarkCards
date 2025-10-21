# RusCode: Russian Cultural Code Benchmark for Text-to-Image Generation

## 📊 Benchmark Details

**Name**: RusCode: Russian Cultural Code Benchmark for Text-to-Image Generation

**Overview**: This paper presents the RusCode benchmark dataset for evaluating the quality of text-to-image generation containing elements of the Russian cultural code, consisting of 1250 text prompts in Russian with English translations.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- Russian
- English

**Resources**:
- [GitHub Repository](https://github.com/ai-forever/RusCode)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cultural awareness of text-to-image generation models using a comprehensive dataset of Russian cultural concepts.

**Target Audience**:
- ML Researchers
- Model Developers
- Cultural Analysts

**Tasks**:
- Image Generation

**Limitations**: The dataset may not represent the entirety of the Russian cultural code and includes only a limited number of prompts per subcategory.

## 💾 Data

**Source**: Generated prompts and reference images sourced from open internet resources.

**Size**: 1250 examples

**Format**: JSON

**Annotation**: Prompts were created by a team of 13 prompt-engineers reflecting diverse perspectives.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Side-by-side comparison

**Metrics**:
- Accuracy of representation against reference images

**Calculation**: Quality assessment based on human judgment comparing model-generated images to reference images.

**Interpretation**: Higher accuracy in matching generated images with prompts indicates better cultural understanding.

**Baseline Results**: Comparison of image outputs of four models: Stable Diffusion 3, DALL-E 3, Kandinsky 3.1, and YandexART 2.

**Validation**: Human evaluations conducted across a diverse group of participants.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Cultural Misunderstanding

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: The dataset aims to represent various aspects of Russian culture but may not capture all demographic nuances.

**Potential Harm**: Inadequately trained models may generate culturally insensitive or biased content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT

**Consent Procedures**: Prompt-engineers were informed about the project's objectives and ethical guidelines.

**Compliance With Regulations**: Not Applicable
