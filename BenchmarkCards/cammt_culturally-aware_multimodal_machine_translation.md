# CAMMT (Culturally-Aware Multimodal Machine Translation)

## 📊 Benchmark Details

**Name**: CAMMT (Culturally-Aware Multimodal Machine Translation)

**Overview**: CAMMT is a human-curated benchmark of over 5,800 triples of images along with parallel captions in English and regional languages, designed to evaluate multimodal machine translation systems on culturally relevant translation tasks.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Amharic
- Arabic
- Bengali
- Bulgarian
- Chinese
- Filipino
- Igbo
- Indonesian
- Japanese
- Korean
- Malay
- Marathi
- Oromo
- Portuguese
- Russian
- Spanish
- Swahili
- Tamil
- Urdu

**Similar Benchmarks**:
- CoMMuTe

**Resources**:
- [Resource](https://huggingface.co/datasets/villacu/cammt)

## 🎯 Purpose and Intended Users

**Goal**: To support broader efforts to build and evaluate multimodal translation systems that are better aligned with cultural nuance and regional variations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multimodal Machine Translation

**Limitations**: Dataset size is constrained by the original CVQA dataset; relies on single annotators which may introduce subjectivity.

## 💾 Data

**Source**: Human-curated triples from CVQA transformed into declarative caption pairs.

**Size**: 5,817 triples

**Format**: JSON

**Annotation**: Manual annotation by native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- chrF++

**Calculation**: Metrics are calculated using SacreBLEU and include evaluations of multimodal translation quality through human preferences.

**Interpretation**: Higher scores in human preference evaluations suggest improvements in cultural and semantic alignment of translations.

**Baseline Results**: Compared performance of VLMs against strong baselines like NLLB-600M and NLLB-3.3B.

**Validation**: Validation included assessing translation performance across multiple languages and models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Future work should focus on expanding annotator diversity to improve coverage and objectivity of cultural relevance judgments.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercialShareAlike 4.0 International (CC BY-NC-SA 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
