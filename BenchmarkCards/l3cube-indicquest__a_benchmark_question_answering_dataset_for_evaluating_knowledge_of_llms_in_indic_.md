# L3Cube-IndicQuest: A Benchmark Question Answering Dataset for Evaluating Knowledge of LLMs in Indic Context

## 📊 Benchmark Details

**Name**: L3Cube-IndicQuest: A Benchmark Question Answering Dataset for Evaluating Knowledge of LLMs in Indic Context

**Overview**: L3Cube-IndicQuest is a gold-standard factual question-answering benchmark dataset designed to evaluate how well multilingual LLMs capture regional knowledge across various Indic languages. The dataset contains 4000 question-answer pairs, each for English and 19 Indic languages, covering five domains specific to the Indic region.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Assamese
- Bengali
- Dogri
- Gujarati
- Hindi
- Kannada
- Konkani
- Maithili
- Malayalam
- Marathi
- Meitei (Manipuri)
- Nepali
- Odia
- Punjabi
- Sanskrit
- Sindhi
- Tamil
- Telugu
- Urdu

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/indic-nlp)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the performance of LLMs in understanding and representing knowledge relevant to the Indian context.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises factual question-and-answer pairs sourced from reputable platforms like Wikipedia and well-known educational websites.

**Size**: 4,000 question-answer pairs

**Format**: N/A

**Annotation**: Manual verification and translation processes were conducted to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Automated evaluation with Llama-3.1-405B-Instruct
- F1 Score
- ROUGE Score

**Metrics**:
- F1 Score
- ROUGE Score
- Overall Evaluation Score

**Calculation**: Metrics are calculated based on alignment between model-generated responses and ground truth answers.

**Interpretation**: Scores are interpreted based on factual accuracy, relevance, clarity, language consistency, and conciseness.

**Baseline Results**: N/A

**Validation**: Evaluation covered various multilingual models including GPT-4o, Llama-3.1-405B-Instruct, Gemma-2-2B-it, and Gemma-2-9B-it.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
