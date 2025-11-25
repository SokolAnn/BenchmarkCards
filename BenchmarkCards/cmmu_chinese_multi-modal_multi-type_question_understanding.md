# CMMU (Chinese Multi-modal Multi-type Question Understanding)

## 📊 Benchmark Details

**Name**: CMMU (Chinese Multi-modal Multi-type Question Understanding)

**Overview**: CMMU is a novel benchmark for multi-modal and multi-type question understanding and reasoning in Chinese. It consists of 3,603 questions in 7 subjects, covering knowledge from primary to high school, featuring multiple-choice, multiple-response, and fill-in-the-blank questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Similar Benchmarks**:
- ScienceQA
- MMMU
- M3Exam

**Resources**:
- [GitHub Repository](https://github.com/FlagOpen/CMMU)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multi-modal and multi-type question understanding and reasoning abilities of multi-modal large language models (MLLMs) in Chinese.

**Target Audience**:
- ML Researchers
- Education Practitioners
- Model Developers

**Tasks**:
- Multi-modal Question Answering
- Question Understanding

**Limitations**: N/A

## 💾 Data

**Source**: The questions were collected from diverse exams and educational materials, comprising both text and images.

**Size**: 3,603 questions

**Format**: JSON

**Annotation**: Questions were manually reviewed and corrected, including transformation of formulas into LaTeX format.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Positional Error Variance

**Calculation**: Positional Error Variance measures the extent of position bias in multiple-choice questions through cyclically changing the positions of the answer options.

**Interpretation**: A model is considered proficient if it can answer questions correctly across diverse formats without showing significant positional bias.

**Baseline Results**: CMMU was evaluated against several MLLMs, with performance varied across different question types and subjects.

**Validation**: The validation set consists of 1,800 questions, while the test set has 1,803 questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
