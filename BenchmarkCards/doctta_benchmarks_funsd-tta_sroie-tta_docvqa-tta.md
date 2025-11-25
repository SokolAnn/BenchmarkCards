# DocTTA benchmarks (FUNSD-TTA, SROIE-TTA, DocVQA-TTA)

## 📊 Benchmark Details

**Name**: DocTTA benchmarks (FUNSD-TTA, SROIE-TTA, DocVQA-TTA)

**Overview**: The paper introduces new adaptation benchmarks for Visual Document Understanding (VDU) by modifying existing public datasets to mimic real-world test-time/source-free adaptation scenarios. The benchmarks target multiple VDU tasks including entity recognition, key-value extraction, and document visual question answering to evaluate test-time adaptation methods such as DocTTA.

**Data Type**: multimodal (document images with OCR-extracted text and layout bounding boxes)

**Domains**:
- Natural Language Processing
- Computer Vision
- Document Understanding

**Similar Benchmarks**:
- FUNSD
- SROIE
- DocVQA

**Resources**:
- [Resource](https://saynaebrahimi.github.io/DocTTA.html)
- [Resource](https://guillaumejaume.github.io/FUNSD/work/)
- [GitHub Repository](https://github.com/zzzDavid/ICDAR-2019-SROIE)
- [Resource](https://www.docvqa.org/datasets/doccvqa)
- [Resource](https://openreview.net/forum?id=zshemTAa6U)

## 🎯 Purpose and Intended Users

**Goal**: To provide realistic test-time/source-free adaptation benchmarks for VDU tasks (entity recognition, key-value extraction, document visual question answering) to evaluate DocTTA and facilitate future research in test-time adaptation for VDU by modifying public datasets to mimic real-world adaptation scenarios.

**Target Audience**:
- Machine Learning Researchers
- Visual Document Understanding researchers
- Model Developers

**Tasks**:
- Named Entity Recognition
- Key-Value Extraction
- Question Answering (Document Visual Question Answering)

**Limitations**: DocVQA does not have public meta-data to easily sort documents into domains; some domain splits have small dataset sizes (e.g., Figures & Diagrams source has 150 training documents), which the authors note can limit evaluation and affect results.

## 💾 Data

**Source**: Benchmarks are constructed from existing public VDU datasets: FUNSD, SROIE, and DocVQA. Source/target splits are created by modifying the original datasets (e.g., splitting by sparsity for FUNSD, by visual appearance for SROIE, and by selected document domains via keyword search for DocVQA). Official OCR annotations provided with the original datasets are used.

**Size**: FUNSD-TTA: Source training 139 documents, Source validation 10 documents, Target 50 documents. SROIE-TTA: Source training 600 documents, Source validation 39 documents, Target 347 documents. DocVQA-TTA: Source training - Layout: 1807 documents, Emails & Letters: 1417 documents, Tables & Lists: 592 documents, Figures & Diagrams: 150 documents; Source validation - Layout: 200, Emails & Letters: 157, Tables & Lists: 65, Figures & Diagrams: 17; Target evaluation counts - Layout: 512, Emails & Letters: 137, Tables & Lists: 187, Figures & Diagrams: 49.

**Format**: Document images (raw), OCR annotations, JSON files for training/validation/test splits, tokenized text (WordPiece) as used by LayoutLMv2

**Annotation**: Uses officially-provided OCR annotations and the original dataset labels (human-labeled annotations) from FUNSD, SROIE, and DocVQA.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Comparative evaluation with baseline adaptation methods (DANN, CDAN, BN, TENT, SHOT)
- Ablation studies

**Metrics**:
- F1 Score (entity-level F1 for entity recognition and key-value extraction)
- Average Normalized Levenshtein Similarity (ANLS) for document VQA
- Expected Calibration Error (ECE) for calibration analysis

**Calculation**: Entity-level F1 is computed for entity recognition and key-value extraction. ANLS is computed as defined in Biten et al. (2019) (Average Normalized Levenshtein Similarity) for DocVQA. ECE is computed as in Naeini et al. (2015) using reliability diagrams and binning.

**Interpretation**: Source-only (model trained on source and evaluated on target without adaptation) serves as a lower bound; train-on-target (model trained and tested on target) serves as an upper bound. Higher F1 and higher ANLS indicate better adaptation performance. ANLS is used because it does not penalize minor OCR text mismatches.

**Baseline Results**: Selected results reported in paper: FUNSD-TTA source-only F1 = 80.80; DocTTA F1 = 84.23; DocUDA F1 = 89.76. SROIE-TTA source-only F1 = 92.45; DocTTA F1 = 94.34; DocUDA F1 = 97.38. DocVQA-TTA reported ANLS improvements include up to +17.68% ANLS (e.g., F→E adaptation) and DocTTA achieves higher ANLS than source-only across many domain pairs (see Tables 1 and 2 in paper).

**Validation**: Hyperparameters tuned on source-domain validation splits (FUNSD: 10 validation documents; SROIE: 39 validation documents; DocVQA: 10% of source domain used for validation). Target labels are only used for final evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Data Laws**: Data usage restrictions

**Potential Harm**: The paper notes reduced stability and reliability due to domain shift which is undesirable for high-stakes applications (finance, insurance, healthcare, legal); privacy concerns from accessing/storing source data in deployment environments are also highlighted.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors note privacy concerns associated with accessing or storing source data in deployment, especially for privacy-sensitive domains (legal, finance). No specific anonymization procedures are described for the introduced benchmarks.

**Data Licensing**: Datasets used are publicly-available and can be downloaded from their original hosts under their original terms and conditions (see provided dataset URLs for license/instructions).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
