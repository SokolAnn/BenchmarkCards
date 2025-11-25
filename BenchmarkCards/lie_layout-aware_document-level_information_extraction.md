# LIE (Layout-aware document-level Information Extraction)

## 📊 Benchmark Details

**Name**: LIE (Layout-aware document-level Information Extraction)

**Overview**: A layout-aware document-level information extraction dataset (LIE) to facilitate extracting both structural and semantic knowledge from visually rich documents (VRDs) to generate accurate responses in document-grounded dialogue systems. LIE contains 62k annotations of three extraction tasks from 4,061 pages in product and official documents.

**Data Type**: multimodal (text tokens with 2D layout bounding boxes and PDF documents)

**Domains**:
- Natural Language Processing
- Finance
- Government

**Languages**:
- Chinese

**Similar Benchmarks**:
- CORD
- SROIE
- FUNSD
- EPHOIE
- DocRED
- doc2dial

**Resources**:
- [Resource](https://arxiv.org/abs/2207.06717)
- [GitHub Repository](https://github.com/jsvine/pdfplumber)

## 🎯 Purpose and Intended Users

**Goal**: To enable extraction of structural (hierarchy and section) and relational fact knowledge from multi-page visually rich documents to support downstream document-grounded dialogue systems.

**Tasks**:
- Hierarchy Extraction
- Section Extraction
- Relation Extraction

**Limitations**: About 2% of annotation instances could not be aligned to parsed tokens and were discarded due to parsing errors.

## 💾 Data

**Source**: Chinese product documents in PDF format downloaded from portal websites of the insurance sector and official documents issued by government departments collected via web search engines.

**Size**: 4,061 pages from 400 documents (200 product documents and 200 official documents); 62,000 annotations across three IE tasks.

**Format**: PDF files and token-level annotations with bounding box coordinates (x0,y0,x1,y1) per token (provided after parsing).

**Annotation**: Crowdsourced annotation by 20 annotators with linguistic knowledge; each instance labeled by at least two annotators, disagreements resolved by a third annotator; annotators passed trial annotation; random checks performed and annotator results reviewed if document-level accuracy < 95%; approximately 2% of annotation instances discarded due to parsing alignment errors. Pre-defined relation schemes: 18 relations for product documents and 15 relations for official documents.

## 🔬 Methodology

**Methods**:
- Automated metrics-based evaluation
- Model-based evaluation (comparisons between BERT, LayoutBERT variants, LayoutLMv2)
- Sequence labeling evaluation (task-specific tagging schemes and decoding)

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Precision and recall defined as P = S_m / |P| and R = S_m / |G| where S_m is the matching score. For hierarchy extraction and relation extraction, S_m is the count of strictly matching predicted results. For section extraction, S_m is computed by computing pairwise similarities between predicted and ground-truth facts using a gestalt pattern matching measure and finding the optimal matching via a linear assignment to maximize matched similarities; similarity between two facts is the average of the gestalt matching scores of their elements.

**Interpretation**: Evaluation uses F1 (the harmonic mean of precision and recall). Results are interpreted comparatively across models (higher F1 indicates better performance); the paper reports relative improvements of layout-aware models and pre-training over baselines. No absolute performance thresholds are provided.

**Baseline Results**: BERT (baseline) average results — Hierarchy Extraction F1: 73.6 (Product 75.9, Official 71.2); Section Extraction F1: 75.4 (Product 80.2, Official 70.5); Relation Extraction F1: 62.1 (Product 52.3, Official 71.9). LayoutBERT (w/ MLLM, PHS) average results — Hierarchy Extraction F1: 77.4 (Product 78.3, Official 76.5); Section Extraction F1: 79.2 (Product 85.1, Official 73.2); Relation Extraction F1: 65.5 (Product 54.2, Official 76.7). LayoutLMv2 reported comparable or lower results on these tasks.

**Validation**: Official dataset partition provided with train/dev/test split ratio 6:2:2 (statistics reported in Table 2). Annotation quality control: dual annotation with third-annotator adjudication for disagreements, random checks, and reviewer re-checks if annotator document-level accuracy < 95%. Pre-training corpus: 100k additional pages from 10k in-domain documents used for in-domain pre-training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
