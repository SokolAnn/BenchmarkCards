# Mind the Gap: Benchmarking LLM Uncertainty, Discrimination, and Calibration in Specialty-Aware Clinical QA

## 📊 Benchmark Details

**Name**: Mind the Gap: Benchmarking LLM Uncertainty, Discrimination, and Calibration in Specialty-Aware Clinical QA

**Overview**: This paper evaluates uncertainty estimation methods for clinical question answering focusing on eleven clinical specialties and six question types across ten open-source LLMs. It benchmarks uncertainty across multiple models and introduces a new annotation scheme mapping QA pairs onto different question types.

**Data Type**: multiple-choice question answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- S-MedQA
- MedExQA

**Resources**:
- [Resource](https://huggingface.co/ContactDoctor/Bio-Medical-Llama-3-8B)
- [Resource](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark uncertainty quantification methods in clinical question answering using large language models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Two English multiple-choice question answering datasets: S-MedQA and MedExQA.

**Size**: 1,810 questions

**Format**: N/A

**Annotation**: Manually gathered and annotated with a validated pipeline mapping to clinical specialties.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- AUROC
- Expected Calibration Error (ECE)
- Brier Score

**Calculation**: Metrics computed based on model outputs comparing predictions to ground-truth labels.

**Interpretation**: Higher AUROC indicates better discrimination; lower ECE indicates better calibration.

**Baseline Results**: N/A

**Validation**: Model outputs validated against human annotations.

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
