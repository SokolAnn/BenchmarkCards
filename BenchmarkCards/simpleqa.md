# SimpleQA

## 📊 Benchmark Details

**Name**: SimpleQA

**Overview**: SimpleQA is a benchmark that evaluates the ability of language models to answer short, fact-seeking questions. It contains 4,326 short, fact-seeking questions that are adversarially collected against GPT-4 responses, with each answer graded as correct, incorrect, or not attempted.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TriviaQA
- Natural Questions

**Resources**:
- [GitHub Repository](https://github.com/openai/simple-evals)

## 🎯 Purpose and Intended Users

**Goal**: To measure the factuality of frontier language models through a targeted evaluation of their ability to answer short, fact-seeking questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: SimpleQA only measures factuality under the constrained setting of short, fact-seeking queries with a single, verifiable answer.

## 💾 Data

**Source**: Data was created by AI trainers who generated question and answer pairs, with answers verified by another AI trainer.

**Size**: 4,326 questions

**Format**: N/A

**Annotation**: Questions were created by AI trainers and answers verified by independent AI trainers.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F-score
- overall correct
- correct given attempted

**Calculation**: The F-score is computed as the harmonic mean of overall correct and correct given attempted.

**Interpretation**: A model that gets many questions correct while attempting those it is confident about would indicate ideal behavior.

**Baseline Results**: Various OpenAI and Anthropic models were evaluated on SimpleQA, with GPT-4 showing different scores based on its configurations.

**Validation**: Performance metrics were manually validated against a set of test answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Hallucinations', 'Inaccurate information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
