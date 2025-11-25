# ThaliaType

## 📊 Benchmark Details

**Name**: ThaliaType

**Overview**: ThaliaType is a new dataset specifically designed to evaluate the type inference capabilities of LLMs for Java code snippets while mitigating the potential biases introduced by data leakage.

**Data Type**: code snippets

**Domains**:
- Computer Science

**Languages**:
- Java

**Similar Benchmarks**:
- StatType-SO

**Resources**:
- [GitHub Repository](https://github.com/uw-pluverse/thalia-type)

## 🎯 Purpose and Intended Users

**Goal**: To assess the true type inference capabilities of LLMs on unseen Java code snippets.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Type Inference

**Limitations**: N/A

## 💾 Data

**Source**: Generated using Thalia, a program synthesis technique.

**Size**: 300 code snippets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation on unseen code snippets
- Comparison with existing benchmarks

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision and recall are calculated based on the accuracy of inferred fully qualified names (FQNs) against the expected FQNs.

**Interpretation**: A higher precision and recall indicate better type inference capabilities.

**Baseline Results**: SnR achieved precision of 84.15% and recall of 84.43% on ThaliaType.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Leakage
- Generalization

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
