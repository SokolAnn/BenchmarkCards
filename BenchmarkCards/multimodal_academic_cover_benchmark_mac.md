# Multimodal Academic Cover benchmark (MAC)

## 📊 Benchmark Details

**Name**: Multimodal Academic Cover benchmark (MAC)

**Overview**: MAC is a live benchmark that dynamically evolves alongside scientific advancements to evaluate multimodal large language models' (MLLMs) scientific understanding capabilities, leveraging over 25,000 image-text pairs from leading scientific journals.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/mhjiang0408/MAC Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the MAC benchmark is to continuously assess MLLMs' ability to comprehend implicit scientific concepts in cover images and associated stories.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Image2Text
- Text2Image

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from the official websites of leading scientific journals including Nature, Science, and Cell.

**Size**: 25,000 image-text pairs

**Format**: N/A

**Annotation**: Curated through live curation mechanisms by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Expected Calibration Error (ECE)
- Negative Log-Likelihood (NLL)
- Root Mean Square Error (RMS)

**Calculation**: Measured based on model predictions against the correct image-text pair associations.

**Interpretation**: Accuracy reflects models' ability to identify correct scientific concepts while ECE measures prediction reliability.

**Validation**: Annual performance assessments to gauge evolving comprehension and reasoning of MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Compliance with open access policies of journal publishers.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
