# FACTCHD (Fact-Conflicting Hallucination Detection)

## 📊 Benchmark Details

**Name**: FACTCHD (Fact-Conflicting Hallucination Detection)

**Overview**: FACTCHD is a dedicated benchmark designed for the detection of fact-conflicting hallucinations from LLMs, featuring a diverse dataset that spans various factuality patterns and integrates fact-based evidence chains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zjunlp/FactCHD)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the detection of fact-conflicting hallucinations in LLMs and improve their factuality assessments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact-Conflicting Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: Generated using knowledge graphs and human annotation.

**Size**: 51,383 training examples; 6,960 testing examples

**Format**: N/A

**Annotation**: Annotated with hallucination presence by human annotators.

## 🔬 Methodology

**Methods**:
- Evaluation on various LLM models such as Alpaca, Llama2-chat, and ChatGPT.

**Metrics**:
- Micro F1 Score
- EXPMATCH

**Calculation**: Micro F1 Score is used for factuality classification performance and EXPMATCH measures the quality of explanations.

**Interpretation**: Higher scores indicate better performance in detecting factuality and providing explanations.

**Baseline Results**: N/A

**Validation**: Evaluated through extensive testing on multiple language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
