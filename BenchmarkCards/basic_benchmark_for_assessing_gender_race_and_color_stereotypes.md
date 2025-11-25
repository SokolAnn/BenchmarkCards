# BASIC (Benchmark for Assessing Gender, Race, and Color Stereotypes)

## 📊 Benchmark Details

**Name**: BASIC (Benchmark for Assessing Gender, Race, and Color Stereotypes)

**Overview**: BASIC is a benchmark for assessing gender, race, and color stereotypes in large vision language models (LVLMs), designed to evaluate the impact of these attributes on the models' outputs.

**Data Type**: image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate stereotypes in large vision language models using the Stereotype Content Model.

**Target Audience**:
- AI Researchers
- Machine Learning Practitioners

**Tasks**:
- Bias Detection
- Stereotype Analysis

**Limitations**: While our study presents SCM-based evaluation metrics and introduces BASIC, three limitations remain. First, our findings may not be fully independent from other visual attributes. Second, our findings suggest correlations between architectural differences and stereotype presence without proving causation. Third, we conducted our experiment only in English.

## 💾 Data

**Source**: Generated images simulating various occupations with controlled color and demographic attributes.

**Size**: 18,360 images

**Format**: JPEG

**Annotation**: Automatically generated with human oversight to ensure quality.

## 🔬 Methodology

**Methods**:
- Statistical tests
- Pointwise mutual information (PMI) analysis

**Metrics**:
- Competence
- Warmth

**Calculation**: Metrics are calculated based on word embeddings projected onto the axes of competence and warmth.

**Interpretation**: Higher scores signify stronger associations with positive traits; lower scores indicate stereotype associations.

**Validation**: Systematic comparison of eight large vision language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis conducted across various gender, race, and color attributes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
