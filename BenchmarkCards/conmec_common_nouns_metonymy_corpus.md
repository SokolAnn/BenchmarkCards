# ConMeC (Common Nouns Metonymy Corpus)

## 📊 Benchmark Details

**Name**: ConMeC (Common Nouns Metonymy Corpus)

**Overview**: The dataset consists of 6,000 sentences with human annotations indicating whether the target common noun is used metonymically or not.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RelocaR
- SemEval2007-Task8
- Pedinotti-Lenci

**Resources**:
- [GitHub Repository](https://github.com/SaptGhosh/ConMeC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for training and evaluating metonymy resolution systems focusing on common nouns.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Metonymy Resolution

**Limitations**: The dataset focuses only on six types of common noun metonymy and may not cover all possible variations.

## 💾 Data

**Source**: Sentences extracted from Wikipedia and annotated by human annotators.

**Size**: 6,000 sentences

**Format**: JSON

**Annotation**: Human annotation indicating metonymic vs non-metonymic usage.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based prompting
- Fine-tuning BERT

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Precision, Recall and F1 Score are calculated based on the model predictions compared to the gold annotations.

**Interpretation**: Higher F1 scores indicate better performance in correctly identifying metonymic usage.

**Baseline Results**: BERT achieved an accuracy of 86.6 and macro-F1 of 82.9 on this dataset.

**Validation**: Evaluation against human-annotated gold standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset was sampled to avoid dominant noun usage, aiming for diversity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: N/A - Data is freely available.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
