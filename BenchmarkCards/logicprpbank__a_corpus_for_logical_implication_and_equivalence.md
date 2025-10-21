# LogicPrpBank: A Corpus for Logical Implication and Equivalence

## 📊 Benchmark Details

**Name**: LogicPrpBank: A Corpus for Logical Implication and Equivalence

**Overview**: LOGIC PRPBANK contains 7093 Propositional Logic Statements (PLSs) across six mathematical subjects to study the reasoning capabilities of Language Models (LMs) regarding logical implication and equivalence.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- ENTAILMENT BANK
- LOGIC INFERENCE

**Resources**:
- [GitHub Repository](https://github.com/JZCS2018/AI4ED2024)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the reasoning of complex propositional logic in educational applications, particularly Intelligent Tutoring Systems (ITSs).

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Logical Reasoning
- Text Classification

**Limitations**: The corpus may contain annotating errors and has limited coverage of propositional logic beyond mathematical fields.

## 💾 Data

**Source**: Generated from ChatGPT API and validated by qualified human annotators.

**Size**: 7,093 Propositional Logic Statements (PLSs)

**Format**: N/A

**Annotation**: Validated by qualified human annotators who corrected any inconsistencies in truth values.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: F1 Scores calculated based on classifier performance on the test set.

**Interpretation**: Higher F1 Scores indicate better performance in classifying the truth values of PLSs.

**Validation**: Split into train (70%), validation (10%), and test (20%) sets; using three-seed runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
