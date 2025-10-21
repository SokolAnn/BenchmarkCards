# AmbGIMT (Gender-Inclusive Machine Translation with Ambiguous attitude words)

## 📊 Benchmark Details

**Name**: AmbGIMT (Gender-Inclusive Machine Translation with Ambiguous attitude words)

**Overview**: AmbGIMT is a gender-inclusive machine translation benchmark that assesses gender bias beyond binary gender by utilizing ambiguous emotional attitude words and an Emotional Attitude Score (EAS) metric.

**Data Type**: English-Chinese parallel translation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- WinoBias
- BUG

**Resources**:
- [GitHub Repository](https://github.com/pppa2019/ambGIMT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate gender-inclusive translations with ambiguous attitude words and assess gender bias in machine translation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Machine Translation

**Limitations**: Limited to a single translation language pair (English-Chinese) and does not include all possible non-binary pronoun usages.

## 💾 Data

**Source**: Authentic and synthesized English sentences with ambiguous attitude words and expert Chinese translations.

**Size**: 3,116 examples

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- COMET
- BLEU Score

**Calculation**: Metrics calculated by comparing the translation outputs against reference translations using COMET and BLEU scores.

**Interpretation**: Higher scores indicate better translation quality, while lower scores reflect poorer performance, specifically assessing gender bias.

**Baseline Results**: The experimental results show up to 10 COMET points lower for non-binary identities compared to binary gender contexts.

**Validation**: Evaluated through human judgment and consistency checks (Kappa coefficient > 0.8).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark covers 14 types of non-binary gender identities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
