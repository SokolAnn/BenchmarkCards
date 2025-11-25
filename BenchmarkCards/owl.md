# OWL

## 📊 Benchmark Details

**Name**: OWL

**Overview**: OWL is a dataset probing cross-lingual memorization in large language models, containing 31,540 aligned excerpts from 20 books across ten languages, allowing the evaluation of memorization across models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Turkish
- Vietnamese
- Sesotho
- Yoruba
- Maithili
- Malagasy
- Setswana
- Tahitian

**Resources**:
- [GitHub Repository](https://github.com/emirkaan5/OWL)

## 🎯 Purpose and Intended Users

**Goal**: To investigate multilingual and cross-lingual memorization capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Direct Probing
- Name Cloze
- Prefix Probing

**Limitations**: N/A

## 💾 Data

**Source**: Aligned excerpts from 20 books including official translations and newly produced machine translations.

**Size**: 31,540 passages

**Format**: text

**Annotation**: Manual tagging of named entities and alignment of translations.

## 🔬 Methodology

**Methods**:
- Direct Probing
- Name Cloze
- Prefix Probing

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated by comparing model predictions against ground-truth data.

**Interpretation**: Higher accuracy indicates better memorization and knowledge recall by models across languages.

**Validation**: Manual verification of aligned excerpts and passage content.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
