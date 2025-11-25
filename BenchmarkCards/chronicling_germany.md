# Chronicling Germany

## 📊 Benchmark Details

**Name**: Chronicling Germany

**Overview**: The Chronicling Germany dataset contains 801 annotated historical newspaper pages from the time period between 1617 and 1933, designed to enable the training of layout and OCR models for historic German-language newspapers.

**Data Type**: annotated newspaper pages

**Domains**:
- Natural Language Processing
- Computer Vision
- Digital History

**Languages**:
- German

**Similar Benchmarks**:
- Europeana

**Resources**:
- [Resource](https://gitlab.uni-bonn.de/digital-history/Chronicling-Germany-Dataset)
- [GitHub Repository](https://github.com/Digital-History-Bonn/Chronicling-Germany-Code)

## 🎯 Purpose and Intended Users

**Goal**: To reduce the character error rate and improve the detection of individual elements of historical newspaper pages for research and machine learning purposes.

**Target Audience**:
- Historians
- Machine Learning Researchers
- Digital Humanists

**Tasks**:
- Layout Detection
- Optical Character Recognition (OCR)

**Limitations**: N/A

## 💾 Data

**Source**: 801 historical newspaper pages annotated by student assistants with a background in history.

**Size**: 801 pages

**Format**: PAGE-XML

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Levenshtein distance

**Calculation**: Metrics are calculated using pixel-wise comparisons for layout detection and character recognition accuracy for OCR.

**Interpretation**: Higher F1 scores indicate better accuracy in layout detection and OCR tasks.

**Baseline Results**: Initial tests show an F1 score for the paragraph class of 0.97 and a Levenshtein distance of 0.022 per character.

**Validation**: The dataset includes validation and test datasets split into in-distribution and out-of-distribution sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation from OCR errors in historical text.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
