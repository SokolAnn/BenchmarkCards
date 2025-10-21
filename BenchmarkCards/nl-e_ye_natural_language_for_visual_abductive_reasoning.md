# NL-E YE (Natural Language for Visual Abductive Reasoning)

## 📊 Benchmark Details

**Name**: NL-E YE (Natural Language for Visual Abductive Reasoning)

**Overview**: NL-E YE is a benchmark designed to assess VLMs’ visual abductive reasoning skills by adapting the abductive Natural Language Inference task to the visual domain. It evaluates the plausibility of hypothesis images based on a premise image and requires models to explain their decisions.

**Data Type**: image triplets

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://venturamor.github.io/NLEye/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual abductive reasoning capabilities of visual language models (VLMs) and identify their weaknesses in reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Plausibility Prediction
- Plausibility Explanation

**Limitations**: N/A

## 💾 Data

**Source**: Data curated from human-written descriptions and generated images using text-to-image models.

**Size**: 350 triplets (1,050 images)

**Format**: Images and textual annotations

**Annotation**: Manual curation by experts involving writing descriptions, generating images, and creating explanations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct predictions against total predictions.

**Interpretation**: Higher accuracy indicates better performance in abductive reasoning tasks.

**Baseline Results**: Humans achieved 85% accuracy while VLMs performed significantly lower, often at random baseline levels.

**Validation**: The benchmark was validated by comparing human performance against VLMs across multiple input types and settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes AI-generated images; potential for sensitive content was recognized and mitigated as much as possible.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
