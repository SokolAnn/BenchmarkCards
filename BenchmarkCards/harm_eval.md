# HARM EVAL

## 📊 Benchmark Details

**Name**: HARM EVAL

**Overview**: HARM EVAL is a novel benchmark for comprehensive safety evaluations, designed to address potential misuse scenarios in line with the policies of leading AI technology companies.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NeuralSentinel/SafeInfer)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety and ethical compliance of language models by assessing their responses to harmful queries.

**Target Audience**:
- AI Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from policy violations identified by Meta and OpenAI.

**Size**: 550 questions

**Format**: JSON

**Annotation**: Manually crafted and verified by experts using GPT-4 for ethical implications.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated as the percentage of responses not aligned with safety.

**Interpretation**: Lower ASR values indicate better safety alignment.

**Validation**: Validated using multiple prompting techniques and against various baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized and sensitive information is not included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
