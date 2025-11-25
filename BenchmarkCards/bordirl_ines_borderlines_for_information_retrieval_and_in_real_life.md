# BORDIRL INES (BorderLines for Information Retrieval and In Real Life)

## 📊 Benchmark Details

**Name**: BORDIRL INES (BorderLines for Information Retrieval and In Real Life)

**Overview**: BORDIRL INES is a multilingual dataset covering territorial disputes paired with retrieved Wikipedia documents across 49 languages. It evaluates the cross-lingual robustness of retrieval-augmented generation (RAG) systems.

**Data Type**: query-document pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Chinese
- Hindi
- Arabic
- Korean
- Vietnamese
- French
- Russian
- Turkish
- Portuguese
- Indonesian
- Urdu
- Japanese
- Thai
- Burmese
- Hungarian
- Greek
- Swahili
- Somali
- Armenian
- Serbian
- Malay
- Azerbaijani
- Georgian
- Uighur
- Bene
- Tigrinya
- Basque
- Ukrainian
- Haitian

**Resources**:
- [Resource](https://www.example.com/dataset/BORDIRL_INES)
- [GitHub Repository](https://github.com/username/BORDIRL_INES)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing the cross-lingual robustness of retrieval-augmented generation systems on culturally-sensitive tasks.

**Target Audience**:
- ML Researchers
- Geopolitical Analysts
- Natural Language Processing Practitioners

**Tasks**:
- Multilingual Information Retrieval
- Cross-lingual Knowledge Retrieval

**Limitations**: This study focuses on territorial disputes, which may not generalize to other types of queries.

## 💾 Data

**Source**: Wikipedia

**Size**: 19,916 unique query-document pairs

**Format**: JSON

**Annotation**: Annotated for relevance and viewpoint

## 🔬 Methodology

**Methods**:
- Cross-lingual retrieval evaluation
- Human evaluation for annotation
- LLM-based evaluation using various prompts

**Metrics**:
- Factuality
- Consistency
- Geopolitical Bias

**Calculation**: Metrics calculated based on concurrence scores comparing responses across languages.

**Interpretation**: Higher scores indicate better alignment with factual information sources and consistent outputs across languages.

**Baseline Results**: Comparisons made against existing multilingual RAG systems.

**Validation**: Results validated across 720 queries for 251 territories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Annotated data includes diverse language perspectives to mitigate biases.

**Potential Harm**: Potential for misinformation due to cultural sensitivities around territorial disputes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons

**Consent Procedures**: Annotation participants were fully informed and could opt out of tasks due to sensitivity.

**Compliance With Regulations**: Not Applicable
