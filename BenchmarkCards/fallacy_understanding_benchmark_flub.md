# FaLlacy Understanding Benchmark (FLUB)

## 📊 Benchmark Details

**Name**: FaLlacy Understanding Benchmark (FLUB)

**Overview**: FLUB contains cunning texts that are easy for humans to understand but difficult for models to grasp. It is designed to evaluate the fallacy understanding ability of LLMs through tasks such as Answer Selection, Cunning Type Classification, and Fallacy Explanation.

**Data Type**: cunning texts

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/THUKElab/FLUB)

## 🎯 Purpose and Intended Users

**Goal**: To challenge the reasoning and understanding abilities of Large Language Models (LLMs) by evaluating their ability to understand cunning texts and fallacies.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Answer Selection
- Cunning Type Classification
- Fallacy Explanation

**Limitations**: N/A

## 💾 Data

**Source**: Cunning texts collected from the 'Ruozhiba' online forum.

**Size**: 834 samples

**Format**: JSON

**Annotation**: Annotated by native Chinese speakers with oversight from senior annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F-1 Score

**Calculation**: Accuracy is calculated based on selection results, and F-1 Score is used for classification tasks to balance precision and recall.

**Interpretation**: High scores indicate better understanding and classification of cunning texts.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive experimentation with representative LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All texts are anonymized, and sensitive information has been removed.

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Data was collected following the Baidu Bar agreement, which allows academic use.

**Compliance With Regulations**: Not Applicable
