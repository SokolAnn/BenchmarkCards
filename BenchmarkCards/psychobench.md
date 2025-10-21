# PsychoBench

## 📊 Benchmark Details

**Name**: PsychoBench

**Overview**: PsychoBench is a benchmark designed to evaluate LLMs' capability to perform psychological counseling tasks. It comprises approximately 2,252 single-choice questions crafted to evaluate the knowledge required for passing the US National Counselor Certification Exam.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cloversjtu/PsychoBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the competency of large language models in psychological counseling tasks.

**Target Audience**:
- AI Researchers
- Mental Health Professionals
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark is limited to English and U.S.-specific licensure standards, which may restrict generalizability across cultural and linguistic contexts.

## 💾 Data

**Source**: Publicly available psychological counseling certification exam questions on the internet.

**Size**: 2,252 questions

**Format**: N/A

**Annotation**: Questions were paraphrased and refined using GPT-based methods and reviewed by human experts.

## 🔬 Methodology

**Methods**:
- Evaluation of model performance using classification metrics

**Metrics**:
- Top-1 Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on the proportion of correctly predicted items over the total number of questions.

**Interpretation**: Scores indicating model performance where higher accuracy suggests better competence in psychological counseling knowledge.

**Baseline Results**: GPT-4o achieved the highest Top-1 accuracy of 94.36%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset contains no personal or sensitive information.

**Data Licensing**: CC-BY-NC-ND

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
