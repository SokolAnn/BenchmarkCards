# MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs

## 📊 Benchmark Details

**Name**: MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs

**Overview**: MM-Eval is a specialized dataset for evaluating the capabilities of large language models (LLMs) in modern Mongolian, which is a low-resource language. It categorizes capabilities into language abilities (syntax and semantics) and cognitive abilities (knowledge and reasoning).

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Mongolian

**Resources**:
- [GitHub Repository](https://github.com/joenahm/MM-Eval)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal is to evaluate modern LLMs' capabilities in processing Mongolian, providing insights for future research and development in NLP for low-resource languages.

**Target Audience**:
- NLP Researchers
- LLM Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: MM-Eval is limited by its single content source, only multiple-choice questions, and a narrow scope of logical reasoning tasks.

## 💾 Data

**Source**: Data is sourced from Modern Mongolian Language Textbook I and enriched with WebQSP and MGSM datasets.

**Size**: 2,220 multiple-choice questions

**Format**: JSON

**Annotation**: Manual correction for accuracy and verification of question-answer pairs.

## 🔬 Methodology

**Methods**:
- Evaluation of model performance using accuracy metrics.

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on correct versus incorrect answers from multiple-choice questions.

**Interpretation**: A model's performance is interpreted based on the accuracy percentage in the evaluation tasks.

**Validation**: The dataset and results were validated using manual quality checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
