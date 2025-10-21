# VRDU (Visually-rich Document Understanding)

## 📊 Benchmark Details

**Name**: VRDU (Visually-rich Document Understanding)

**Overview**: We identify the desiderata for a more comprehensive benchmark and propose one we call Visually Rich Document Understanding (VRDU). VRDU contains two datasets that represent several challenges: rich schema including diverse data types as well as hierarchical entities, complex templates including tables and multi-column layouts, and diversity of different layouts (templates) within a single document type. We design few-shot and conventional experiment settings along with a carefully designed matching algorithm to evaluate extraction results. We open-source the dataset with high-quality OCR results and annotations and an evaluation toolkit with a type-aware matching algorithm.

**Data Type**: multimodal (document images and OCR text with token-level annotations and bounding boxes)

**Domains**:
- Natural Language Processing
- Computer Vision
- Procurement
- Finance
- Insurance
- Retail
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- FUNSD
- CORD
- SROIE
- Kleister-NDA
- Kleister-Charity
- DeepForm

**Resources**:
- [GitHub Repository](https://github.com/google-research/google-research/tree/master/vrdu)
- [Resource](https://doi.org/10.1145/3580305.3599929)
- [Resource](https://publicfiles.fcc.gov)
- [Resource](https://www.justice.gov)
- [Resource](https://cloud.google.com/vision/docs/ocr)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive public benchmark for extracting structured information from visually-rich documents that reflects practical challenges (rich schema, layout complexity, template diversity, high-quality OCR, token-level annotation), and to evaluate template generalization, few-shot learning, and hierarchical entity extraction.

**Target Audience**:
- Academic researchers
- Industry practitioners
- Model developers

**Tasks**:
- Information Extraction
- Token-level Sequence Labeling (BIO tagging)
- Hierarchical Entity Extraction
- Single Template Learning (STL)
- Mixed Template Learning (MTL)
- Unseen Template Learning (UTL)

**Limitations**: N/A

**Out of Scope Uses**:
- Evaluating OCR robustness under challenging image artifacts (the benchmark uses high-quality OCR and explicitly states the focus is not on challenging OCR scenarios)

## 💾 Data

**Source**: Two datasets collected from public sources: Ad-buy Forms crawled from the Federal Communications Commission (FCC) and Registration Forms crawled from Foreign Agents Registration Act (FARA) documents (U.S. Department of Justice).

**Size**: Ad-buy Forms: 641 documents; Registration Forms: 1,915 documents.

**Format**: N/A

**Annotation**: Manual annotation by human annotators (30 annotators) with expert review (3 experts). Token-level annotations with bounding boxes, token indices, entity category labels, BIO-style token labeling and hierarchical grouping for hierarchical entities. Annotators drew bounding boxes and experts reviewed and corrected annotations.

## 🔬 Methodology

**Methods**:
- Automated metrics (micro-F1 and macro-F1)
- Type-aware fuzzy matching algorithm (entity-type-specific matching functions)
- Few-shot and conventional experimental settings with prescribed train/validation/test splits
- Evaluation on three task settings: Single Template Learning, Mixed Template Learning, Unseen Template Learning

**Metrics**:
- Micro-F1
- Macro-F1
- F1 Score (reported as micro and macro)

**Calculation**: Predictions are compared to ground-truth using a type-aware fuzzy matching algorithm that applies entity-type-specific matching functions (e.g., numeric conversion for price values, standardized date parsing for date strings) before computing F1 scores. Both micro-F1 and macro-F1 are reported.

**Interpretation**: Micro-F1 weighs every instance equally (instance-level performance) while macro-F1 averages F1 across entity types. Lower micro-F1 relative to macro-F1 on Ad-buy Forms indicates poor performance on hierarchical/repeated entities. Higher scores indicate better extraction performance; differences across tasks (STL/MTL/UTL) measure template generalization.

**Baseline Results**: The paper reports baseline results for LayoutLM, LayoutLMv2, LayoutLMv3, and FormNet across tasks and training sizes (|D| = 10, 50, 100, 200). Example results at |D|=200: Registration Form (Single Template) micro-F1 — LayoutLM: 90.47, LayoutLMv2: 91.41, LayoutLMv3: 90.89, FormNet: 92.12. Registration Form (Unseen Template) micro-F1 — LayoutLM: 70.47, LayoutLMv2: 72.03, LayoutLMv3: 62.58, FormNet: 77.29. Ad-buy Form (Mixed Template) micro-F1 at |D|=200 — LayoutLM: 44.66, LayoutLMv2: 46.54, LayoutLMv3: 45.16, FormNet: 43.23. (All numbers taken from Table 4 in the paper.)

**Validation**: Prescribed dataset splits include 300 documents in the testing set for each task. For training, four sizes are provided (10, 50, 100, 200). Under each setting, three training sets with different random seeds are built and reported results are the average over the three runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data are public documents from FCC and FARA; the paper notes that documents with sensitive information often cannot be released publicly and such documents are kept in-house. No anonymization procedures are described.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
