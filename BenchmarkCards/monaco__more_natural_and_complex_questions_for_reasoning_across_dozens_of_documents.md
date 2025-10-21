# MONACO: More Natural and Complex Questions for Reasoning Across Dozens of Documents

## 📊 Benchmark Details

**Name**: MONACO: More Natural and Complex Questions for Reasoning Across Dozens of Documents

**Overview**: MONACO is a benchmark of 1,315 natural and time-consuming questions that require dozens and at times hundreds of intermediate steps to solve, challenging existing QA benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- DROP
- QAMPARI
- QUEST

**Resources**:
- [Resource](https://tomerwolgithub.github.io/monaco)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM-based systems on information-seeking tasks that are realistic and time-consuming, requiring planning, collecting, and synthesizing many pieces of information.

**Target Audience**:
- ML Researchers
- AI Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced annotations from workers using Wikipedia as the knowledge base.

**Size**: 1,315 questions

**Format**: N/A

**Annotation**: Manual annotation with a decomposed annotation pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics calculated based on the performance of LLMs on the MONACO benchmark.

**Interpretation**: Higher F1 scores indicate better performance in understanding and answering complex, multi-step questions.

**Validation**: Manual validation of all intermediate answers and final answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
