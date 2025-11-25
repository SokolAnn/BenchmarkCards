# Compound-QA

## 📊 Benchmark Details

**Name**: Compound-QA

**Overview**: Compound-QA is a benchmark focusing on evaluating large language models (LLMs) on their ability to answer compound questions that include multiple sub-questions. It consists of 1,500 compound questions created from existing QA datasets, aiming to assess understanding, reasoning, and knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- HotpotQA
- TriviaQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Compound-QA benchmark is to evaluate the capability of LLMs in handling compound questions containing multiple sub-questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is based on existing datasets and is limited to English.

## 💾 Data

**Source**: The dataset is derived from existing QA datasets using a synthesis framework called CQ-Syn, incorporating human verification for quality control.

**Size**: 1,500 examples

**Format**: N/A

**Annotation**: Annotated with proprietary LLMs and verified by humans for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Win rate

**Calculation**: The win rate indicates the proportion of instances where the model’s answers are as good as or better than the reference answers in terms of quality.

**Interpretation**: Higher win rates indicate better performance of the models on compound questions.

**Baseline Results**: Performance of eight open-source LLMs evaluated on compound questions.

**Validation**: Manual verification by graduate-level students to ensure accurate and high-quality data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
