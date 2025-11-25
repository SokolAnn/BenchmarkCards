# MODE LING

## 📊 Benchmark Details

**Name**: MODE LING

**Overview**: MODE LING is a novel benchmark of Linguistics Olympiad-style puzzles which tests few-shot reasoning in AI systems, requiring compositional generalization and inductive reasoning based on a small number of examples.

**Data Type**: linguistic puzzles

**Domains**:
- Natural Language Processing

**Languages**:
- Ayutla Mixe
- Bangime
- Chimalapa Zoque
- Dogon
- Engenni
- Guugu Yimithirr
- Kalam
- Komi-Zyrian
- Kutenai
- Mapudungan
- Misantla Totonac
- Mixtepec Zapotec
- Ngadha
- Niuean
- Rapa Nui
- Seri
- Totonac

**Resources**:
- [GitHub Repository](https://github.com/nathanchi/modeLing)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate LLMs’ capacity to reason analytically in unseen foreign languages.

**Target Audience**:
- ML Researchers
- Language Model Evaluators
- Linguists

**Tasks**:
- Linguistic Reasoning

**Limitations**: The authors of the paper are not native speakers of the languages included, and there cannot be guaranteed accuracy of the sentences used.

## 💾 Data

**Source**: Generated and curated by the authors specifically for this benchmark.

**Size**: 48 puzzles, 272 questions

**Format**: N/A

**Annotation**: Problems were test-solved and rated for difficulty by two International Linguistics Olympiad medalists.

## 🔬 Methodology

**Methods**:
- Exact Match Evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed based on exact matches for puzzle solutions.

**Interpretation**: Good performance is indicated by higher exact match accuracy.

**Validation**: Validated through evaluation against existing knowledge of the languages without training data leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Data Contamination

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination

**Demographic Analysis**: The choice of extremely low-resource languages aims to improve diversity in NLP evaluations, but bias in the selection process may exist.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
