# A document processing pipeline for the construction of a dataset for topic modeling based on the judgments of the Italian Supreme Court

## 📊 Benchmark Details

**Name**: A document processing pipeline for the construction of a dataset for topic modeling based on the judgments of the Italian Supreme Court

**Overview**: We developed a document processing pipeline that generates an anonymized dataset of legal judgments optimized for topic modeling, addressing challenges such as limited datasets in the Italian legal domain.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Italian

**Resources**:
- [Resource](https://www.italgiure.giustizia.it/sncass/)

## 🎯 Purpose and Intended Users

**Goal**: To create a novel dataset from Italian Supreme Court judgments for the purpose of applying topic modeling and ensuring compliance with privacy regulations.

**Target Audience**:
- Researchers in legal NLP
- Legal professionals
- Data scientists

**Tasks**:
- Topic Modeling

**Limitations**: The anonymization module lacks systematic quantitative validation due to time constraints.

## 💾 Data

**Source**: Italian Supreme Court published judgments, ordinances, and decrees available on the Italgiure website.

**Size**: 307 judgments

**Format**: JSON

**Annotation**: Manual annotation using Label Studio, following DocLayNet annotation scheme.

## 🔬 Methodology

**Methods**:
- Document Layout Analysis
- Optical Character Recognition (OCR)
- Named Entity Recognition (NER)
- Topic Modeling

**Metrics**:
- mean Average Precision (mAP)
- Character Error Rate (CER)
- Word Error Rate (WER)
- topic coherence (Cv)
- topic diversity

**Calculation**: Metrics were calculated based on the performance of various models used in the pipeline and topic modeling quality.

**Interpretation**: Higher values indicate better performance in detection, recognition, and topic quality.

**Baseline Results**: mAP@50 of 0.964 and mAP@50-95 of 0.800 for DLA; CER of 0.0047 and WER of 0.0248 for OCR; topic diversity of 0.6198 and coherence score of 0.663.

**Validation**: The benchmark was validated through a detailed evaluation against expert interpretations and comparisons with previous methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures were integrated to ensure compliance with GDPR guidelines.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The pipeline aims to meet GDPR requirements for data anonymization.
