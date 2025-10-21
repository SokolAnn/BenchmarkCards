# WebSight

## 📊 Benchmark Details

**Name**: WebSight

**Overview**: WebSight is a synthetic dataset consisting of 2 million pairs of HTML codes and their corresponding screenshots, aimed at facilitating the conversion of webpage screenshots to functional HTML code using vision-language models.

**Data Type**: HTML code and screenshot pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Design2Code

**Resources**:
- [Resource](https://huggingface.co/datasets/HuggingFaceM4/WebSight)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, high-quality dataset for fine-tuning vision-language models to automate the conversion of webpage screenshots into HTML code.

**Target Audience**:
- ML Researchers
- Web Developers
- AI Practitioners

**Tasks**:
- Image to Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation using LLMs and web rendering

**Size**: 2,000,000 pairs

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Fine-tuning VLMs on the generated dataset
- Image rendering and code generation

**Metrics**:
- Accuracy

**Calculation**: Validation loss is monitored but is not a good indicator of quality; manual inspection is used.

**Interpretation**: Lower validation loss does not necessarily correlate with better generalization.

**Baseline Results**: N/A

**Validation**: Manual inspection of generated samples

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Incomplete or incorrect HTML output']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
