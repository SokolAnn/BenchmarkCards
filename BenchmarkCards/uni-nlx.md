# Uni-NLX

## 📊 Benchmark Details

**Name**: Uni-NLX

**Overview**: Uni-NLX is a unified framework that consolidates all Natural Language Explanations (NLE) tasks into a single and compact multi-task model using a unified training objective of text generation. It introduces two new NLE datasets: ImageNetX for explaining ImageNet categories and VQA-ParaX for explaining the Visual Question Answering task.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- NLX-GPT

**Resources**:
- [GitHub Repository](https://github.com/fawazsammani/uni-nlx)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified model that performs multiple NLE tasks simultaneously and reduces the need for separate models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Visual Recognition
- Visual Reasoning

**Limitations**: The model may exhibit shortcut learning in certain tasks, leading to explanations that repeat elements of the questions.

## 💾 Data

**Source**: Datasets created using Large Language Models and existing NLE sample collections.

**Size**: 1,000,000 samples

**Format**: JSON

**Annotation**: Automatically generated using prompts for LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU Score
- METEOR
- ROUGE-L
- CIDER
- SPICE

**Calculation**: Metrics are calculated based on the generated outputs when evaluated against a set of reference answers.

**Interpretation**: Higher scores indicate better generation quality compared to benchmarks.

**Baseline Results**: Performance compared to existing models like NLX-GPT.

**Validation**: Evaluated using both filtered and unfiltered scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
