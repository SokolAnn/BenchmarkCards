# WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation

## 📊 Benchmark Details

**Name**: WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation

**Overview**: WikiHint is the first manually curated dataset for the Automatic Hint Generation task, containing 5,000 hints for 1,000 questions, designed to assist users in finding correct answers through hints instead of direct responses.

**Data Type**: hint-question pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- Natural Questions

**Resources**:
- [GitHub Repository](https://github.com/DataScienceUIBK/WikiHint)

## 🎯 Purpose and Intended Users

**Goal**: To support users in developing reasoning skills by providing hints for question answering instead of direct answers.

**Target Audience**:
- ML Researchers
- Educators
- Information Retrieval Researchers

**Tasks**:
- Hint Generation
- Hint Ranking

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia articles, human annotations via Amazon MTurk

**Size**: 5,000 hints and 1,000 questions

**Format**: CSV

**Annotation**: Manual annotation by crowdworkers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Relevance
- Readability
- Convergence
- Familiarity
- Answer Leakage

**Calculation**: Metrics are calculated based on automated assessments and human judgments.

**Interpretation**: Higher values in Relevance and Convergence indicate better hint quality.

**Baseline Results**: N/A

**Validation**: Hints were verified by multiple judges for quality and correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: This work is licensed under a Creative Commons Attribution 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
