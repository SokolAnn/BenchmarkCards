# Arabic Parallel Gender Corpus (APGC v2.0)

## 📊 Benchmark Details

**Name**: Arabic Parallel Gender Corpus (APGC v2.0)

**Overview**: We introduce a new parallel corpus for gender identification and rewriting in contexts involving one or two users with independent grammatical gender preferences. The corpus expands on Habash et al. (2019)'s Arabic Parallel Gender Corpus by adding second person targets as well as increasing the total number of sentences over 6.5 times, reaching over 590K words.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- English

**Similar Benchmarks**:
- Arabic Parallel Gender Corpus v1.0

**Resources**:
- [Resource](http://resources.camel-lab.com/)

## 🎯 Purpose and Intended Users

**Goal**: The Arabic Parallel Gender Corpus is intended to aid the research and development of gender identification, controlled text generation, and post-editing rewrite systems to personalize NLP applications.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners
- Model Developers

**Tasks**:
- Gender Identification
- Controlled Text Generation
- Post-Editing

**Limitations**: N/A

## 💾 Data

**Source**: English-Arabic OpenSubtitles 2018 dataset

**Size**: 590,000 words

**Format**: JSON

**Annotation**: Manual annotation by professional linguists

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- BLEU Score

**Calculation**: BLEU scores are calculated for machine translation outputs against the target corpus.

**Interpretation**: Higher BLEU scores indicate better translation performance, reflecting less gender bias towards masculine grammatical preferences.

**Baseline Results**: N/A

**Validation**: The dataset was validated through professional linguistic annotations and quality checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
