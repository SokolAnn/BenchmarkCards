# Deciphering the Underserved: Benchmarking LLM OCR for Low-Resource Scripts

## 📊 Benchmark Details

**Name**: Deciphering the Underserved: Benchmarking LLM OCR for Low-Resource Scripts

**Overview**: This study investigates the potential of Large Language Models (LLMs), particularly GPT-4o, for Optical Character Recognition (OCR) in low-resource scripts such as Urdu, Albanian, and Tajik, with English serving as a benchmark. Using a meticulously curated dataset of 2,520 images incorporating controlled variations in text length, font size, background color, and blur, the research simulates diverse real-world challenges.

**Data Type**: image

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Urdu
- Albanian
- Tajik

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the OCR performance of LLMs across low-resource scripts and address the accessibility gaps in text digitization.

**Target Audience**:
- NLP Researchers
- OCR Developers

**Tasks**:
- Optical Character Recognition

**Limitations**: The labor-intensive nature of dataset creation limited the dataset size, preventing the inclusion of additional languages and larger datasets.

## 💾 Data

**Source**: Curated dataset consisting of 2,520 images from news articles sourced from various outlets in Urdu, English, Albanian, and Tajik.

**Size**: 2,520 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot inference

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- BLEU Score

**Calculation**: Metrics are calculated based on edit distances and comparison of n-grams with the reference text.

**Interpretation**: Lower values of CER and WER indicate better OCR performance, while higher BLEU scores reflect better semantic coherence.

**Baseline Results**: N/A

**Validation**: The dataset was assessed under controlled dimensions including word count, font size, background color, and Gaussian blur.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
