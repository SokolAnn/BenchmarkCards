# BEAR (Benchmark for Evaluating Abilities of Relational Knowledge)

## 📊 Benchmark Details

**Name**: BEAR (Benchmark for Evaluating Abilities of Relational Knowledge)

**Overview**: This study evaluates how efficiently language models learn and retain facts with an emphasis on sample efficiency and factual knowledge recall across varying model architectures.

**Data Type**: fact-frequency statistics

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Jabbawukis/sample-efficiency-evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To assess the sample efficiency of various language models in learning factual information from a pre-training corpus.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Fact Recall

**Limitations**: Limited to analyzing small to medium-sized language models; does not evaluate models exceeding one billion parameters.

## 💾 Data

**Source**: English Wikipedia dump (Wikimedia Foundation, 2023)

**Size**: 5 billion tokens

**Format**: Raw text

**Annotation**: Fact frequencies calculated using a heuristic matching algorithm.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Weighted Accuracy Score (WASB)

**Calculation**: Sample efficiency determined through models' responses to factual queries and the frequency of encountered facts.

**Interpretation**: Higher scores in sample efficiency metrics indicate a model learns factual information more effectively and requires fewer training samples.

**Validation**: Evaluation of model performance during different training checkpoints based on the frequency of fact occurrences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
