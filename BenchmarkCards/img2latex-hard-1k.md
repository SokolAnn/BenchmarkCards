# Img2LaTex-Hard-1K

## 📊 Benchmark Details

**Name**: Img2LaTex-Hard-1K

**Overview**: Img2LaTex-Hard-1K is a dataset consisting of 1,100 carefully curated and challenging examples designed to rigorously evaluate the capabilities of vision-language models (VLMs) in translating mathematical expressions and structured visual content from images into LaTeX code.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous benchmark for assessing the performance of vision-language models in the Img2LaTeX task.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image to LaTeX Conversion

**Limitations**: N/A

## 💾 Data

**Source**: Curated subset from the Im2LaTeX-100K dataset.

**Size**: 1,100 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- m-ROUGE
- BLEU-4
- Edit Distance

**Calculation**: Metrics are calculated using textual similarity metrics (m-ROUGE, BLEU-4, Edit Distance) for evaluating LaTeX generation.

**Interpretation**: Higher scores indicate better similarity and correctness of the generated LaTeX code compared to ground truth.

**Validation**: Performance validated through extensive experimental results and comparisons with baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
