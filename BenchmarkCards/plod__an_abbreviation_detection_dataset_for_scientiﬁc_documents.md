# PLOD: An Abbreviation Detection Dataset for Scientiﬁc Documents

## 📊 Benchmark Details

**Name**: PLOD: An Abbreviation Detection Dataset for Scientiﬁc Documents

**Overview**: This paper presents PLOD, a large-scale dataset for abbreviation detection and extraction that contains 160k+ segments automatically annotated with abbreviations and their long forms.

**Data Type**: text (annotated segments with abbreviations and corresponding long-form span annotations)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MACRONYM
- SDU@AAAI-22 Shared Task

**Resources**:
- [Resource](https://plos.org/)
- [Resource](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/)
- [Resource](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/)
- [Resource](https://arxiv.org/abs/2204.12061)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale dataset for the detection and extraction of short (abbreviations) and long forms in scientific documents, and to release baseline models and code for abbreviation detection.

**Target Audience**:
- NLP Researchers
- Computational Linguistics researchers
- Model Developers

**Tasks**:
- Abbreviation Detection
- Acronym Extraction
- Sequence Labeling
- Named Entity Recognition

**Limitations**: Dataset is mainly focused on the Biomedical domain; 26.7% of sampled segments had missing annotation and 5.5% had wrong annotation in a sampled analysis; one-character abbreviations were filtered out which removed 705 unique long forms (3,877 occurrences); some long forms and abbreviations were found to be incorrectly formed and were removed during validation.

## 💾 Data

**Source**: Open access articles from PLOS journals (PMC Open Access Subset via NCBI FTP), extracted from XML articles' "Abbreviations" sections and <p> text.

**Size**: Final PLOD Filtered Dataset: 160,932 annotated segments; 449,266 annotated abbreviations; 266,351 annotated long forms. Raw corpus: 305,445 files (31GB); Research Articles used: 283,874 files.

**Format**: Source articles in XML; released dataset in I-O-B (IOB) formatted training files and TSV.

**Annotation**: Automatically annotated by matching abbreviations from each article's "Abbreviations" section to text segments and recording character indexes; annotated with I-O-B scheme (B-AB for abbreviations, B-LF/I-LF for long-form tokens). Validation included manual sampling checks, spaCy-based language-model heuristics, length-based filters, and removal of erroneous entries.

## 🔬 Methodology

**Methods**:
- Extrinsic evaluation via fine-tuning pre-trained transformer models (spaCy v3.2 NER pipeline with spaCy-transformers)
- Sequence labeling (IOB token-level tagging)

**Metrics**:
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Accuracy

**Calculation**: Token-level sequence-labeling evaluation: predicted I-O-B tags evaluated against gold I-O-B annotations to compute Precision, Recall, and F1 for abbreviations (B-AB) and long forms (B-LF/I-LF) on held-out test splits (70% train, 15% dev, 15% test).

**Interpretation**: Higher Precision/Recall/F1 indicate better detection of abbreviations and long forms. Authors report RoBERTa variants as top-performing; performance drops when testing on out-of-domain/shared-task data indicating domain sensitivity.

**Baseline Results**: Best reported results: F1-score ≈ 0.92 for abbreviations and ≈ 0.89 for long forms (e.g., RoBERTa large: Abbreviations F1=0.922 on PLOD unfiltered; RoBERTa large Long-forms F1≈0.898).

**Validation**: Validation steps included manual inspection of random samples (500 and 1,000 samples), spaCy-based language-model heuristics to detect oddly formed long forms, length-based filtering of excessively long abbreviations/long-forms, removal of one-character abbreviations, and reporting of error rates (e.g., 5.5% wrong annotation, 26.7% missing annotation in a 1,000-sample analysis).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
