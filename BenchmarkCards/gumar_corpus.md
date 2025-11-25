# Gumar Corpus

## 📊 Benchmark Details

**Name**: Gumar Corpus

**Overview**: A large-scale corpus of Gulf Arabic consisting of 110 million words from 1,200 forum novels. The corpus is annotated for sub-dialect information at the document level. The paper also presents a preliminary study in the morphological annotation of Gulf Arabic including developing guidelines for a conventional orthography. The text of the corpus is publicly browsable through a web interface.

**Data Type**: text (forum novels / long conversational novels in Gulf Arabic)

**Domains**:
- Natural Language Processing

**Languages**:
- Gulf Arabic
- Modern Standard Arabic

**Similar Benchmarks**:
- Emirati Arabic Corpus (EAC)
- Emirati Arabic Language Acquisition Corpus (EMALAC)
- CALLHOME Egyptian Arabic (CHE) corpus
- YADAC
- Levantine Arabic Treebank (LATB)
- Curras corpus
- COLABA
- Tharwa
- Multidialectal parallel Arabic corpus
- Arabic Online Commentary Dataset

**Resources**:
- [Resource](https://arxiv.org/abs/1609.02960)
- [Resource](http://www.graaam.com)
- [Resource](http://camel.abudhabi.nyu.edu/gumar/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale corpus of Gulf Arabic annotated for sub-dialect information and to present preliminary morphological annotation and orthography guidelines to support NLP applications for Gulf Arabic.

**Target Audience**:
- ML Researchers
- Model Developers
- Computational Linguists
- Domain Experts in Arabic dialects

**Tasks**:
- Dialect Identification
- Morphological Annotation
- Part-of-Speech Tagging
- Lemma Extraction
- Corpus Search and Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Automatically collected from approximately 1,200 MS Word documents of online forum novels (source example: www.graaam.com).

**Size**: 112,410,688 words; 9,335,224 sentences; 1,236 documents

**Format**: MS Word documents (original collection); corpus text stored in a relational database for the web interface.

**Annotation**: Document-level annotations: sub-dialect (dialect), novel name, writer name. Preliminary manual morphological annotation of around 4,000 words from four novels following extended CODA orthography and morphology guidelines. Annotated features include word orthography, morphemic tokenization, Part-of-Speech (MADAMIRA POS and CATiB POS), lemma (diacritized form), and English gloss.

## 🔬 Methodology

**Methods**:
- Automated web harvesting of MS Word forum novels
- Document-level manual annotation for dialect, novel name, and writer name
- Semi-automatic morphological annotation using MADAMIRA (MSA and EGY modes) followed by manual corrections
- Extension of Conventional Orthography for Dialectal Arabic (CODA) to Gulf Arabic
- Evaluation by comparing manual gold annotations to MADAMIRA outputs and manual error analysis

**Metrics**:
- Accuracy (for word orthography, morphemic tokenization, POS, CATiB POS, and lemma)
- Out-of-vocabulary (OOV) rate

**Calculation**: Accuracy calculated by comparing manual gold annotations (~4,000 words) against MADAMIRA outputs for word orthography, morphemic tokenization, POS, CATiB POS and lemma. OOV rate measured as percentage of words not found in model vocabulary for each MADAMIRA mode.

**Interpretation**: Higher accuracy indicates better alignment of automatic annotations with the gold standard; MADAMIRA-EGY outperforms MADAMIRA-MSA by 4–13% absolute on evaluated metrics, indicating MADAMIRA-EGY is a better baseline for Gulf Arabic. Lower OOV rate indicates better vocabulary coverage (MADAMIRA-EGY OOV 5.6% vs MADAMIRA-MSA OOV 9.3%).

**Baseline Results**: MADAMIRA-MSA vs MADAMIRA-EGY (Accuracy %): CODA 83.81 vs 88.34; Morph 76.16 vs 83.62; POS 72.37 vs 80.39; CATiB 76.28 vs 81.51; Lemma 64.03 vs 77.02. OOV rates: MADAMIRA-EGY 5.6%, MADAMIRA-MSA 9.3%.

**Validation**: Manual gold annotation of around 4,000 words from four novels used for evaluation. Additional error analysis performed on a 400-word sample (four sets of 100 words) to identify error sources.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Distribution of dialects across the corpus: SA 60.52%; AE 13.35%; KW 5.91%; OM 1.13%; QA 0.65%; BH 0.49%; GA (other) 10.03%; Arabic (other, including MSA and other dialects) 7.93%.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Writers are anonymous under pen names and no real names are used; some authors ask to be credited if the novel is transferred to another forum.

**Data Licensing**: No copyright claims by the anonymous writers or organizers; authors state they do not claim any copyrights to the text. (Specific license not specified in the paper.)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
