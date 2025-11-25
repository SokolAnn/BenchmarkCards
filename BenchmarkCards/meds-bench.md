# MedS-Bench

## 📊 Benchmark Details

**Name**: MedS-Bench

**Overview**: MedS-Bench is a comprehensive benchmark designed to evaluate the performance of large language models (LLMs) in clinical contexts, including 11 high-level clinical tasks such as clinical report summarization, treatment recommendations, diagnosis, named entity recognition, and medical concept explanation.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://henrychur.github.io/MedS-Bench/)
- [GitHub Repository](https://github.com/MAGIC-AI4Med/MedS-Ins)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the capabilities of LLMs in clinical tasks and to encourage further advancements in the application of LLMs to clinical challenges.

**Target Audience**:
- Researchers
- Clinicians

**Tasks**:
- Clinical Report Summarization
- Treatment Recommendations
- Diagnosis
- Named Entity Recognition
- Medical Concept Explanation
- Information Extraction
- Multi-choice Question Answering
- Text Classification
- Natural Language Inference

**Limitations**: MedS-Bench currently covers only 11 clinical tasks, which does not fully encompass the complexity of all clinical scenarios.

## 💾 Data

**Source**: Collected from various medical datasets, including existing biomedical natural language processing datasets and clinical texts.

**Size**: 5M instances

**Format**: JSON

**Annotation**: Manually written task definitions and examples for each task.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the evaluations of LLMs on the specified clinical tasks.

**Interpretation**: Higher scores indicate better performance on clinical tasks.

**Baseline Results**: Results from LLMs including GPT-4, Claude-3.5, Mistral, and others evaluated against MedS-Bench.

**Validation**: The benchmark was validated through comparisons with existing models and clinical task performance assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
