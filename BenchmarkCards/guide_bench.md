# GUIDE BENCH

## 📊 Benchmark Details

**Name**: GUIDE BENCH

**Overview**: GUIDE BENCH is a comprehensive benchmark designed to evaluate guideline following performance of LLMs in real-world applications.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Dlxxx/GuideBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of LLMs to follow domain-oriented guidelines in real-world applications.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a combination of automatic synthesis and human-in-the-loop refinement.

**Size**: 1,272 instances

**Format**: JSON

**Annotation**: Human reviewed and curated.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the number of correctly predicted labels comparing outputs to ground truth.

**Interpretation**: A higher accuracy indicates better alignment of LLM responses with guideline requirements.

**Baseline Results**: Results from 18 prominent LLMs, with Deepseek-R1 being one of the best-performing models.

**Validation**: Validated through human annotation and expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**
- **Privacy**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures are taken to address privacy risks, ensuring rigorous de-identification and anonymization.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
