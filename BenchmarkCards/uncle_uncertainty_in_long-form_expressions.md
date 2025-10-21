# UNCLE (Uncertainty in Long-form Expressions)

## 📊 Benchmark Details

**Name**: UNCLE (Uncertainty in Long-form Expressions)

**Overview**: UNCLE is a benchmark designed to evaluate uncertainty expression in both long- and short-form question answering (QA), bridging short- and long-form QA with paired questions and gold-standard answers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/rhyang2021/UNCLE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of a model’s ability to accurately express uncertainty in both long-form and short-form generation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Wikidata with key aspects formed for various entities.

**Size**: approximately 4,000 long-form QA instances and over 20,000 short-form QA pairs

**Format**: JSON

**Annotation**: Manual annotation by authors and verification process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Factual Accuracy
- Uncertain Accuracy
- Known to Correct Rate
- Unknown to Uncertain Rate
- Expression Accuracy

**Calculation**: Metrics are calculated based on the accuracy of responses concerning known and unknown aspects.

**Interpretation**: High scores indicate better model performance in expressing uncertainty.

**Validation**: Validated through both automated metrics and human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from annotators.

**Compliance With Regulations**: Not Applicable
