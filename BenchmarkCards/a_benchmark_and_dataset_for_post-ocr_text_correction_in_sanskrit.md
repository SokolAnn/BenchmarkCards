# A Benchmark and Dataset for Post-OCR text correction in Sanskrit

## 📊 Benchmark Details

**Name**: A Benchmark and Dataset for Post-OCR text correction in Sanskrit

**Overview**: We release a post-OCR text correction dataset containing around 218,000 sentences (1.5 million words) from 30 different books across multiple domains (e.g., astronomy, medicine, mathematics). We also release multiple strong seq2seq baselines as benchmarks for the task and a 500-image OCR test set with corresponding text for benchmarking OCR systems. Our best-performing baseline (ByT5+SLP1) yields substantial improvements in Word Error Rate and Character Error Rate over the original OCR outputs.

**Data Type**: sentence pairs (OCR output, corrected text); scanned page images with corresponding text (OCR test set)

**Domains**:
- Natural Language Processing
- Computer Vision
- Cultural Heritage

**Languages**:
- Sanskrit

**Resources**:
- [GitHub Repository](https://github.com/ayushbits/pe-ocr-sanskrit)
- [Resource](https://www.cse.iitb.ac.in/~ocr/trained)
- [Resource](https://arxiv.org/abs/2211.07980)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large multi-domain dataset and evaluation benchmarks for post-OCR text correction in Sanskrit and to release an OCR test set for benchmarking OCR systems prior to post-OCR correction.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Computational Linguistics Researchers
- Digital Humanities / Cultural Heritage practitioners

**Tasks**:
- Post-OCR Text Correction
- Optical Character Recognition evaluation

**Limitations**: Major limitation is mispredictions at the word level: of the mispredicted words by the best model (ByT5-SLP1), 71.17% are not valid Sanskrit words. Pretrained models used are not lexically or morphologically aware, and none of the pretrained models employed used Sanskrit during pretraining. This can challenge downstream tasks that rely on rule-based morphological analysis of words.

## 💾 Data

**Source**: Scanned images and OCR outputs from 30 printed Devanāgari books (a subset of 103 books in the digitisation pipeline). Books are from domains including philosophy, literature, mathematics, medicine and astronomy. Texts are manually verified (three-step process: manual correction/post-editing, verification, proofreading) by experts.

**Size**: Train: 208,173 sentences (1,444,913 words); Validation: 5,000 sentences (34,762 words); Test: 5,000 sentences (34,705 words). Total ~218,173 sentences and ~1.5 million words. Vocabulary: 581,445 unique words. OCR test dataset: 500 images with corresponding text.

**Format**: N/A

**Annotation**: Manual correction/post-editing by experts using a three-step process (1. manual correction/post-editing by looking at the scanned image, 2. verification of the corrected text, 3. proofreading). 14 experts contributed to the process (linguists or computational linguists, seven working full time).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Baseline evaluation using seq2seq models (CopyNet, mBART, mT5, ByT5, IndicBART)
- Out-of-domain evaluation

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)

**Calculation**: Metrics reported as macro-averaged Word Error Rate and Character Error Rate.

**Interpretation**: Lower WER and CER indicate better performance (table notes: lower is better).

**Baseline Results**: OCR baseline: CER 3.89%, WER 30.23%. CopyNet: CER 13.25%, WER 50.38%. mBART (Dev): CER 3.50%, WER 26.11%. mT5 (Dev): CER 3.34%, WER 25.57%. IndicBART (Dev): CER 3.55%, WER 25.73%. ByT5 (SLP1): CER 2.98%, WER 23.19% (best reported).

**Validation**: Ensured no sentence-level overlap between train, validation and test splits. Out-of-domain test data from a completely new book (Brihat-samhita) not included in the train/val/test splits; additional out-of-domain test dataset of 500 sentences released and evaluated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Manually verified to have no copyright issues for the books included.
