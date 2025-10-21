# GlossLM (A Massively Multilingual Corpus and Pretrained Model for Interlinear Glossed Text)

## 📊 Benchmark Details

**Name**: GlossLM (A Massively Multilingual Corpus and Pretrained Model for Interlinear Glossed Text)

**Overview**: We compile the largest existing corpus of Interlinear Glossed Text (IGT) data from a variety of sources, covering over 450k examples across 1.8k languages, to enable research on crosslingual transfer and IGT generation.

**Data Type**: interlinear glossed text instances

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/collections/lecslab/glosslm-66da150854209e910113dd87)

## 🎯 Purpose and Intended Users

**Goal**: To aid in language documentation, preservation, and research by providing a large corpus of normalized IGT data and a pretrained model for automatic IGT generation.

**Target Audience**:
- Linguists
- NLP Researchers
- Language Documenters

**Tasks**:
- Automatic Gloss Generation
- Crosslingual Transfer

**Limitations**: N/A

## 💾 Data

**Source**: Compiled from six different IGT corpora including ODIN, SIGMORPHON, IMTVault, APICS, UraTyp, and Guarani Corpus.

**Size**: 450,000 instances

**Format**: Raw text files

**Annotation**: Data is normalized to follow a standard set of labels across languages.

## 🔬 Methodology

**Methods**:
- Pretraining on a large multilingual corpus
- Fine-tuning on monolingual corpora

**Metrics**:
- Morpheme Accuracy
- Word Accuracy
- chrF++ Score

**Calculation**: Metrics are calculated as the number of correct glosses in the correct position compared to the gold standard.

**Interpretation**: Higher scores indicate better performance with respect to generating accurate glosses.

**Baseline Results**: Comparisons made against various state-of-the-art models including TOP-CHOICE, TOKEN-CLASS, and TÜ-CL models.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
