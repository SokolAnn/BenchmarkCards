# Wild2MaxDiacs (Multi-genre Wild Diacritization to Maximal Diacritization)

## 📊 Benchmark Details

**Name**: Wild2MaxDiacs (Multi-genre Wild Diacritization to Maximal Diacritization)

**Overview**: Wild2MaxDiacs is a new annotated dataset designed for evaluating models to exploit naturally occurring diacritics in Arabic text and improve the quality of Arabic diacritization tools.

**Data Type**: word-level diacritization pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- WikiNews
- Penn Arabic Treebank

**Resources**:
- [GitHub Repository](https://github.com/CAMeL-Lab/wild_diacritics)

## 🎯 Purpose and Intended Users

**Goal**: To enhance Arabic diacritization models by utilizing patterns from partially diacritized words and to provide an open-source resource for researchers.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Diacritization

**Limitations**: The observations are limited by the selection of genres and sample sizes studied.

## 💾 Data

**Source**: Annotated dataset created from six diverse genres including news articles, novels, children’s books, poetry, political documents, and ChatGPT outputs.

**Size**: 6,000 words

**Format**: N/A

**Annotation**: Annotated by two Arabic native speakers following a definition of in-context full diacritization.

## 🔬 Methodology

**Methods**:
- Hybrid (neuro-symbolic) analyze-and-disambiguate approach

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated by matching outputs against human-annotated maximal diacritizations.

**Interpretation**: Higher accuracy indicates better performance of diacritization models utilizing the dataset.

**Baseline Results**: The baseline model accuracy increased from 47.1% to 84.5% with enhancements.

**Validation**: Evaluated using a well-formedness check and comparison against Oracle performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
