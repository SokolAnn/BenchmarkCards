# TAT-DQA

## 📊 Benchmark Details

**Name**: TAT-DQA

**Overview**: A new Document Visual Question Answering (VQA) dataset named TAT-DQA that consists of visually-rich multi-page business documents (tabular + textual) sampled from financial reports, containing 3,067 document pages and 16,558 question-answer pairs. The dataset emphasizes discrete reasoning (counting, comparison, addition, subtraction, multiplication, division and their compositions) over documents and is intended to facilitate research on understanding visually-rich documents requiring discrete reasoning.

**Data Type**: question-answer pairs (multimodal: document images, extracted text with layout/bounding boxes; includes tabular and textual content)

**Domains**:
- Natural Language Processing
- Computer Vision
- Finance

**Similar Benchmarks**:
- TAT-QA
- DocVQA
- VisualMRC

**Resources**:
- [Resource](https://nextplusplus.github.io/TAT-DQA/)
- [Resource](https://doi.org/10.1145/3503161.3548422)
- [Resource](https://arxiv.org/abs/2207.11871v3)
- [Resource](https://www.annualreports.com/)
- [Resource](https://pdfbox.apache.org/)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate research on deep understanding of complex real-world visually-rich documents (documents containing both tables and text), especially scenarios that require discrete reasoning.

**Target Audience**:
- Researchers

**Tasks**:
- Question Answering (Document Visual Question Answering)
- Discrete Reasoning
- Document Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Built upon the previous TAT-QA dataset: question-answer pairs borrowed from TAT-QA and extended/cleaned by human experts in finance; document pages filtered from raw financial reports downloaded from https://www.annualreports.com/ (file names provided by TAT-QA authors); text and bounding boxes extracted using Apache PDFBox for readable PDFs or a commercial OCR engine.

**Size**: 16,558 question-answer pairs; 2,758 documents; 3,067 document pages; from 182 financial reports; splits: train 13,251 questions, dev 1,645 questions, test 1,662 questions.

**Format**: Document page images and extracted text with bounding boxes (as extracted by Apache PDFBox or commercial OCR); each document page converted to a list of text blocks and words with bounding boxes.

**Annotation**: Question-answer pairs and derivations generated and/or verified by human experts in finance; answers labeled with four types (Span, Spans, Counting, Arithmetic); derivations for Counting and Arithmetic questions retained in same format as TAT-QA.

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match and numeracy-focused macro-averaged F1)
- Baseline model comparison (NumNet+ V2, TagOp)
- Human expert evaluation (reported human expert performance)

**Metrics**:
- Exact Match (EM)
- Numeracy-focused macro-averaged F1 (numeracy-focused F1 is set to 0 unless the predicted number multiplied by the predicted scale equals exactly the ground truth)

**Calculation**: Both Exact Match and numeracy-focused macro-averaged F1 measure overlap between a bag-of-words representation of the gold and predicted answers. The numeracy-focused F1 is set to 0 unless the predicted number multiplied by the predicted scale equals exactly the ground truth.

**Interpretation**: Higher EM and numeracy-focused F1 indicate better performance. The authors report that model performance still lags far behind expert human performance on the dataset.

**Baseline Results**: Test set results: Human Experts EM 84.1 F1 90.8; NumNet+ V2 EM 30.6 F1 40.1; TagOp EM 33.7 F1 42.5; MHST (RoBERTa LARGE) EM 39.8 F1 47.6; MHST (LayoutLMv2 LARGE) EM 41.5 F1 50.7.

**Validation**: Documents and Q-A pairs randomly split into train/dev/test with ratios 80%/10%/10%; all questions about a particular document belong to only one split. Q-A pairs were generated and validated by human experts and erroneous pairs removed during data preparation.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
