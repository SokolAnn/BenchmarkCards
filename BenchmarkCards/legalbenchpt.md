# LegalBench.PT

## 📊 Benchmark Details

**Name**: LegalBench.PT

**Overview**: LegalBench.PT is the first comprehensive legal benchmark covering key areas of Portuguese law. It measures LLMs’ legal knowledge and practical application through a dataset generated from real law exams, converted into various question formats to assess legal reasoning.

**Data Type**: multiple-choice questions, true/false questions, matching questions

**Domains**:
- Legal

**Languages**:
- Portuguese

**Similar Benchmarks**:
- LegalBench

**Resources**:
- [Resource](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT)
- [Resource](https://arxiv.org/abs/2502.16357)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' legal knowledge and application specific to the Portuguese legal system.

**Target Audience**:
- Legal Researchers
- Lawyers
- Machine Learning Researchers

**Tasks**:
- Legal Knowledge Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Long-form questions and answers collected from real law exams at a leading law school in Portugal.

**Size**: 4,723 questions

**Format**: JSON

**Annotation**: Synthetic questions generated and filtered using GPT-4o, reviewed by legal professionals.

## 🔬 Methodology

**Methods**:
- Question Generation
- Human Evaluation
- Automated Metrics

**Metrics**:
- Accuracy
- F1 Score
- Balanced Accuracy

**Calculation**: Metrics were calculated based on model responses to the benchmark questions.

**Interpretation**: High scores indicate better legal knowledge and reasoning capabilities.

**Validation**: Validated through human review by legal professionals.

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

**Privacy And Anonymity**: Data collected from real law exams with anonymized information of exam participants.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
