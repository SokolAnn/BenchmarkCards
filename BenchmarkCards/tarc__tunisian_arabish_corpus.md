# TArC: Tunisian Arabish Corpus

## 📊 Benchmark Details

**Name**: TArC: Tunisian Arabish Corpus

**Overview**: The paper presents the final result of a project on Tunisian Arabic encoded in Arabizi (Latin-based writing system) that produced two integrated resources: a corpus (TArC) and an NLP tool to annotate the corpus with multiple levels of linguistic information (word classification, transliteration, tokenization, POS-tagging, lemmatization). The corpus was created via a semi-automatic iterative annotation procedure using a neural multi-task architecture and manual correction.

**Data Type**: text (Tunisian Arabizi sentences with token-level annotations: token classification, transliteration into CODA script, tokenization, POS-tagging, lemmatization)

**Domains**:
- Natural Language Processing
- Linguistics
- Computational Linguistics

**Languages**:
- Tunisian Arabic

**Similar Benchmarks**:
- MADAR
- TuDiCoI
- STAC
- LETD
- TLD
- TAD
- TSAC
- PADIC
- MADAR CODA

**Resources**:
- [Resource](https://gricad-gitlab.univ-grenoble-alpes.fr/dinarelm/tarc-multi-task-system/)
- [GitHub Repository](https://github.com/eligugliotta/tarc)
- [Resource](https://arxiv.org/abs/2207.04796)

## 🎯 Purpose and Intended Users

**Goal**: To create a multi-level annotated corpus of Tunisian Arabic encoded in Arabizi (TArC) and an accompanying neural annotation tool to produce token classification, transliteration (CODA), tokenization, POS tags, and lemmatization for computational and linguistic research.

**Target Audience**:
- Natural Language Processing researchers
- Linguists

**Tasks**:
- Token Classification
- Transliteration
- Tokenization
- Part-of-Speech Tagging
- Lemmatization

**Limitations**: The authors explicitly state they concentrated on a reduced amount of data to focus on methodology; the corpus size is limited and they plan to increase the size by exploiting TArC as a gold standard.

## 💾 Data

**Source**: Collected from Digital Networked Writing environments: social networks, forums, blogs, and rap song lyrics (lyrics used for comparison between Arabizi and Arabic script). Additionally, the MADAR parallel corpus was annotated/used to extend training data.

**Size**: 4,797 sentences; 43,327 words

**Format**: N/A

**Annotation**: Semi-automatic iterative annotation using a neural multi-task sequence-to-sequence architecture with manual correction and incremental retraining (split into blocks, auto-annotate, manual correction, add to training data, retrain).

## 🔬 Methodology

**Methods**:
- Semi-automatic iterative annotation (model annotation + manual correction)
- Neural multi-task sequence-to-sequence annotation (multi-decoder architecture)
- Automated evaluation using Accuracy

**Metrics**:
- Accuracy

**Calculation**: Accuracy reported as percentage of correct predictions for each annotation level (classification, transliteration, tokenization, POS, lemmatization) on development/test splits. Data splits created by random shuffle at sentence level with 70/15/15 ratios per genre then concatenated.

**Interpretation**: Higher Accuracy indicates better annotation/model performance. The authors report that transliteration from Arabizi to CODA is the most difficult task; LSTM-based models outperform Transformer-based models on this (small) dataset.

**Baseline Results**: Final reported results (examples): Final Step global-split (42,559 train tokens, 30,168 from TArC): Classification 97.14%, Transliteration (Ar) 82.34%, Tokenization 81.45%, POS 80.95%, Lemmatization 80.48%. Final Step 2xlstm input:Ar (42,559 train tokens): Classification 98.77%, Lemmatization 92.40%, Tokenization 96.74%, POS 85.90%.

**Validation**: Data split into training, development and test with 70/15/15 ratios per genre then concatenated; iterative manual correction of auto-annotations and retraining across annotation blocks used to validate and improve annotations.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data and code are stated as freely available by the authors; specific license type is not specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
