# BEnQA (Bengali and English Question Answering Benchmark)

## 📊 Benchmark Details

**Name**: BEnQA (Bengali and English Question Answering Benchmark)

**Overview**: BEnQA is a dataset comprising parallel Bengali and English exam questions for middle and high school levels in Bangladesh. The dataset consists of approximately 5,161 questions covering several subjects in science with different types of questions, including factual, application, and reasoning questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali
- English

**Resources**:
- [GitHub Repository](https://github.com/sheikhshafayat/BEnQA)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the performance of existing Large Language Models (LLMs) on a dataset that includes parallel question-answering in Bengali and English.

**Target Audience**:
- ML Researchers
- Educators
- Language Model Developers

**Tasks**:
- Question Answering

**Limitations**: Our dataset primarily focused on text-based questions, excluding figure-based questions.

## 💾 Data

**Source**: Collected from nationwide board exams in Bangladesh.

**Size**: 5,161 questions

**Format**: CSV

**Annotation**: Manually curated and reviewed by proficient typists in both Bengali and English.

## 🔬 Methodology

**Methods**:
- Manual evaluation

**Metrics**:
- Accuracy

**Calculation**: The final answer aligns with the ground truth without scrutinizing the validity of intermediate reasoning steps.

**Interpretation**: An answer is considered correct if it matches the ground truth.

**Validation**: Utilized zero-shot and few-shot prompting techniques to evaluate existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Includes demographic breakdowns based on questions and subjects.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset consists of exam questions that are freely available and manually curated to minimize harmful content.

**Data Licensing**: Distributed under the CC BY-SA 4.0 license.

**Consent Procedures**: Involvement of annotators was compensated above the minimum wage.

**Compliance With Regulations**: The work received approval from the Institutional Review Board (IRB) at the institution.
