# AstroMMBench

## 📊 Benchmark Details

**Name**: AstroMMBench

**Overview**: AstroMMBench is the first benchmark specifically designed to evaluate the performance of multimodal large language models (MLLMs) in the domain of astronomical image interpretation, comprising 621 multiple-choice questions curated across six core subfields of astrophysics.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MathVista
- MathVerse
- MedXpertQA

**Resources**:
- [Resource](https://arxiv.org/abs/2510.00063)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for assessing MLLM performance in astronomical image understanding and advance the development of models with better capabilities for scientific applications.

**Target Audience**:
- ML Researchers
- Astronomy Experts
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: Limited benchmark size and task diversity.

## 💾 Data

**Source**: Images and textual content sourced from publicly available preprints on arXiv in the 'Astrophysics' (astro-ph) category.

**Size**: 621 questions

**Format**: N/A

**Annotation**: Questions generated through an automated pipeline and reviewed by domain experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert review

**Metrics**:
- Accuracy

**Calculation**: A model's response is considered correct only if the extracted answer option precisely matches the predefined correct answer.

**Interpretation**: Higher accuracy indicates better performance of MLLMs in understanding astronomical images.

**Validation**: Evaluated through the VLMEvalKit framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Complies with copyright regulations as per arXiv's terms of use.

**Data Licensing**: Released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
