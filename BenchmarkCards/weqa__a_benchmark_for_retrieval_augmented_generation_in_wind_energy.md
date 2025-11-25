# WeQA: A Benchmark for Retrieval Augmented Generation in Wind Energy

## 📊 Benchmark Details

**Name**: WeQA: A Benchmark for Retrieval Augmented Generation in Wind Energy

**Overview**: WeQA is the first comprehensive benchmark QA dataset specifically designed for the wind energy domain, addressing the gap in specialized evaluation datasets for wind energy project permitting. It allows for rigorous assessment of RAG-based LLMs using diverse metrics and multiple question types with varying complexity levels.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Environmental Science

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- MMLU
- EnviroExam
- NEPAQuAD

**Resources**:
- [Resource](https://arxiv.org/abs/2408.11800)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of WeQA is to provide a structured benchmark for evaluating RAG-based LLMs in the context of wind energy project permitting, facilitating the assessment of diverse LLM performance across complex real-world scenarios.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Questions generated can be too specific to the documents they were derived from, potentially complicating accurate responses from LLMs.

## 💾 Data

**Source**: Wind energy-related documents, including research articles and environmental impact studies published by the Department of Energy (DOE) under the National Environmental Policy Act (NEPA).

**Size**: 5,000 question-answer pairs

**Format**: JSON

**Annotation**: Manual curation and validation by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Answer correctness
- Context precision
- Context recall

**Calculation**: Metrics are calculated based on the evaluations of answers by judge LLMs and ground truth validation.

**Interpretation**: Higher scores indicate better LLM performance in retrieving relevant information and generating accurate responses.

**Baseline Results**: Evaluations conducted using GPT-4 and Gemini-1.5Pro as judge models.

**Validation**: Use of RAGAS evaluation framework for systematic assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
