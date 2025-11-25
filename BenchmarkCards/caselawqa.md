# CaselawQA

## 📊 Benchmark Details

**Name**: CaselawQA

**Overview**: A benchmark comprising 260 legal annotation tasks, nearly all new to the machine learning community.

**Data Type**: question-answering pairs

**Domains**:
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- LegalBench

**Resources**:
- [GitHub Repository](https://github.com/socialfoundations/lawma)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate empirical legal research through efficient legal annotation.

**Target Audience**:
- Legal Researchers
- Empirical Legal Scholars

**Tasks**:
- Legal Classification

**Limitations**: The fine-tuned models are still far from perfect, and the variance in accuracy across tasks remains high.

## 💾 Data

**Source**: U.S. Supreme Court Database (SCDB) and U.S. Courts of Appeals Database (USCAD).

**Size**: 718,971 task examples

**Format**: N/A

**Annotation**: Labels created from existing court case data.

## 🔬 Methodology

**Methods**:
- Multiple-choice evaluation
- Fine-tuning of language models

**Metrics**:
- Accuracy

**Calculation**: Weighted average of task accuracies across all task examples.

**Interpretation**: Higher accuracy indicates better model performance on legal annotation tasks.

**Baseline Results**: Average accuracy of commercial models ranged from 70% to 78% on CaselawQA.

**Validation**: Evaluated models against a train/validation/test split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
