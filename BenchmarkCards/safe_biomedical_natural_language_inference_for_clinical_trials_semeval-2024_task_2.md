# Safe Biomedical Natural Language Inference for Clinical Trials (SemEval-2024 Task 2)

## 📊 Benchmark Details

**Name**: Safe Biomedical Natural Language Inference for Clinical Trials (SemEval-2024 Task 2)

**Overview**: This paper evaluates the natural language inference capabilities of large language models using clinical trial reports, with a focus on challenging instances involving medical abbreviations and numerical-quantitative reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Multi-Evidence Natural Language Inference for Clinical Trial Data (NLI4CT)

**Resources**:
- [GitHub Repository](https://github.com/DuyguA/SemEval2024_NLI4CT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the clinical inference capabilities of popular large language models using enriched datasets of clinical trial reports.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: ClinicalTrials.gov dataset containing information on clinical studies related to breast cancer.

**Size**: 7,400 statements

**Format**: text

**Annotation**: Labeled as entailment or contradiction based on clinical trial report information.

## 🔬 Methodology

**Methods**:
- Evaluation using macro F1-score
- Semantic evaluations for faithfulness and consistency

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Metrics were calculated based on binary classification results of the models.

**Interpretation**: High F1 scores indicate better inference capability of LLMs in medical trial contexts.

**Validation**: Varying performance evaluations across development and test sets for chosen LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
