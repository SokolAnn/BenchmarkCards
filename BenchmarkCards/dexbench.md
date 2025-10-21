# DexBench

## 📊 Benchmark Details

**Name**: DexBench

**Overview**: DexBench is a benchmark designed to evaluate large language model (LLM) performance across real-world decision-making tasks faced by individuals managing diabetes. It introduces a comprehensive evaluation framework tailored to the challenges of diabetes management, compiling data from 15,000 individuals to generate 360,600 personalized questions across 7 task categories.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- HealthBench
- MedHELM
- MedCalc-Bench
- MedGPTEval

**Resources**:
- [Resource](https://arxiv.org/abs/2510.00038)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate LLMs on patient-facing diabetes management tasks.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI Developers

**Tasks**:
- Decision Making
- Planning
- Education
- Simple Reasoning
- Advanced Reasoning
- Alert/Triage
- Glucose Math

**Limitations**: The curated dataset lacks detailed cohort demographics and relies on wearable and self-logged data, which can be sparse and noisy.

## 💾 Data

**Source**: Data compiled from continuous glucose monitors and behavioral logs from 15,000 individuals across three diabetes populations.

**Size**: 360,600 questions from 15,000 individuals

**Format**: CSV, JSON

**Annotation**: Data collected through self-logging and continuous monitoring.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Groundedness
- Safety
- Clarity
- Actionability

**Calculation**: Metrics are calculated based on model outputs compared to ground truths and predefined criteria for each task.

**Interpretation**: Higher scores reflect better performance in providing accurate, grounded, safe, clear, and actionable responses.

**Baseline Results**: N/A

**Validation**: Cross-validated using human reviewers for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**
- **Societal Impact**

**Demographic Analysis**: Limited demographic data was collected.

**Potential Harm**: Focus on preventing misinformation and ensuring safe usage of AI in healthcare contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used in DexBench was de-identified and obtained with appropriate consent, ensuring compliance with relevant regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: All data collected met ethical standards and received necessary approvals.

**Compliance With Regulations**: The work conforms to HIPAA regulations.
