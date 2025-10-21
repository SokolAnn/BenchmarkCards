# CVEFixes (Refined Version)

## 📊 Benchmark Details

**Name**: CVEFixes (Refined Version)

**Overview**: This paper presents SCoPE, a code processing framework for refining the CVEFixes dataset specifically for Software Vulnerability Detection (SVD), addressing prior flaws in the dataset and aiming to enhance the performance of LLMs.

**Data Type**: source code

**Domains**:
- Computer Science

**Languages**:
- C
- C++

**Resources**:
- [GitHub Repository](https://github.com/jp2425/SCoPE)
- [Resource](https://zenodo.org/records/7029359)

## 🎯 Purpose and Intended Users

**Goal**: To refine the CVEFixes dataset for software vulnerability detection using the SCoPE framework.

**Target Audience**:
- ML Researchers
- Cybersecurity Experts

**Tasks**:
- Software Vulnerability Detection

**Limitations**: The refined dataset may still contain faulty entries not identified during processing.

## 💾 Data

**Source**: Created from the CVEFixes dataset version 1.0.7.

**Size**: 11,573 entries

**Format**: CSV

**Annotation**: Processed to remove duplicates and improve feature representation.

## 🔬 Methodology

**Methods**:
- Feature representation analysis
- Fine-tuning of LLMs

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Metrics were calculated based on the performance of the LLMs trained on the refined dataset.

**Interpretation**: Results suggested that the model performance did not significantly improve post-refinement of the dataset.

**Validation**: Used an 80-10-10 split for train, test, and validation sets with stratification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: The possibility of training on erroneous data points could impact the models' effectiveness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
