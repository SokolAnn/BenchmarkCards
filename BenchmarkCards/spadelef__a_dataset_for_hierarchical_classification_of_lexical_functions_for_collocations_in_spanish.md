# SpaDeLeF: A Dataset for Hierarchical Classification of Lexical Functions for Collocations in Spanish

## 📊 Benchmark Details

**Name**: SpaDeLeF: A Dataset for Hierarchical Classification of Lexical Functions for Collocations in Spanish

**Overview**: This paper presents a dataset of frequent Spanish verb-noun collocations and sentences where they occur, each assigned to one of 37 defined lexical functions for hierarchical classification.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To contribute to the solution of the problem of lexical resources shortage by building a collection of Spanish verb-noun collocations annotated with lexical functions.

**Target Audience**:
- ML Researchers
- Linguists
- NLP Practitioners

**Tasks**:
- Hierarchical Classification

**Limitations**: The dataset is not balanced in terms of the number of sentences and collocations per lexical function.

## 💾 Data

**Source**: The dataset was created using dependency tree parsing of sentences extracted from Spanish newspapers like Excelsior, La Razón, and Público.

**Size**: 957 collocations

**Format**: N/A

**Annotation**: Annotated with lexical functions from the Meaning-Text Theory.

## 🔬 Methodology

**Methods**:
- Hierarchical Classification
- Naïve Bayes
- Support Vector Machine

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on results from the classification tasks across different levels.

**Interpretation**: Precision indicates the fraction of relevant instances among the retrieved instances; Recall indicates the fraction of relevant instances that were retrieved; F1 Score is the harmonic mean of Precision and Recall.

**Baseline Results**: BETO for classification tasks showed weighted average F1-scores ranging from 0.672 to 0.793 across tasks.

**Validation**: K-fold cross-validation was used for model evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
