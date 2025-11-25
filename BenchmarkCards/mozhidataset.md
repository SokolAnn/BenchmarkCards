# Mozhidataset

## 📊 Benchmark Details

**Name**: Mozhidataset

**Overview**: Mozhidataset is a public dataset comprising over 1.2 million annotated word images (equivalent to approximately 120 thousand text line images) across 13 Indian languages, introduced to address the lack of public data for Indian language text recognition. The paper also conducts a comprehensive empirical analysis of various CTC-based neural network models across these 13 languages and provides APIs and web-based applications to digitize Indic printed documents.

**Data Type**: image (cropped word and line images with text annotations)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- Assamese
- Bengali
- Gujarati
- Hindi
- Kannada
- Malayalam
- Manipuri
- Marathi
- Oriya
- Punjabi
- Tamil
- Telugu
- Urdu

**Resources**:
- [Resource](https://cvit.iiit.ac.in/usodi/tdocrmil.php)
- [Resource](https://ilocr.iiit.ac.in/fastocr/)
- [Resource](https://bhashini.gov.in/)
- [Resource](https://arxiv.org/abs/2205.06740)

## 🎯 Purpose and Intended Users

**Goal**: Introduce Mozhidataset for printed text recognition in 13 Indian languages, perform an empirical comparison of CTC-based text recognition models across these languages, and provide deployable OCR models, APIs, and web applications to digitize Indic printed documents.

**Target Audience**:
- Startups
- Solution providers
- Researchers
- Model developers

**Tasks**:
- Word Recognition
- Line Recognition
- End-to-End Page OCR

**Limitations**: The dataset predominantly comprises pages from books, resulting in limited font, style, layout, and distortion diversity.

**Out of Scope Uses**:
- Layout analysis and reading order identification

## 💾 Data

**Source**: Mozhidataset: cropped line and word segments with corresponding ground truth text annotations for 13 Indian languages. Only cropped lines are annotated for Urdu (no word annotations for Urdu).

**Size**: Over 1.2 million annotated word images; approximately 120,000 text line images in total; approximately 100,000 word images per language (for each of the 13 languages except Urdu which has only line annotations).

**Format**: N/A

**Annotation**: Text transcriptions (ground truth strings) for each image. Both line-level and word-level annotations are provided; word-level annotations are not provided for Urdu.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (Character Accuracy, Sequence Accuracy, Word Accuracy)
- Page OCR evaluation using ISRI Analytic Tools (modern adaptation)
- Empirical comparison of CTC-based recognition models (Col_RNN, Win_RNN, CNN_only, CRNN) trained per language

**Metrics**:
- Character Accuracy (CA)
- Sequence Accuracy (SA)
- Word Accuracy (WA)
- Character Error Rate (CER)

**Calculation**: Character Accuracy (CA) is computed as CA = (sum_i len(gi) - sum_i LD(li, gi)) / sum_i len(gi) * 100, where LD is Levenshtein distance and len returns string length. Sequence Accuracy (SA) is the percentage of samples with LD(li, gi) = 0. Word Accuracy (WA) is computed using the Longest Common Sub-sequence (LCS) between predicted and ground truth word sequences: WA = sum_i len(LCS(li, gi)) / sum_i len(gi) * 100. Character Error Rate (CER) is 100 - CA.

**Interpretation**: Higher CA, SA, and WA indicate better recognition performance. CER (100 - CA) indicates error rate. SA corresponds to exact-match accuracy (word accuracy) for word recognition.

**Baseline Results**: The paper compares page-level OCR pipelines against public OCR tools Tesseract and Google Cloud Vision OCR. The authors report that their GT Detection+CRNN pipeline outperforms Tesseract and Google Cloud Vision OCR on 8 out of 13 languages. Example (from Table 4): Assamese - Tesseract End-to-End CA 90.0 SA 86.0; Google CA 92.7 SA 91.2; GT Detection+CRNN CA 99.4 SA 97.2.

**Validation**: For each language, line-level data is randomly split into training, validation, and test in an 80:10:10 ratio. For validation, 5% of pages from each book in the train split are randomly selected to ensure validation reflects training pages; the test split comprises pages from different sets of books. The ISRI-based toolkit is used for page OCR evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
