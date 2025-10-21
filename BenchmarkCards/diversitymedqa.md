# DiversityMedQA

## 📊 Benchmark Details

**Name**: DiversityMedQA

**Overview**: DiversityMedQA is a novel benchmark designed to assess LLM responses to medical queries across diverse patient demographics, such as gender and ethnicity, by perturbing questions from the MedQA dataset.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA

**Resources**:
- [Resource](https://huggingface.co/datasets/Rajat1212/DiversityMedQA)

## 🎯 Purpose and Intended Users

**Goal**: To measure bias in large language models used for medical diagnoses by assessing their performance across different demographics.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Medical Diagnosis

**Limitations**: Due to the scope of the MedQA dataset, only a subset of questions was fully prompted for gender and ethnicity perturbation, which might limit the generalizability of findings.

## 💾 Data

**Source**: MedQA dataset, modified through demographic perturbations.

**Size**: 1,108 questions (540 for gender and 568 for ethnicity)

**Format**: JSON

**Annotation**: Automated annotation and filtering were performed to remove questions clinically dependent on demographics.

## 🔬 Methodology

**Methods**:
- LLM prompting
- Z-tests for bias assessment

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the proportion of correct responses from the models across original and perturbed datasets.

**Interpretation**: Higher accuracy indicates better understanding and less bias in LLM responses across demographic variations.

**Baseline Results**: Models tested include GPT-3.5, GPT-4, GPT-4o, Gemini 1.5 Flash, and Llama3-8B, with varying accuracies reported.

**Validation**: Model responses were validated through systematic bias testing using statistical significance assessments (Z-tests).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: The performance was analyzed across different demographics, specifically focusing on gender and ethnicity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
