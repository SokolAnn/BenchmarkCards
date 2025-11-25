# K-Viscuit (Korean Visual and Cultural Interpretation Test)

## 📊 Benchmark Details

**Name**: K-Viscuit (Korean Visual and Cultural Interpretation Test)

**Overview**: K-Viscuit is a benchmark dataset tailored to Korean culture, developed using a semi-automated framework that combines human-VLM collaboration. It focuses on evaluating vision-language models’ cultural understanding through visually grounded multiple-choice questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Korean

**Similar Benchmarks**:
- CVQA

**Resources**:
- [Resource](https://huggingface.co/datasets/ddehun/k-viscuit)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of K-Viscuit is to evaluate the cultural understanding capabilities of vision-language models within the context of Korean culture.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Web images and human annotations, using Wikimedia Commons as the primary source.

**Size**: 657 examples

**Format**: JSON

**Annotation**: Annotations were generated through a semi-automated framework combining VLM-generated questions and human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated based on the percentage of correct answers selected by the models from provided options.

**Interpretation**: Higher accuracy indicates better cultural understanding and recognition of visual cues associated with Korean culture.

**Validation**: Validation was performed through a combination of human verification and empirical evaluation against existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Images sourced under Creative Commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
