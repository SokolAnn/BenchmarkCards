# AltChart

## 📊 Benchmark Details

**Name**: AltChart

**Overview**: AltChart is a dataset comprising 10,000 real chart images, each paired with comprehensive summaries featuring long-context and semantically rich annotations, aimed at enhancing accessibility for blind and visually impaired individuals.

**Data Type**: chart-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/moured/AltChart)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rich dataset for chart summarization tasks that enhances accessibility for blind and visually impaired individuals.

**Target Audience**:
- ML Researchers
- Accessibility Researchers
- Data Visualization Developers

**Tasks**:
- Chart Summarization

**Limitations**: Despite having diverse chart categories, the model still tends to hallucinate and produce factually incorrect statements, particularly with complex charts.

## 💾 Data

**Source**: Collected from HCI publications across five ACM conferences (CHI, ASSETS, DIS, UIST, W4A) from 2015 to 2023.

**Size**: 10,000 images

**Format**: JPEG

**Annotation**: Manual annotation by experts for semantically rich descriptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score

**Calculation**: Metrics are calculated based on the semantic similarity and informativeness of generated summaries compared to human-authored summaries.

**Interpretation**: Higher scores indicate better performance in generating accurate and comprehensive chart summaries.

**Validation**: The dataset was validated by rigorous manual checks on a subset of the images to ensure adherence to accessibility guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: The dataset aims to improve accessibility for blind and visually impaired individuals, fostering inclusive data representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
