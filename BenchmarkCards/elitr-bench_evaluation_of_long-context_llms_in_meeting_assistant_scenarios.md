# ELITR-Bench (Evaluation of Long-context LLMs in Meeting Assistant Scenarios)

## 📊 Benchmark Details

**Name**: ELITR-Bench (Evaluation of Long-context LLMs in Meeting Assistant Scenarios)

**Overview**: ELITR-Bench is a benchmark designed to evaluate long-context language models in real-world meeting assistant scenarios, incorporating transcripts obtained by automatic speech recognition and assessing the models' robustness to various noise levels.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Long Range Arena
- L-Eval
- LongEval
- LongBench
- MeeQA
- MeetingQA

**Resources**:
- [GitHub Repository](https://github.com/utter-project/ELITR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark that evaluates the performance of long-context LLMs in scenarios relevant to meeting assistants, challenging LLMs with real-world noise and context-based questioning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Meeting transcripts from the ELITR project supplemented with manually crafted questions and ground-truth answers.

**Size**: 10 meetings in dev set, 8 meetings in test set

**Format**: JSON

**Annotation**: Questions and answers are manually created and validated.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Human evaluation
- Crowdsourcing study

**Metrics**:
- Average score
- Correlation with human judges

**Calculation**: Scores are calculated based on the closeness of model predictions to the ground-truth answers.

**Interpretation**: Scores reflect the model's ability to accurately respond to questions based on the provided meeting transcripts.

**Baseline Results**: GPT-4 and GPT-4o achieved average scores above 8 on ELITR-Bench.

**Validation**: Validation of the evaluation method was performed through comparison with human judges.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection complied with ethical regulations and guidelines including anonymization of personally identifiable information.

**Data Licensing**: The data is made publicly available under appropriate licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
