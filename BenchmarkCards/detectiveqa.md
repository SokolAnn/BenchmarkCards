# DetectiveQA

## 📊 Benchmark Details

**Name**: DetectiveQA

**Overview**: DetectiveQA is a dataset specifically designed for narrative reasoning within long contexts, featuring 1200 human-annotated questions from detective novels in both Chinese and English, along with reference reasoning steps.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the long-context reasoning abilities of large language models using narrative reasoning based on detective novels.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark contains only data from detective novels and mainly serves narrative reasoning.

## 💾 Data

**Source**: Orthodox detective novels categorized for their logical puzzles.

**Size**: 1,200 questions

**Format**: JSON

**Annotation**: Manually annotated by experts with the assistance of LLMs for efficiency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Multiple-Choice Accuracy
- Step-wise Reasoning Metric

**Calculation**: Multiple-choice accuracy is calculated as the percentage of correctly answered questions; step-wise reasoning metric counts the number of correct reference steps included in model responses.

**Interpretation**: Higher scores indicate better reasoning alignment with detective reasoning steps.

**Validation**: The dataset's annotation quality was validated through manual checks by the authors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All novels have been copyright-checked to ensure fair use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
