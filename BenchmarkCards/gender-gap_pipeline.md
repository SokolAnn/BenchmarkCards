# GENDER-GAP Pipeline

## 📊 Benchmark Details

**Name**: GENDER-GAP Pipeline

**Overview**: An automatic pipeline to characterize gender representation in large-scale datasets for 55 languages, using a multilingual lexicon of gendered person-nouns.

**Data Type**: N/A

**Languages**:
- English
- Finnish
- Zulu
- Vietnamese
- Ganda
- Japanese
- Lithuanian
- Arab Modern Standard Arabic
- Assamese
- Belarusian
- Bengali
- Bulgarian
- Catalan
- Czech
- Central Kurdish
- Mandarin Chinese
- Welsh
- Danish
- German
- Greek
- Irish
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Georgian
- Halh Mongolian
- Kyrgyz
- Lithuanian
- Ganda
- Standard Latvian
- Marathi
- Maltese
- Dutch
- Eastern Panjabi
- Western Persian
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Slovenian
- Spanish
- Swedish
- Swahili
- Tamil
- Thai
- Turkish
- Ukrainian
- Urdu
- Northern Uzbek
- Vietnamese
- Yue Chinese

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/ResponsibleNLP/tree/main/gender_gap_pipeline)

## 🎯 Purpose and Intended Users

**Goal**: To quantify gender representation bias of multilingual texts using lexical matching as a proxy.

**Target Audience**:
- NLP practitioners
- Researchers in gender bias in AI

**Tasks**:
- Characterizing gender representation in datasets
- Quantitative reporting of gender biases

**Limitations**: None

## 💾 Data

**Source**: Collected from various datasets including Common Crawl, FLORES-200, and NTREX-128.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Lexical matching
- Word segmentation using Stanza tokenizer

**Metrics**:
- Gender-class scores
- Distribution of gendered nouns

**Calculation**: Scores are defined by counting occurrences of gendered nouns and dividing by the total number of words.

**Interpretation**: Provides a depiction of gender representation in datasets.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Data bias
- Underrepresentation of genders in datasets

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Analysis covers 55 languages with attention to gender representation.

**Potential Harm**: Potential misrepresentation or bias in NLP systems due to conducted analysis.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
