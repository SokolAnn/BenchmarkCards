# AfriHG (African News Headline Generation)

## 📊 Benchmark Details

**Name**: AfriHG (African News Headline Generation)

**Overview**: This paper introduces AfriHG—a news headline generation dataset created by combining data from XLSum and MasakhaNEWS datasets focusing on 16 languages widely spoken in Africa.

**Data Type**: article-headline pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Amharic
- Hausa
- Igbo
- Kirundi
- Nigerian-Pidgin
- Oromo
- Somali
- Kiswahili
- Tigrinya
- Yoruba
- isiXhosa
- isiZulu
- Shona
- English
- French
- Arabic

**Similar Benchmarks**:
- XL-SUM
- MasakhaNEWS

**Resources**:
- [GitHub Repository](https://github.com/dadelani/AfriHG)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to generate news headlines in various African languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Data Scientists
- NLP Practitioners

**Tasks**:
- Text Generation
- Summarization

**Limitations**: Languages with non-Latin script have a very low ROUGE score (<4.0) on news headline generation.

## 💾 Data

**Source**: Merging data from the XLSum dataset and the MasakhaNEWS corpus, focusing on news articles from major news outlets like BBC, VOA, and Isolezwe.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation with ROUGE scores

**Metrics**:
- ROUGE

**Calculation**: ROUGE scores calculated based on article-headline pairs.

**Interpretation**: Higher ROUGE scores indicate better performance in generating coherent and relevant headlines.

**Baseline Results**: N/A

**Validation**: Validation done using the retained development and test split from the XL-SUM dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset covers multiple African languages, providing a demographic distribution.

**Potential Harm**: ['Potential for generating biased or inaccurate headlines.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
