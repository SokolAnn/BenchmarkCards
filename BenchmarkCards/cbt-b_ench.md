# CBT-B ENCH

## 📊 Benchmark Details

**Name**: CBT-B ENCH

**Overview**: CBT-B ENCH is a systematic benchmark for evaluating the assistance of large language models (LLMs) in Cognitive Behavioral Therapy (CBT) across three levels: basic knowledge acquisition, cognitive model understanding, and therapeutic response generation.

**Data Type**: multiple-choice questions, classification examples, response generation tasks

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mianzhang/CBT-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To thoroughly investigate the proficiency and potential of LLMs in supporting various facets and stages of professional mental health care in CBT.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Multiple-Choice Question Answering
- Cognitive Distortion Classification
- Core Belief Classification
- Therapeutic Response Generation

**Limitations**: The size of datasets is limited by the cost of annotating in specialized fields like mental health.

## 💾 Data

**Source**: CBT exam questions for Master of Social Work (MSW) students and compositions by CBT experts.

**Size**: 220 multiple-choice questions, 146 cognitive distortion examples, 184 primary core belief examples, 112 fine-grained core belief examples, 156 therapeutic response exercises

**Format**: JSON, CSV

**Annotation**: Annotated by CBT experts, with rigorous verification for quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy for multiple-choice questions and weighted precision, recall, F1 score for classification datasets.

**Interpretation**: Performance is compared against human expert scores to evaluate LLMs' capabilities.

**Baseline Results**: Human baseline accuracy for CBT-QA is 90.7%. LLM performance varies significantly across tasks.

**Validation**: Validation involved cross-verification and expert evaluations of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from experts was de-identified and consented for research purposes.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all participants involved in data annotation.

**Compliance With Regulations**: This project was approved by the Institutional Review Board (IRB).
