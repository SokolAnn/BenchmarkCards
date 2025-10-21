# COPYBENCH

## 📊 Benchmark Details

**Name**: COPYBENCH

**Overview**: COPYBENCH is a benchmark designed to measure both literal and non-literal copying in language model generations, evaluating how these models reproduce copyright-protected content while also considering model utility in terms of fact recall and fluency.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Law

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/chentong0/copy-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate reproduction of copyright-protected text by language models, focusing on both literal and non-literal copying, alongside measuring the utility of the models.

**Target Audience**:
- AI Researchers
- Legal Experts
- Content Creators

**Tasks**:
- Text Generation
- Fact Recall

**Limitations**: The evaluation is limited to English fictional books and does not cover non-literal copying in other languages or domains.

## 💾 Data

**Source**: Fictional works sourced from CliffsNotes and BookMIA, containing copyright-protected content.

**Size**: 118 books for non-literal copying and 16 books for literal copying

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE-L
- F1 Score

**Calculation**: ROUGE-L measures the longest common subsequence between model outputs and source texts for literal copying. F1 Score is calculated for fact recall based on question-answer pairs.

**Interpretation**: A higher ROUGE-L score indicates a higher degree of reproduction, while the F1 score measures the accuracy of model responses in fact recall tasks.

**Baseline Results**: Comparative results of various language models on literal and non-literal copying metrics.

**Validation**: Validation includes human evaluation of a sample of outputs to ensure automatic metrics align with human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Copyright Risks
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
