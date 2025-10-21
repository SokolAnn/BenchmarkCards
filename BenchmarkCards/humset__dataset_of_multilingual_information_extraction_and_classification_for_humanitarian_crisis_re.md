# HUMSET: Dataset of Multilingual Information Extraction and Classification for Humanitarian Crisis Response

## 📊 Benchmark Details

**Name**: HUMSET: Dataset of Multilingual Information Extraction and Classification for Humanitarian Crisis Response

**Overview**: HUMSET is a novel multilingual dataset of humanitarian response documents annotated by experts, providing documents in English, French, and Spanish from 2018 to 2021. For each document the dataset provides selected snippets (entries) and multi-label classes for each entry according to a common humanitarian analysis framework, enabling entry extraction and multi-label entry classification research in the humanitarian response domain.

**Data Type**: annotated text snippets (entries) and full text documents

**Domains**:
- Natural Language Processing
- Humanitarian Response

**Languages**:
- English
- French
- Spanish

**Similar Benchmarks**:
- MultiHumES (Yela-Bello et al., 2021)
- CrisisBench (Alam et al., 2021)
- Human-annotated Twitter corpora for crisis-related messages (Imran et al., 2016)

**Resources**:
- [Resource](https://blog.thedeep.io/humset/)
- [GitHub Repository](https://github.com/the-deep/humset)
- [Resource](https://thedeep.io/)
- [Resource](https://datafriendlyspace.org/)
- [Resource](https://app.thedeep.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enable creation of NLP systems for humanitarian response by providing a validated, expert-annotated multilingual dataset of documents with annotated informative snippets and multi-label tags according to humanitarian analysis frameworks.

**Target Audience**:
- ML Researchers
- Model Developers
- Humanitarian response analysts/practitioners

**Tasks**:
- Extractive Summarization (Entry Extraction)
- Multi-label Text Classification (Entry Classification)

**Limitations**: HUMSET is an aggregation of 46 different projects with varying contributions which can introduce implicit bias due to different goals and annotator subjectivity; errors and limitations arise from converting PDF/HTML documents into plain text; HUMSET might contain societal biases and stereotypes and/or over-represent particular demographics or entities.

## 💾 Data

**Source**: Documents collected from publicly-available resources via the DEEP platform: official reports by humanitarian organizations and international and national media articles; entries annotated by humanitarian experts using the DEEP platform and mapped to a common humanitarian analysis framework.

**Size**: 16,857 documents; 148,621 tagged entries; 62 tags; average ~2,000 words per document; average ~65 words per entry

**Format**: N/A

**Annotation**: Manual annotation by humanitarian experts on the DEEP platform; entries selected and mapped to a custom humanitarian analysis framework; multi-label annotations (more than one tag can be assigned to an entry).

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE F1, Precision, F1-score)
- Model-based evaluation (fine-tuning multilingual pre-trained language models such as XLM-R Base and XtremeDistil)
- Heuristic baseline (LEAD4)
- fastText baseline

**Metrics**:
- ROUGE-1 F1
- ROUGE-2 F1
- ROUGE-L F1
- Precision
- F1 Score (macro-averaged for multi-label classification)

**Calculation**: For entry extraction the target text is the concatenation of all relevant entries and the prediction is the concatenation of predicted relevant entries; ROUGE-1/2/L F1 are reported. For classification, per-label threshold tuning is performed on the validation set optimizing macro-average F1; classification metrics reported as Precision and macro-averaged F1.

**Interpretation**: Higher ROUGE F1 indicates better entry extraction; higher Precision and macro F1 indicate better multi-label classification. XLM-R Base outperformed other baselines in reported experiments. Authors present results as strong baselines and note that categories with many tags are particularly challenging.

**Baseline Results**: Entry extraction (ROUGE F1): XLM-R Base R-1=0.42, R-2=0.35, R-L=0.41 (Table 3). Entry classification (macro F1) for XLM-R Base: Sectors F1=0.73, Pillars 1D F1=0.53, Subpillars 1D F1=0.38, Pillars 2D F1=0.63, Subpillars 2D F1=0.40 (Table 2). Other baselines reported include LEAD4, XtremeDistil, fastText, and a random baseline.

**Validation**: Data split into training/validation/test sets with 80%/10%/10% respectively using stratified splitting to maintain label distributions; threshold tuning performed on the validation set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: Authors note HUMSET might contain societal biases and stereotypes and/or over-represent particular demographics or entities and recommend defining, monitoring, and mitigating such biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
