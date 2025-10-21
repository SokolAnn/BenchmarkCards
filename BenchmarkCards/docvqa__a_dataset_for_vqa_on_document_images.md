# DocVQA: A Dataset for VQA on Document Images

## 📊 Benchmark Details

**Name**: DocVQA: A Dataset for VQA on Document Images

**Overview**: We present a new dataset for Visual Question Answering (VQA) on document images called DocVQA. The dataset consists of 50,000 questions defined on 12,000+ document images. The benchmark is intended to drive document image understanding by requiring systems to read text and exploit layout, non-textual elements and style to answer natural language questions on document images.

**Data Type**: document images with question-answering pairs (image + QA)

**Domains**:
- Document Analysis and Recognition
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- VQA 2.0
- ST-VQA
- TextVQA
- SQuAD 1.1
- OCR-VQA
- DVQA
- FigureQA
- TQA

**Resources**:
- [Resource](https://docvqa.org)
- [Resource](https://www.industrydocuments.ucsf.edu/)
- [Resource](https://arxiv.org/abs/2007.00398)
- [GitHub Repository](https://github.com/facebookresearch/mmf)
- [Resource](https://huggingface.co/transformers/)

## 🎯 Purpose and Intended Users

**Goal**: Introduce DocVQA, a large scale dataset and associated VQA task on document images to drive purpose-driven Document Analysis and Recognition research and to evaluate methods that combine textual and visual/layout cues for answering natural language questions on documents.

**Target Audience**:
- Document Analysis and Recognition researchers

**Tasks**:
- Visual Question Answering
- Question Answering
- Extractive Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Pages from documents in the UCSF Industry Documents Library (documents drawn from 6,071 industry documents spanning tobacco, food, drug, fossil fuel and chemical collections).

**Size**: 50,000 questions over 12,767 images (pages drawn from 6,071 documents). Train: 39,463 questions, 10,194 images; Validation: 5,349 questions, 1,286 images; Test: 5,188 questions, 1,287 images.

**Format**: N/A

**Annotation**: Crowdsourced annotation by remote workers using a three-stage process: (1) workers author up to 10 question-answer pairs per image, (2) verification stage where different workers answer and assign question types and can flag invalid/ambiguous questions, (3) author review of disagreement cases (authors review and edit/accept questions).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Baseline model evaluation (heuristics, VQA models, reading comprehension models)

**Metrics**:
- Average Normalized Levenshtein Similarity (ANLS)
- Accuracy

**Calculation**: ANLS is used as the primary evaluation metric (originally proposed for ST-VQA) to reduce penalization from minor mismatches due to OCR errors by averaging normalized Levenshtein similarities. Accuracy measures the percentage of questions for which the predicted answer matches exactly any target answer.

**Interpretation**: ANLS is the preferred metric to account for OCR-induced minor mismatches; Accuracy is a strict exact-match metric that gives zero for even small differences between prediction and target.

**Baseline Results**: Human performance on test: Accuracy 94.36% (ANLS 0.981). Heuristics and upper bounds on test: Random answer Accuracy 0.00 (ANLS 0.003), Random OCR token Accuracy 0.58 (ANLS 0.014), Majority answer Accuracy 0.89 (ANLS 0.017), Vocab UB Accuracy 33.78, OCR substring UB Accuracy 87.00, OCR subsequence UB Accuracy 77.00. VQA baselines on test: LoRRA best ~ANLS 0.112 Acc 7.63; M4C best (dynamic vocab 500) ANLS 0.391 Acc 24.81. BERT QA baselines on test: bert-large-squad finetuned on DocVQA ANLS 0.665 Acc 55.77 (best reported baseline).

**Validation**: Data split randomly into train/validation/test with an 80/10/10 ratio. Human performance collected on the test split using volunteers. OCR tokens for experiments were extracted using a commercial OCR application.

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
