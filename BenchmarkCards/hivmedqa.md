# HIVMedQA

## 📊 Benchmark Details

**Name**: HIVMedQA

**Overview**: HIVMedQA is a benchmark designed for evaluating open-ended medical question answering in the context of HIV patient management, developed with insights from an infectious disease physician.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/records/15868085)
- [GitHub Repository](https://github.com/GonzaloCardenalAl/medical LLM evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of current LLMs in the context of curbside consults for HIV care and provide actionable insights for their future development.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated set of clinically relevant HIV-related questions, validated with an infectious disease physician.

**Size**: N/A

**Format**: N/A

**Annotation**: Expert validation of the questions and gold-standard answers.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge
- Lexical Matching

**Metrics**:
- MedGPT Score
- F1 Score

**Calculation**: Metrics are calculated based on LLM responses compared to gold-standard answers.

**Interpretation**: Higher MedGPT scores indicate better performance in comprehension, reasoning, and medical knowledge recall.

**Baseline Results**: N/A

**Validation**: Validation of model performance through repeated evaluations across multiple question categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
