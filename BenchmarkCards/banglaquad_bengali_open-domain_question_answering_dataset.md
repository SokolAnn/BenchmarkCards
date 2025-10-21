# BanglaQuAD (Bengali Open-domain Question Answering Dataset)

## 📊 Benchmark Details

**Name**: BanglaQuAD (Bengali Open-domain Question Answering Dataset)

**Overview**: BanglaQuAD is a Bengali question answering dataset containing 30,808 high-quality human-annotated question-answer pairs constructed from Bengali Wikipedia articles by native speakers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Resources**:
- [GitHub Repository](https://github.com/rashad101/BanglaQuAD-LREC-COLING-24)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for developing question answering and information retrieval systems in Bengali.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Bengali Wikipedia articles

**Size**: 30,808 question-answer pairs

**Format**: JSON

**Annotation**: Human annotation by native Bengali speakers

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: Metrics are calculated based on the performance of baseline models on the BanglaQuAD dataset.

**Interpretation**: A higher value in EM and F1 score indicates better performance by the QA model on the dataset.

**Baseline Results**: BanglaBERT and IndicBERT scores on BanglaQuAD dataset are 22.92 (EM) and 39.38 (F1) for BanglaBERT, and 21.50 (EM) and 37.22 (F1) for IndicBERT.

**Validation**: The dataset construction process is validated through qualitative analysis and inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
