# UnsafeBench

## 📊 Benchmark Details

**Name**: UnsafeBench

**Overview**: UnsafeBench is a benchmarking framework that evaluates the effectiveness and robustness of image safety classifiers on real-world and AI-generated images. It consists of a dataset of 10K annotated images across 11 unsafe categories to support the evaluation of various classifiers.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://unsafebench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for image safety classifiers, focusing on their effectiveness and robustness against real-world and AI-generated unsafe images.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification

**Limitations**: The dataset may contain challenges as all images are queried using a common set of unsafe keywords, making them difficult to classify for image safety classifiers.

## 💾 Data

**Source**: UnsafeBench dataset consists of 10K images curated from large databases including LAION-5B and Lexica, annotated for safety and categorization.

**Size**: 10,000 images

**Format**: N/A

**Annotation**: Annotated by three authors of the paper.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 Score is used to evaluate the effectiveness of image safety classifiers, measuring precision and recall across 11 unsafe categories.

**Interpretation**: An F1 Score closer to 1 indicates better classifier performance, while lower scores suggest poorer effectiveness.

**Baseline Results**: Baseline F1 Scores vary among classifiers; GPT-4V achieves high scores in multiple categories.

**Validation**: The UnsafeBench dataset has been validated through human annotation and computing agreement statistics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures include restricting exposure of annotators to harmful images, with an ethical review approved by an institution's Ethics Review Board.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotations were manually performed by authors, avoiding exposure of distressing content to external annotators.

**Compliance With Regulations**: Not Applicable
