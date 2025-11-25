# iTRI-QA (Interactive Trained Research Innovator - Question Answering)

## 📊 Benchmark Details

**Name**: iTRI-QA (Interactive Trained Research Innovator - Question Answering)

**Overview**: A tool for the development of a customized question-answer (QA) dataset tailored for the needs of researchers leveraging language models (LMs) to retrieve scientific knowledge in a QA format.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Liu-Qiming/iTRI-QA/releases/tag/v1.0.0)

## 🎯 Purpose and Intended Users

**Goal**: To streamline the process of creating customized QA databases for research-oriented applications using LMs.

**Target Audience**:
- Researchers
- Domain Experts
- Academics

**Tasks**:
- Question Answering

**Limitations**: The computational resources required for fine-tuning and deploying even medium-sized LLMs can be prohibitive.

## 💾 Data

**Source**: PubMed and customized QA examples generated through domain expert input.

**Size**: 50 examples

**Format**: JSONL

**Annotation**: Manual curation by domain experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Evaluation loss

**Calculation**: Evaluation metrics are calculated based on the performance of the fine-tuned models on test datasets.

**Interpretation**: Lower evaluation loss indicates better model performance.

**Baseline Results**: Llama-3.2-1B and Llama-3.2-3B model comparisons for QA generation performance.

**Validation**: The methodology is validated through benchmarking experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
