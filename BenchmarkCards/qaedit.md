# QAEdit

## 📊 Benchmark Details

**Name**: QAEdit

**Overview**: QAEdit is a benchmark tailored for real-world QA tasks, designed to assess model editing in large language models (LLMs) and to expose limitations in synthetic evaluation practices.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ZsRE
- COUNTER FACT

**Resources**:
- [GitHub Repository](https://github.com/WanliYoung/Revisit-Editing-Evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously assess model editing methods in real-world question answering scenarios and to expose pitfalls of synthetic evaluation methods.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from three widely-used QA datasets: Natural Questions, TriviaQA, and SimpleQA.

**Size**: 19,249 samples

**Format**: N/A

**Annotation**: Extracted subjects from the questions using GPT-4, paraphrased prompts, and selected unrelated QA pairs for locality evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Calculated based on the success rate of edited LLMs on previously failed questions in QA tasks.

**Interpretation**: Higher accuracy indicates better performance of the editing methods in real-world QA settings.

**Baseline Results**: Average accuracy of existing editing methods was found to be significantly lower than previously reported results under synthetic evaluations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used in the research is publicly available and does not raise any privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
