# Emakhuwa-Portuguese Parallel Corpus

## 📊 Benchmark Details

**Name**: Emakhuwa-Portuguese Parallel Corpus

**Overview**: This paper describes the creation of the Emakhuwa-Portuguese parallel corpus, which is a collection of texts for machine translation between the Emakhuwa language and Portuguese, aimed at improving resources for low-resource languages.

**Data Type**: parallel sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese
- Emakhuwa

**Similar Benchmarks**:
- JW300

**Resources**:
- [Resource](https://www.jw.org)
- [Resource](https://www.africanstorybook.org)
- [GitHub Repository](https://github.com/masakhane-io/masakhane-mt)

## 🎯 Purpose and Intended Users

**Goal**: To provide a parallel corpus for Emakhuwa and Portuguese to support machine translation.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Practitioners

**Tasks**:
- Machine Translation

**Limitations**: Further processing and normalization of texts are required.

## 💾 Data

**Source**: Collected from the Jehovah’s Witness website, African Story Book, Universal Declaration of Human Rights, and Mozambican legal documents.

**Size**: 47,415 sentence pairs

**Format**: N/A

**Annotation**: Manual alignment of Portuguese and Emakhuwa sentences

## 🔬 Methodology

**Methods**:
- Neural machine translation model training
- Manual data alignment

**Metrics**:
- BLEU Score

**Calculation**: BLEU score calculations based on parallel sentence pairs.

**Interpretation**: Higher BLEU scores indicate better performance of translation models.

**Baseline Results**: Initial NMT model trained with default OpenNMT configuration shows BLEU scores for translations.

**Validation**: Data splits were assigned for training and test sets at a ratio of 9:1.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
