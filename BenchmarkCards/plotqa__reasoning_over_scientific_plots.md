# PlotQA: Reasoning over Scientific Plots

## 📊 Benchmark Details

**Name**: PlotQA: Reasoning over Scientific Plots

**Overview**: Specifically, we propose PlotQA with 28.9 million question-answer pairs over 224,377 plots on data from real-world sources and questions based on crowd-sourced question templates.

**Data Type**: question-answer pairs over plot images

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FigureQA
- DVQA
- VQA
- CLEVR
- TextVQA
- FigureSeer

**Resources**:
- [Resource](https://bit.ly/PlotQA)
- [Resource](https://arxiv.org/abs/1909.00997)
- [GitHub Repository](https://github.com/tesseract-ocr/tesseract)

## 🎯 Purpose and Intended Users

**Goal**: To reduce the gap between existing synthetic plot datasets and real-world plots and question templates by proposing PlotQA, a large dataset that exposes the need to train models for questions that have answers from an Open Vocabulary.

**Tasks**:
- Question Answering
- Visual Question Answering
- Optical Character Recognition
- Object Detection
- Table Question Answering
- Numerical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from World Bank Open Data, Open Government Data, Global Terrorism Database, and similar online data sources (crawled indicator variables and entities).

**Size**: 224,377 plots; 28,952,641 question-answer pairs

**Format**: N/A

**Annotation**: Bounding box annotations for legend boxes, legend names, legend markers, axes titles, axes ticks, bars, lines, and title. Questions generated from 74 templates extracted from 7,000 crowd-sourced questions (paraphrased and instantiated).

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy, mAP, F1-score, IOU)
- Human evaluation (human accuracy measured on subset)

**Metrics**:
- Accuracy
- Mean Average Precision (mAP)
- F1 Score
- Intersection over Union (IOU)

**Calculation**: Textual answers: exact match. Numeric (floating point) answers: considered correct if within 5% of the correct answer. VED evaluated using mAP at IOU thresholds (0.5, 0.75, 0.9). SIE evaluated using F1-score on extracted tuples. OCR evaluated in oracle and pipeline modes.

**Interpretation**: Higher Accuracy indicates better model performance; human accuracy on a subset is 80.47% (reference upper-bound). The dataset is challenging as state-of-the-art models achieve substantially lower accuracy than humans.

**Baseline Results**: On PlotQA (accuracy): IMG-only 4.84%, QUES-only 5.35%, BAN 0.01%, LoRRA 0.02%, SAN 7.76%, Our Model 22.52%. On DVQA: SAN 32.1%, SANDY-OCR 45.77% (reported), Our Model 57.99% (DVQA test).

**Validation**: Train/Validation/Test splits: 70%/15%/15% on 224,377 plots (Train: 157,070 images, 20,249,479 QA pairs; Validation: 33,650 images, 4,360,648 QA pairs; Test: 33,657 images, 4,342,514 QA pairs). Human evaluation performed on 5,860 questions across 160 images (human accuracy 80.47%). Module-level evaluation includes oracle vs pipeline OCR, VED measured at multiple IOU thresholds, and SIE evaluated via F1 on tuples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
