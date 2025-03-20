# Hallucinations Leaderboard

## 📊 Benchmark Details

**Name**: Hallucinations Leaderboard

**Overview**: An open initiative to quantitatively measure and compare the tendency of large language models (LLMs) to produce hallucinations across various tasks such as question-answering, summarisation, and reading comprehension.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Open-domain QA
- Summarisation
- Reading Comprehension

**Languages**:
- English

**Similar Benchmarks**:
- Open LLM Leaderboard
- Hughes Hallucination Evaluation Model

**Resources**:
- [Resource](https://huggingface.co/spaces/hallucinations-leaderboard/leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To guide researchers and practitioners in choosing reliable models by providing insights into the hallucination tendencies of different LLMs.

**Target Audience**:
- Researchers
- Practitioners in NLP

**Tasks**:
- Measure hallucinations in LLMs
- Evaluate factuality and faithfulness of model outputs

**Limitations**: N/A

**Out of Scope Uses**:
- Closed-source models
- Non-NLP applications

## 💾 Data

**Source**: Various datasets for evaluating LLMs including Natural Questions, TriviaQA, XSum, CNN/DM among others.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot in-context learning

**Metrics**:
- Accuracy
- ROUGE-L
- Exact Match

**Calculation**: Metrics are averaged to produce factuality and faithfulness scores.

**Interpretation**: Higher scores indicate better adherence to factuality and faithfulness in the model outputs.

**Baseline Results**: N/A

**Validation**: Evaluation framework based on the EleutherAI Language Model Evaluation Harness.

## ⚠️ Targeted Risks

**Risk Categories**:
- factuality hallucination
- faithfulness hallucination

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinformation from hallucinated outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
