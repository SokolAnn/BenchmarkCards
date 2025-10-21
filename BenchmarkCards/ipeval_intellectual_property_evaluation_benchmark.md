# IPEval (Intellectual Property Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: IPEval (Intellectual Property Evaluation Benchmark)

**Overview**: IPEval is the first bilingual capability evaluation benchmark designed for assessing the understanding, application, and reasoning abilities of Large Language Models (LLMs) in the field of intellectual property (IP) agency and consulting tasks. It consists of 2657 multiple-choice questions divided into four major capability dimensions: creation, application, protection, and management.

**Data Type**: multiple-choice questions

**Domains**:
- Legal

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MedQA
- LawBench
- E-EVAL
- HUPD
- MoZIP

**Resources**:
- [Resource](https://ipeval.github.io/)
- [GitHub Repository](https://github.com/Mathsion2/IPEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide an accurate assessment of LLM capabilities in the IP domain and encourage researchers to develop LLMs with richer IP knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Annual Chinese patent bar exams from 2012 to 2019 and biannual US patent bar exams from 1997 to 2003.

**Size**: 2,657 questions

**Format**: JSON

**Annotation**: Manual annotation conducted by experts from relevant fields.

## 🔬 Methodology

**Methods**:
- Zero-shot
- 5-few-shot
- Chain of Thought (CoT)

**Metrics**:
- Accuracy

**Calculation**: The models' capabilities are evaluated across four dimensions with questions graded on a scale from A to 5A.

**Interpretation**: Scores of A, 2A, 3A, 4A, and 5A correspond to levels of model performance in IP agency consulting tasks.

**Baseline Results**: The best-performing models achieved scores of 2A.

**Validation**: Evaluated using multiple LLMs across different parameter sizes and types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
