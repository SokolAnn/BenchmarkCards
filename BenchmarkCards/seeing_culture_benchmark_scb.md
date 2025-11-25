# Seeing Culture Benchmark (SCB)

## 📊 Benchmark Details

**Name**: Seeing Culture Benchmark (SCB)

**Overview**: The Seeing Culture Benchmark (SCB) focuses on cultural reasoning with a novel approach requiring VLMs to reason on culturally rich images through multiple-choice VQA and segmentation tasks. It comprises 1,065 images and 3,178 questions highlighting cultural artifacts across seven Southeast Asian countries.

**Data Type**: multiple-choice visual question answering and segmentation

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://seeingculture-benchmark.github.io)
- [Resource](https://huggingface.co/datasets/Multimedia-SMU/seeingculture-benchmark)
- [GitHub Repository](https://github.com/buraksatar/SeeingCulture)

## 🎯 Purpose and Intended Users

**Goal**: To assess the cultural reasoning of Vision-Language Models (VLMs) on culturally rich images from Southeast Asia.

**Target Audience**:
- ML Researchers
- Cultural Studies Experts
- Data Scientists

**Tasks**:
- Visual Question Answering
- Image Segmentation

**Limitations**: Challenges in sourcing sufficient cultural concepts from specific nations.

## 💾 Data

**Source**: Images crawled from Google Images based on curated cultural concepts.

**Size**: 1,065 images and 3,178 questions

**Format**: JSON

**Annotation**: Questions and segmentation masks created by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- Mean Intersection over Union (mIoU)

**Calculation**: Metrics calculated using standard methodologies for multiple-choice VQA and segmentation.

**Interpretation**: Accuracy indicates the effectiveness of answering questions, while mIoU measures the quality of segmentation.

**Validation**: Evaluated on selected state-of-the-art Vision-Language Models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Focused on cultural representation across seven Southeast Asian countries.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured that collected data respects intellectual property and privacy rights of images.

**Data Licensing**: CC BY-NC-SA 4.0 license for non-commercial research use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
