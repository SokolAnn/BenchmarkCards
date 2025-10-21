# PerCQA: Persian Community Question Answering Dataset

## 📊 Benchmark Details

**Name**: PerCQA: Persian Community Question Answering Dataset

**Overview**: PerCQA is the first Persian dataset for Community Question Answering (CQA). It contains 989 questions and 21,915 annotated answers crawled from the Ninisite forum, providing strong benchmarks for answer selection tasks within the Persian language.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- SemEval 2015
- TREC QA
- WikiQA

**Resources**:
- [GitHub Repository](https://github.com/PerCQA)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the research and applications of CQA tasks in the Persian language.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Answer Selection
- Question Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Questions and answers crawled from the Persian forum Ninisite.

**Size**: 989 questions and 21,915 answers

**Format**: N/A

**Annotation**: Annotated by a team using detailed guidelines, labeled as 'Good', 'Bad', and 'Potential'.

## 🔬 Methodology

**Methods**:
- BiLSTM-attention
- RCNN
- PV-Cnt
- CETE

**Metrics**:
- Macro F1 Score

**Calculation**: Macro F1 Score calculated based on the predictions made by the proposed models.

**Interpretation**: Higher F1 scores indicate better performance in answer selection.

**Baseline Results**: The best result achieved was a macro F1 score of 61.14 using XLM-R fine-tuned with SemEvalCQA datasets.

**Validation**: The quality of labeling was evaluated via Cohen's kappa score.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
