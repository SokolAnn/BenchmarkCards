# COMPARE

## 📊 Benchmark Details

**Name**: COMPARE

**Overview**: COMPARE is a taxonomy and a dataset of comparison discussions in peer reviews of research papers in the domain of experimental deep learning. It consists of 1,800 annotated sentences with labels for comparison and non-comparison, categorized into four aspects and thirteen subcategories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shruti-singh/COMPARE)

## 🎯 Purpose and Intended Users

**Goal**: To study meaningful comparison discussions in peer reviews and to enable automatic extraction of comparative statements from peer review texts.

**Target Audience**:
- Researchers
- Reviewers
- Machine Learning Practitioners

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Peer review texts publicly available on the OpenReview platform from papers submitted to ICLR between 2017–2020.

**Size**: 1,800 sentences

**Format**: N/A

**Annotation**: Manual classification of sentences as comparison or non-comparison with four broad categories and associated subcategories.

## 🔬 Methodology

**Methods**:
- Machine Learning classifiers
- Manual annotation

**Metrics**:
- F1 Score

**Calculation**: F1 Score is calculated based on the classification results of comparison vs. non-comparison sentences.

**Interpretation**: An F1 Score closer to 1 indicates better performance in classifying meaningful comparison discussions.

**Validation**: Evaluation through experiments with various machine learning models and fine-tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
