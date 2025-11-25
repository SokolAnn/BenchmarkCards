# The Paradox of Poetic Intent in Back-Translation

## 📊 Benchmark Details

**Name**: The Paradox of Poetic Intent in Back-Translation

**Overview**: This study constructs a diverse corpus for evaluating the quality of large language models in Chinese translation, focusing on the preservation of poetic intent, cultural heritage, and handling specialized terminology. The study introduces a back-translation framework and evaluates multiple metrics to assess the translation capabilities of LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/university/translation-corpus)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the translation quality of large language models (LLMs) in preserving Poetic Intent while translating Chinese texts.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Translation Studies Scholars

**Tasks**:
- Machine Translation
- Back-Translation

**Limitations**: N/A

## 💾 Data

**Source**: Diverse corpus comprising historical paradoxes, scientific abstracts, and literary texts collected from CNKI and popular Chinese songs.

**Size**: 295 Chinese abstracts across multiple scientific fields.

**Format**: JSON

**Annotation**: Data was compiled manually, ensuring accuracy and representation across various themes.

## 🔬 Methodology

**Methods**:
- Back-Translation
- Friedman Test
- Statistical Evaluation

**Metrics**:
- BLEU
- CHRF
- TER
- Semantic Similarity

**Calculation**: Metrics calculated based on n-gram matching and semantic alignment between original and back-translated texts.

**Interpretation**: Higher BLEU scores indicate closer alignment to the original text, while TER values indicate the editing effort required for fidelity.

**Baseline Results**: N/A

**Validation**: Statistical significance confirmed through Friedman test and pairwise comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for cultural misunderstanding in translations if deep semantic nuances are not captured.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
