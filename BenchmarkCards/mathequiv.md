# MathEquiv

## 📊 Benchmark Details

**Name**: MathEquiv

**Overview**: MathEquiv is the first dataset specifically designed for mathematical statement equivalence, enabling the training of a lightweight equivalence detector.

**Data Type**: step-level sentence pairs

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Jiawei1222/MathEquiv)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for evaluating mathematical statement equivalence detection.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Education Professionals

**Tasks**:
- Semantic Equivalence Detection
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: The MathEquiv dataset was constructed from 7,500 mathematical problems sourced from the MATH training set (Hendrycks et al., 2021).

**Size**: 7500 problems

**Format**: CSV

**Annotation**: The dataset was labeled via an iterative refinement process utilizing GPT-4o along with human expert review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of correctly identified equivalent statements.

**Interpretation**: Higher accuracy indicates better performance in identifying mathematical statement equivalence.

**Baseline Results**: N/A

**Validation**: The dataset was validated through human consensus on labeled pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of mathematical reasoning', 'Bias against certain types of mathematical statements']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
