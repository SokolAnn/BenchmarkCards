# CaseReportBench (An LLM Benchmark Dataset for Dense Information Extraction in Clinical Case Reports)

## 📊 Benchmark Details

**Name**: CaseReportBench (An LLM Benchmark Dataset for Dense Information Extraction in Clinical Case Reports)

**Overview**: CaseReportBench is an expert-annotated dataset for dense information extraction focusing on Inborn Errors of Metabolism (IEM) in clinical case reports, designed to evaluate various models and prompting strategies for extracting clinically relevant details.

**Data Type**: structured medical data

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/cxyzhang/caseReportBench_ClinicalDenseExtraction_Benchmark)
- [GitHub Repository](https://github.com/cindyzhangxy/CaseReportBench)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for evaluating dense information extraction from clinical case reports and to identify effective LLM-based methods for this task.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: De-identified case reports from the non-commercial PMC Open Access Subset.

**Size**: 138 case reports

**Format**: N/A

**Annotation**: Expert-annotated by clinicians following predefined guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Clinical evaluations

**Metrics**:
- Token Set Ratio (TSR)
- Levenshtein Distance
- Exact Match (EM)
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the alignment of LLM-extracted information with expert annotations.

**Interpretation**: Higher scores on the metrics indicate better alignment and extraction accuracy.

**Baseline Results**: N/A

**Validation**: Evaluation included comparisons across five LLMs using different prompting and data integration strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Explainability

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Explainability**: Unexplainable output

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only publicly available, de-identified data were used.

**Data Licensing**: CC BY-NC license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
