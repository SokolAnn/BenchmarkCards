# JEEM

## 📊 Benchmark Details

**Name**: JEEM

**Overview**: JEEM is a benchmark designed to evaluate Vision-Language Models (VLMs) on visual understanding across four Arabic-speaking countries: Jordan, The Emirates, Egypt, and Morocco. It includes image captioning and visual question answering tasks, featuring culturally rich and regionally diverse content.

**Data Type**: image-caption pairs, question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Arabic

**Similar Benchmarks**:
- AraCOCO
- V AQA
- CVQA

**Resources**:
- [Resource](https://huggingface.co/datasets/toloka/JEEM)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of Vision-Language Models to generalize across dialects and accurately interpret cultural elements in visual contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Cultural Analysts

**Tasks**:
- Image Captioning
- Visual Question Answering

**Limitations**: The dataset focuses on only four Arabic dialects, limiting a comprehensive and inclusive evaluation.

## 💾 Data

**Source**: Combination of publicly available images from Wikimedia, Flickr, and personal collections of team members.

**Size**: 2,178 images

**Format**: JSON

**Annotation**: Annotated by native speakers of the target dialects with captions in both MSA and dialect, and question-answer pairs in dialect.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- GPT-4-based evaluation

**Metrics**:
- CIDEr
- BLEU Score
- ROUGE
- BERTScore

**Calculation**: Metrics are calculated by comparing generated captions and answers against reference captions and answers.

**Interpretation**: Higher scores indicate better alignment with human expectations of captions and answers.

**Baseline Results**: Evaluation against both automated metrics and human judgments.

**Validation**: Results assessed through a combination of automated and human evaluation methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Cultural Sensitivity
- Model Limitations

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**
- **Societal Impact**

**Demographic Analysis**: Analysis conducted on annotators' demographics to ensure diversity.

**Potential Harm**: ['Bias in model performance across different dialects']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotation and survey results are collected and stored anonymously.

**Data Licensing**: The images are subject to the licensing terms of Wikimedia Commons and Flickr, while annotations are distributed under the MIT license.

**Consent Procedures**: Writers are informed in advance about potentially sensitive content.

**Compliance With Regulations**: Not Applicable
