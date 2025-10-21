# QualBench

## 📊 Benchmark Details

**Name**: QualBench

**Overview**: QualBench is the first multi-domain Chinese QA benchmark dedicated to localized assessment of Chinese LLMs, incorporating over 17,000 questions across six vertical domains derived from 24 Chinese qualifications.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- GAOKAO-Bench
- LexEval
- MedBench
- CFLUE

**Resources**:
- [GitHub Repository](https://github.com/mengze-hong/QualBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive vertical domain evaluation for Chinese LLMs based on localized qualification exams.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The dataset is imbalanced with an over-representation of certain domains and focuses exclusively on multiple-choice and true/false questions.

## 💾 Data

**Source**: Derived from 24 Chinese qualification examinations across six vertical domains.

**Size**: 17,316 questions

**Format**: N/A

**Annotation**: Validated by domain experts for relevance and completeness.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy calculated based on the number of correct answers over total questions.

**Interpretation**: Higher accuracy indicates better model performance on specialized knowledge in localized settings.

**Baseline Results**: Qwen2.5 model achieved an accuracy of 75.26% on QualBench.

**Validation**: Dataset validation was conducted by industry professionals and via comparison to existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All questions are sourced from publicly accessible qualifications.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with relevant regulations regarding data use and distribution.
