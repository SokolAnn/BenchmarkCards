# Text-mined dataset of gold nanoparticle synthesis procedures, morphologies, and size entities

## 📊 Benchmark Details

**Name**: Text-mined dataset of gold nanoparticle synthesis procedures, morphologies, and size entities

**Overview**: We have constructed and made publicly available a dataset of codiﬁed gold nanoparticle synthesis protocols and outcomes extracted directly from the nanoparticle materials science literature using natural language processing and text-mining techniques. This dataset contains 5,154 data records, each representing a single gold nanoparticle synthesis article, filtered from a database of 4,973,165 publications. Each record contains codiﬁed synthesis protocols and extracted morphological information from a total of 7,608 experimental and 12,519 characterization paragraphs.

**Data Type**: text (synthesis and characterization paragraphs; codiﬁed synthesis protocols and morphological/size entities)

**Domains**:
- Materials Science
- Nanotechnology

**Languages**:
- English

**Similar Benchmarks**:
- Text-mined dataset of inorganic materials synthesis recipes
- 35k article nanomaterial dataset (Hiszpanski et al.)
- Web-based nanomaterial database by Yan et al.

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.16614262.v3)
- [GitHub Repository](https://github.com/CederGroupHub/text-mined-aunp-synthesis_public)
- [GitHub Repository](https://github.com/lbnlp/MatBERT)
- [GitHub Repository](https://github.com/ThilinaRajapakse/simpletransformers)
- [Resource](https://solr.apache.org/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate data mining and data-driven understanding of gold nanoparticle synthesis mechanisms by providing an open-source, text-mined dataset of codiﬁed gold nanoparticle synthesis protocols and extracted morphological and size information.

**Target Audience**:
- Materials Science researchers
- Researchers applying data-driven methods to materials synthesis
- Users performing literature review or recipe querying for gold nanoparticle synthesis

**Tasks**:
- Named Entity Recognition
- Information Extraction
- Text Classification (paragraph classification)
- Synthesis recipe extraction
- Morphology and size entity extraction

**Limitations**: The dataset does not contain entity linking (e.g., particle size to specific nanoparticle morphology or morphological entity to synthesis procedure). The synthesis action extraction cannot distinguish constituent steps of seed-mediated syntheses (seed preparation, growth solution, combination). Materials entity recognition does not detect entities that do not contain specific material formulae or chemical names (e.g., 'AuNP seed solution' or 'growth solution' may not be detected). There is currently no way to distinguish extracted morphologies as either the desired target morphology or as incidental mentions. The authors accepted higher precision than recall for some extraction methods to avoid introducing incorrect information.

## 💾 Data

**Source**: Extracted from a materials science publications database of 4,973,165 publications scraped from publisher websites (Elsevier, Wiley, the Royal Society of Chemistry, Nature Publishing Group, the American Institute of Physics, Springer, the American Chemical Society, the American Physical Society, and the Electrochemical Society), parsed and stored in MongoDB; filtered to 5,154 articles containing gold nanoparticle synthesis procedures using regex/tf-idf filtering, paragraph-level classification, and materials entity recognition.

**Size**: 5,154 records (each record = one article); includes 7,608 synthesis paragraphs and 12,519 characterization paragraphs; source database initial size 4,973,165 publications

**Format**: JSON (single JSON file; each top-level list element is a JSON object representing one publication)

**Annotation**: Combination of automated extraction and manual annotation for training data: manual annotation by experts for training sets (e.g., 1,281 synthesis paragraphs annotated for Materials Entity Recognition, 739 paragraphs annotated for synthesis paragraph classification, 299 paragraphs for characterization paragraph classification, 119 characterization paragraphs annotated for MorphER). Extraction for the full dataset performed with NLP/text-mining models and rule-based methods; manual validation performed on selected samples.

## 🔬 Methodology

**Methods**:
- Automated metrics (precision, recall, F1) for extraction models
- Train/validation/test splits (typically 80/10/10) for classifier and NER training
- Manual validation of sample paragraphs and extracted entities
- Rule-based parsing (dependency trees, regex) for quantities and conditions
- Pretrained and fine-tuned transformer models (MatBERT) and BiLSTM-CRF models

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Metrics (F1, precision, recall, accuracy) were calculated on held-out test sets following train/validation/test splits (commonly 80/10/10) for the paragraph classifiers and NER models. Rule-based extraction methods were evaluated via manual validation on sampled paragraphs. Reported metrics for pipeline components are shown in Table 4 of the paper.

**Interpretation**: The authors prioritized higher precision over recall for certain extraction and rule-based methods to avoid introducing incorrect information into the dataset. High precision indicates fewer false positives at the cost of potentially lower completeness (recall).

**Baseline Results**: Selected pipeline metrics (from Table 4): Article filtering regex/tf-idf F1 0.96 (precision 1.00 | recall 0.92); Synthesis paragraph classification (BERT) F1 0.90 (0.96 | 0.85); Characterization paragraph classification (BERT) F1 0.90 (0.93 | 0.87); Materials Entity Recognition (BiLSTM+CRF with MatBERT embeddings) materials 0.95 (0.95 | 0.95), precursors 0.90 (0.89 | 0.91), targets 0.85 (0.86 | 0.83); Morphology Entity Recognition (fine-tuned MatBERT NER) micro average F1 0.87 (0.89 | 0.84); Synthesis actions (BiLSTM Word2Vec) F1 0.89 (0.90 | 0.88); Synthesis conditions rule-based temperature F1 0.94 (0.97 | 0.92), time F1 0.93 (0.98 | 0.89); Material quantities rule-based F1 0.87 (0.90 | 0.85); Seed-mediated tag rule-based accuracy 1.00 (1.00 | 1.00).

**Validation**: Validation procedures included: manual validation on sampled paragraphs and extractions (e.g., 50 seed-mediated tag checks with 49/50 valid), comparison to an external 35k article nanomaterial dataset (Hiszpanski et al.) to evaluate article filtering coverage, and manual validation of rule-based extraction methods on 100 solution-based synthesis paragraphs as reported in related work. Model performance metrics were reported on held-out test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Text and Data Mining agreements with the relevant publishers were obtained (acknowledged assistance in obtaining Text and Data Mining agreements with publishers).
