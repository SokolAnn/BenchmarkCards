# HARDMATH

## 📊 Benchmark Details

**Name**: HARDMATH

**Overview**: HARDMATH is a dataset addressing the lack of advanced applied mathematics problems in existing Large Language Model benchmark datasets. It features 1,466 problems requiring analytical approximation techniques, making it challenging for LLMs. The dataset includes HARDMATH-MINI, a subsampled test set with 366 problems, and emphasizes issues like mathematical reasoning and computational tool use.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K
- MATHQA
- ODYSSEY-MATH

**Resources**:
- [GitHub Repository](https://github.com/sarahmart/HARDMath)
- [Resource](https://arxiv.org/abs/2410.09988)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark LLMs' capabilities in handling advanced applied mathematics problems that require analytical reasoning and computational tools.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Equation Solving

**Limitations**: N/A

## 💾 Data

**Source**: Consists of algorithmically generated problems and their solutions, validated against numerical results.

**Size**: 1,466 problems

**Format**: JSON

**Annotation**: Automatically generated solutions with human verification for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers provided by LLMs against the dataset solutions.

**Interpretation**: Performance is assessed through model accuracy comparing outputs to ground truth answers.

**Baseline Results**: Leading models were evaluated, with GPT-4 achieving an overall accuracy of 43.8% on HARDMATH-MINI.

**Validation**: Systems of equations and numerical solutions were used for validation against known ground truths.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
