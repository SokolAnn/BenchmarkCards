# CLIMB (A Benchmark of Clinical Bias in Large Language Models)

## 📊 Benchmark Details

**Name**: CLIMB (A Benchmark of Clinical Bias in Large Language Models)

**Overview**: CLIMB is a pioneering benchmark to evaluate both intrinsic and extrinsic bias in large language models (LLMs) for clinical decision tasks, introducing a novel metric, AssocMAD, to assess disparities across multiple demographic groups.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uscnlp-lime/climb)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate clinical bias in LLMs.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Clinical Diagnosis Prediction
- Bias Evaluation

**Limitations**: The initial version focuses on diagnosis tasks; further adaptations to other clinical tasks are needed.

## 💾 Data

**Source**: Evaluation from clinical decision tasks using ICD-10-CM codes and demographic attributes.

**Size**: 199 instances

**Format**: N/A

**Annotation**: Real-world clinical data grounded in Electronic Health Records (EHR).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Counterfactual intervention

**Metrics**:
- AssocMAD
- Recall

**Calculation**: AssocMAD is calculated using the average absolute distance of association scores between demographic groups.

**Interpretation**: Lower AssocMAD values indicate less bias, while recall measures performance differences based on demographic information.

**Validation**: Evaluation through experiments across models from the Mistral and LLaMA families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark assesses bias across different demographic groups, including sex and ethnicity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The evaluation is grounded in de-identified Electronic Health Records (EHR).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
