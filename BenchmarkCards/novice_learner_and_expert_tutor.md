# Novice Learner and Expert Tutor

## 📊 Benchmark Details

**Name**: Novice Learner and Expert Tutor

**Overview**: We propose novel evaluations for mathematical reasoning capabilities of Large Language Models (LLMs) based on mathematical misconceptions, simulating a novice learner and an expert tutor.

**Data Type**: multiple-choice grade-school math questions

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- NumGLUE

**Resources**:
- [Resource](https://eedi.com/home)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the mathematical reasoning capabilities of LLMs based on math misconceptions.

**Target Audience**:
- Educational Researchers
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Eedi’s platform dataset of multiple-choice grade-school math questions.

**Size**: 213 questions

**Format**: N/A

**Annotation**: Expert-curated student misconceptions corresponding to the incorrect choices.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Prompting strategies

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed based on the number of correct identifications of misconceptions or mistakes.

**Interpretation**: Higher accuracy indicates better performance in simulating novice learners and expert tutors.

**Baseline Results**: GPT-4 achieved a near-perfect accuracy of 94.8% in answering math questions correctly.

**Validation**: Statistical significance was ensured by reporting results based on mean and standard deviation from independent trials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
