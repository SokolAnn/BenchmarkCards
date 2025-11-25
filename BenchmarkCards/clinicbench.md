# ClinicBench

## 📊 Benchmark Details

**Name**: ClinicBench

**Overview**: ClinicBench is a comprehensive benchmark that assesses large language models (LLMs) in clinical settings. It includes eleven tasks across three scenarios—reasoning, generation, and understanding—with a total of seventeen datasets, including six novel datasets tailored for complex clinical tasks.

**Data Type**: question-answering pairs, document summaries, clinical entity recognition, and treatment recommendations

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA
- MMLU
- PubMedQA
- MIMIC-III
- MIMIC-CXR

**Resources**:
- [GitHub Repository](https://github.com/AI-in-Health/ClinicBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of large language models in clinical tasks and assist in understanding their capabilities and limitations in healthcare applications.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Summarization
- Named Entity Recognition
- Document Classification
- Treatment Recommendation
- Pharmacology Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Combination of existing clinical datasets and newly constructed datasets pertinent to clinical language and reasoning tasks.

**Size**: Over 20,000 test samples across various tasks

**Format**: N/A

**Annotation**: Datasets were collected from existing medical data sources and newly generated through expert curation and review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L

**Calculation**: Performance is evaluated on the basis of both automated scoring systems and qualitative human assessments.

**Interpretation**: Performance is interpreted through the success rates of correct predictions and qualitative evaluations based on clinical relevancy and comprehensiveness.

**Baseline Results**: Competing models such as GPT-4 and other leading LLMs were benchmarked against the proposed tasks.

**Validation**: Cross-validation techniques and expert evaluation in clinical settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Emphasizes the need for secure data handling practices and compliance with HIPAA regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adherence to regulations such as HIPAA is highlighted in the context of clinical application.
