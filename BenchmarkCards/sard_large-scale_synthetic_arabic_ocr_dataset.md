# SARD (Large-Scale Synthetic Arabic OCR Dataset)

## 📊 Benchmark Details

**Name**: SARD (Large-Scale Synthetic Arabic OCR Dataset)

**Overview**: SARD is a massive, synthetically generated dataset specifically designed to simulate book-style documents, comprising 843,622 document images containing 690 million words, rendered across ten distinct Arabic fonts to ensure broad typographic coverage. It serves as a valuable resource for developing and evaluating robust OCR and vision-language models capable of processing diverse Arabic book-style texts.

**Data Type**: document images

**Domains**:
- Computer Vision

**Languages**:
- Arabic

**Resources**:
- [Resource](https://huggingface.co/collections/riotu-lab/sard-large-scale-synthetic-arabic-ocr-dataset-68204eae3ccd1e0216fb68ca)
- [GitHub Repository](https://github.com/riotu-lab/text2image)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality dataset for advancing Arabic OCR research and to enable more effective digitization of Arabic literary heritage.

**Target Audience**:
- ML Researchers
- OCR Engineers
- Data Scientists

**Tasks**:
- Optical Character Recognition

**Limitations**: As a purely synthetic dataset, SARD does not incorporate real-world document degradations such as uneven lighting, paper texture, ink bleed-through, or page skew.

## 💾 Data

**Source**: Synthetic generation from diverse Arabic text sources covering various domains.

**Size**: 843,622 document images containing 690 million words

**Format**: PNG

**Annotation**: Each image is paired with ground truth text generated during the synthesis process.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- Bilingual Evaluation Understudy (BLEU)

**Calculation**: Performance metrics are calculated by comparing the recognized text from OCR models to the ground truth text.

**Interpretation**: Lower CER and WER values signify better accuracy at the character and word levels, respectively. A higher BLEU score indicates greater similarity between predicted and ground truth text.

**Baseline Results**: Initial benchmark results include various models tested on the dataset, showing a range of performance metrics.

**Validation**: Validation is achieved through performance evaluations against multiple OCR models using the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
