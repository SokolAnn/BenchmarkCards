# Complex-TR (Complex Temporal Reasoning)

## 📊 Benchmark Details

**Name**: Complex-TR (Complex Temporal Reasoning)

**Overview**: The Complex-TR dataset focuses on multi-answer and multi-hop temporal reasoning, addressing the shortcomings of existing temporal QA datasets that primarily evaluated one-hop questions and used inappropriate metrics for multi-answer assessments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TempReason
- TimeQA
- TempLAMA

**Resources**:
- [GitHub Repository](https://github.com/nusnlp/complex-tr)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for multi-hop and multi-answer temporal reasoning in question-answering systems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset may contain factual errors existing in the Wikidata knowledge base.

## 💾 Data

**Source**: Constructed from the Wikidata knowledge base and verified using human annotators.

**Size**: 10,800 examples

**Format**: JSON

**Annotation**: Manually verified by college-educated annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Data augmentation
- Context refinement

**Metrics**:
- Set-level accuracy
- Answer-level F1

**Calculation**: Metrics are calculated based on the strict criteria of matching the entire set of answers.

**Interpretation**: Higher set accuracy indicates better performance on multi-answer questions; lower answer F1 scores indicate the model's struggle to retrieve all correct answers.

**Validation**: Human verification of the QA pairs and contexts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data was constructed from the Wikidata knowledge base and Wikipedia articles, which are under creative commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
