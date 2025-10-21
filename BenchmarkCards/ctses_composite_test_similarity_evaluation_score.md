# CTSES (Composite Test Similarity Evaluation Score)

## 📊 Benchmark Details

**Name**: CTSES (Composite Test Similarity Evaluation Score)

**Overview**: CTSES is a behavior-preserving, readability-aware metric specifically tailored to evaluate test refactoring. It combines CodeBLEU, METEOR, and ROUGE-L into a weighted composite metric that balances syntactic accuracy, lexical clarity, and structural alignment.

**Data Type**: code similarity scores

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- Defects4J
- SF110

**Resources**:
- [GitHub Repository](https://github.com/anonymous/CTSES-75D4)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of the quality of refactored unit tests leveraging Large Language Models.

**Target Audience**:
- Software Engineers
- ML Researchers
- Test Developers

**Tasks**:
- Test Refactoring Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Over 5,000 unit tests automatically refactored by GPT-4o and Mistral-Large-2407 using two established Java benchmarks: Defects4J and SF110.

**Size**: 5,000+ test suites

**Format**: N/A

**Annotation**: Tests were refactored using Chain-of-Thought prompting.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- CTSES
- CodeBLEU
- METEOR
- ROUGE-L

**Calculation**: CTSES is calculated as a weighted linear combination of CodeBLEU, METEOR, and ROUGE-L: CTSES = α·CodeBLEU + β·METEOR + γ·ROUGE-L.

**Interpretation**: Higher CTSES scores indicate better alignment with developer expectations regarding readability, structural quality, and behavioral consistency.

**Baseline Results**: N/A

**Validation**: Empirical validation is performed against baseline similarity metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
