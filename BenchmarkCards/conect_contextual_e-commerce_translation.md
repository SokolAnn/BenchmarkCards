# ConECT (Contextual E-Commerce Translation)

## 📊 Benchmark Details

**Name**: ConECT (Contextual E-Commerce Translation)

**Overview**: ConECT is a new Czech-to-Polish e-commerce product translation dataset coupled with images and product metadata consisting of 11,400 sentence pairs, designed to support research on context-aware machine translation in the e-commerce domain.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Czech
- Polish

**Similar Benchmarks**:
- Multi30K
- CoMMuTE

**Resources**:
- [Resource](https://huggingface.co/datasets/allegro/ConECT)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the ConECT dataset is to support research into context-aware translation tasks in the e-commerce domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from the allegro.pl e-commerce platform and manually translated by professional translators.

**Size**: 11,400 sentence pairs

**Format**: JSON

**Annotation**: Manual translation by professional translators.

## 🔬 Methodology

**Methods**:
- Fine-tuning of vision-language models
- Text-to-text models evaluation

**Metrics**:
- sacreBLEU
- chrF
- COMET

**Calculation**: Metrics are calculated based on translations produced for the ConECT test sets.

**Interpretation**: Higher scores in BLEU and COMET indicate better translation quality.

**Validation**: Models were validated on the ConECT validation set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
