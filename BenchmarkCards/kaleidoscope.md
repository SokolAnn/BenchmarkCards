# Kaleidoscope

## 📊 Benchmark Details

**Name**: Kaleidoscope

**Overview**: Kaleidoscope is a large-scale, in-language multimodal benchmark designed to evaluate vision-language models (VLMs) across 18 languages and 14 different subjects, consisting of 20,911 multiple-choice questions that emphasize vision-grounded reasoning.

**Data Type**: multiple-choice question answering

**Domains**:
- Natural Language Processing
- Computer Vision
- Education

**Languages**:
- English
- Spanish
- Portuguese
- Russian
- Arabic
- Hindi
- Bengali
- Serbian
- Lithuanian
- Nepali
- Telugu
- Ukrainian
- German
- French

**Similar Benchmarks**:
- M3Exam
- EXAMS-V

**Resources**:
- [Resource](http://cohere.com/research/kaleidoscope)
- [Resource](https://hf.co/datasets/CohereForAI/kaleidoscope)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and inclusive evaluation framework for multimodal language models through real-world, in-language exam questions.

**Target Audience**:
- ML Researchers
- Model Developers
- Education Researchers

**Tasks**:
- Multimodal Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real-world exams, sourced directly in original languages with no translations.

**Size**: 20,911 questions

**Format**: JSON

**Annotation**: Manually annotated with a rigorous validation process to ensure quality and authenticity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Format Error Rate

**Calculation**: Accuracy is calculated based on the number of correctly answered questions against the total number of questions, along with valid response tracking.

**Interpretation**: A higher accuracy indicates better model performance in understanding and answering the multimodal questions.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through multi-stage manual review and automated scripts to detect formatting errors and duplicates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: The benchmark includes a diverse set of languages, focusing on both high-resource and low-resource languages to investigate performance disparities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not include personally identifiable information and has been sourced from publicly available materials.

**Data Licensing**: Data from contributors allows redistribution and academic use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
