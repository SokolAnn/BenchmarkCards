# Public Affairs Layout (PAL) database

## 📊 Benchmark Details

**Name**: Public Affairs Layout (PAL) database

**Overview**: A publicly available dataset for Document Layout Analysis in the public affairs / legal domain, collected from 24 official Spanish Administration sources. The database provides semi-automatically annotated layout components (images, tables, links, text blocks) and 4 semantic text categories, and includes pre-processed cleaned text for NLP pre-training and domain adaptation. The database comprises 37.9K documents, 441.3K pages, and more than 8M layout labels.

**Data Type**: text (pre-processed text blocks), image (page images), tabular (extracted tables), layout annotations (bounding boxes and labels)

**Domains**:
- Natural Language Processing
- Legal
- Public Affairs

**Languages**:
- Spanish
- Basque
- Catalan
- Galician
- Valencian

**Similar Benchmarks**:
- PubLayNet
- ICDAR datasets
- UW III
- UNLV

**Resources**:
- [GitHub Repository](https://github.com/BiDAlab/PALdb)
- [GitHub Repository](https://github.com/euske/pdfminer)
- [Resource](https://pymupdf.readthedocs.io/en/latest/)
- [Resource](https://pypi.org/project/camelot-py/)
- [Resource](https://scrapy.org/)
- [Resource](https://arxiv.org/abs/2306.10046)

## 🎯 Purpose and Intended Users

**Goal**: Provide a publicly available database for Document Layout Analysis in the public affairs / legislative (legal) domain with semi-automatic annotations of layout blocks and semantic text categories, and to supply pre-processed text suitable for NLP pre-training and domain adaptation.

**Tasks**:
- Document Layout Analysis
- Text Classification
- Layout Component Detection

**Limitations**: Dataset contains only PDF native (digital-born) documents; scanned-image PDFs were filtered out and left out of the scope. Feature extraction is limited to information present in the PDF structure and thus depends on the PDF editor/format. Tables can remain difficult to detect depending on PDF structure.

**Out of Scope Uses**:
- Processing scanned (image) PDF documents (scanned-image PDFs were excluded from this work)

## 💾 Data

**Source**: 24 public sources (official gazettes) from the Spanish Administration: 3 national administrations, 19 regional administrations, and 2 local administrations (full list in Appendix Table A1).

**Size**: 37,910 documents; 441.3K document pages; 138.1M tokens; layout components: 1M images; 118.7K tables; 14.4K links; 7.1M text blocks. (Train set: 36,466 documents, 422K pages, 130.5M tokens, 1.1M images, 145.2K tables, 16.3K links, 8.8M text blocks.)

**Format**: Native PDF files (input); annotated PDF versions with layout information; tables extracted into pandas DataFrame / CSV; layout feature files (format not explicitly specified).

**Annotation**: Semi-automatic: initialization via heuristic rules applied to extracted features, validated and corrected by a single human supervisor, then per-source Random Forest classifiers trained on validated documents and used in an iterative human-in-the-loop curation process.

## 🔬 Methodology

**Methods**:
- Heuristic rule-based annotation (initialization)
- Human-in-the-loop annotation / manual validation by a human supervisor
- Machine learning classification (Random Forest) trained per data source
- Train/test splitting at document level (80% train / 20% test)
- 10-fold Cross Validation (reported as mean ± std over protocol); experiments repeated 10 times with arbitrary splits

**Metrics**:
- Accuracy (overall and per-class)

**Calculation**: Accuracy reported as mean and standard deviation. Experiments used an 80%/20% train/test split of the validation set at document level; per-source evaluations repeated 10 times with arbitrary train/test splits and reported mean/std. A 10-fold Cross Validation protocol is referenced for reporting mean/std.

**Interpretation**: Higher Accuracy indicates effective discrimination of the defined text categories. Identifier class obtained mean accuracies over 99% in most sources; Body class achieved mean accuracies over 95%; Title class showed lower/subjective performance (mean >84%) due to labeling subjectivity and confusion with Body.

**Baseline Results**: Per-source Random Forest classifier overall accuracies reported in Table 3 range from 93.37% (Source 16) to 99.93% (Source 20). Identifier class accuracies exceed 99% in most sources; Body class means exceed 95%; Title class mean accuracies around or above 84%, with 19 sources >90%.

**Validation**: Initial heuristic-labeled documents were validated and corrected by a unique human supervisor to produce validated documents per source. These validated documents were used to train per-source Random Forest classifiers; classifier outputs were iteratively validated/corrected by the human supervisor to expand the validated set. Performance evaluated via per-source train/test splits at document level and cross-validation as described.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
