# EVALUATING LARGE LANGUAGE MODELS ON THE GMAT

## 📊 Benchmark Details

**Name**: EVALUATING LARGE LANGUAGE MODELS ON THE GMAT

**Overview**: This study introduces the first benchmark to assess the performance of seven major LLMs on the GMAT, which is a key exam in the admission process for graduate business programs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2401.02985)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the efficacy of LLMs on the Graduate Management Admission Test (GMAT) and examine their capabilities and limitations in educational environments.

**Target Audience**:
- Educational Researchers
- Business Educators
- AI Researchers

**Tasks**:
- Question Answering

**Limitations**: The scope of the study is limited to multiple-choice questions from the quantitative reasoning and verbal reasoning sections of the GMAT.

## 💾 Data

**Source**: Official GMAT practice exams sourced from the Graduate Management Admission Council (GMAC).

**Size**: 3 GMAT practice exams

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot prompting

**Metrics**:
- Accuracy

**Calculation**: The overall average accuracy is calculated by dividing the number of correct answers by the total number of questions across all three exam sets for each model.

**Interpretation**: Higher accuracy scores indicate better performance on the exam.

**Baseline Results**: GPT-4 Turbo achieved an average accuracy of 85.07%.

**Validation**: The models were tested on both free and premium GMAT exams to ensure comprehensive evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Privacy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Potentially providing incorrect or misleading information that could affect learning.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
