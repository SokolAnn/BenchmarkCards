# MathWriting: A Dataset For Handwritten Mathematical Expression Recognition

## 📊 Benchmark Details

**Name**: MathWriting: A Dataset For Handwritten Mathematical Expression Recognition

**Overview**: MathWriting is the largest dataset of online handwritten mathematical expressions to date, consisting of 230k human-written samples and an additional 400k synthetic ones, aimed at improving the recognition of handwritten mathematical expressions.

**Data Type**: ink samples with corresponding LaTeX expressions

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- CROHME

**Resources**:
- [Resource](https://storage.googleapis.com/mathwriting_data/mathwriting-2024.tgz)
- [Resource](https://storage.googleapis.com/mathwriting_data/mathwriting-2024-excerpt.tgz)
- [GitHub Repository](https://github.com/google-research/google-research/tree/master/mathwriting)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for researching and developing algorithms for the recognition of handwritten mathematical expressions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Handwritten Mathematical Expression Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Human contributions through an Android app and synthetic data based on LaTeX expressions from Wikipedia.

**Size**: 230,000 human-written inks, 400,000 synthetic inks

**Format**: InkML

**Annotation**: Manual annotation through LaTeX expressions

## 🔬 Methodology

**Methods**:
- CTC Transformer
- OCR models

**Metrics**:
- Character Error Rate (CER)

**Calculation**: CER is calculated where a 'character' is defined as a LaTeX token.

**Interpretation**: Lower CER indicates better recognition accuracy.

**Baseline Results**: CTC Transformer achieved 5.49 CER on test split.

**Validation**: Models were evaluated using distinct validation and test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

**Consent Procedures**: Participants agreed to standard Google terms of use and privacy policy.

**Compliance With Regulations**: Not Applicable
