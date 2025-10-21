# InsightVision: A Comprehensive, Multi-Level Chinese-based Benchmark for Evaluating Implicit Visual Semantics in Large Vision Language Models

## 📊 Benchmark Details

**Name**: InsightVision: A Comprehensive, Multi-Level Chinese-based Benchmark for Evaluating Implicit Visual Semantics in Large Vision Language Models

**Overview**: We introduce InsightVision, a comprehensive Chinese-based benchmark designed for nuanced, multi-level image evaluation. It systematically evaluates surface-level content understanding, background knowledge comprehension, symbolic meaning interpretation, and implicit meaning comprehension.

**Data Type**: image-question answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://www.cartoonmovement.com/search?query=&sort=created&order=desc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the understanding of implicit visual semantics in large vision language models and bridge the gaps in existing research.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Surface-level Content Understanding
- Symbolic Meaning Interpretation
- Background Knowledge Comprehension
- Implicit Meaning Comprehension

**Limitations**: The dataset currently focuses on comic images, which may limit generalizability due to a lack of visual diversity.

## 💾 Data

**Source**: Constructed from approximately 100,000 images from Cartoon Movement, with human annotation for quality control.

**Size**: 2,500 images

**Format**: N/A

**Annotation**: Combination of model pre-annotation and human verification

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the ratio of the number of correct answers to the total number of questions.

**Interpretation**: A model’s answer is correct if it matches the ground truth.

**Baseline Results**: Human performance averages: Surface-level Content Understanding: 98.0%, Symbolic Meaning Interpretation: 88.0%, Background Knowledge Comprehension: 86.0%, Implicit Meaning Comprehension: 74.0%.

**Validation**: The benchmark was validated using 15 different large vision language models and human performance comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-sourced with hyperlinks provided for each comic image, ensuring compliance with copyright.

**Consent Procedures**: All annotators voluntarily participated and were compensated.

**Compliance With Regulations**: Not Applicable
