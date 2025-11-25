# I Never Said That: A dataset, taxonomy and baselines on response clarity classification

## 📊 Benchmark Details

**Name**: I Never Said That: A dataset, taxonomy and baselines on response clarity classification

**Overview**: The paper introduces a novel response clarity classification task and a human-labeled dataset consisting of 3,445 question-answer pairs derived from political interviews to analyze response clarity and evasion strategies.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- AmbigQA

**Resources**:
- [GitHub Repository](https://github.com/konstantinosftw/Question-Evasion)

## 🎯 Purpose and Intended Users

**Goal**: To detect the alignment and clarity of a given response with respect to its respective question using a proposed taxonomy.

**Target Audience**:
- ML Researchers
- Political Scientists
- NLP Practitioners

**Tasks**:
- Response Clarity Classification

**Limitations**: N/A

## 💾 Data

**Source**: Political interviews of US Presidents extracted from the official Whitehouse website.

**Size**: 3,445 examples

**Format**: CSV

**Annotation**: Annotated by human annotators using a proposed two-level taxonomy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the model's predictions compared to the ground truth labels.

**Interpretation**: Higher scores indicate better performance in identifying clarity and ambiguity in responses.

**Baseline Results**: LLama-70b: Acc. 0.775, F1 0.732 on the validation set for the clarity classification.

**Validation**: Inter-annotator agreement calculated using Fleiss Kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Misclassification of political responses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
