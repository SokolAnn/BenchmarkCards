# DocGenome

## 📊 Benchmark Details

**Name**: DocGenome

**Overview**: DocGenome is a large-scale scientific document benchmark constructed from 500K annotated documents from the arXiv open-access repository, designed to enhance multi-modal large language models' understanding of scientific documents by providing structured information from various modalities including text, figures, equations, and tables.

**Data Type**: document-oriented tasks

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- PubLayNet
- DocVQA
- DocBank
- DocLayNet

**Resources**:
- [Resource](https://unimodal4reasoning.github.io/DocGenome_page)
- [GitHub Repository](https://github.com/UniModal4Reasoning/DocGenome)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured and comprehensive dataset that enhances the ability of multi-modal large language models to understand and process scientific documents.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Document Classification
- Document Layout Detection
- Visual Grounding
- Document Transformation
- Open-ended Single-page Question Answering
- Multi-page Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 500K scientific documents from the arXiv open-access community.

**Size**: 500K documents

**Format**: N/A

**Annotation**: Auto-annotated using the DocParser pipeline.

## 🔬 Methodology

**Methods**:
- Auto-annotation via DocParser
- Human validation on generated QA pairs

**Metrics**:
- Accuracy
- Edit Distance
- Mean Average Precision (mAP)

**Calculation**: Metrics are calculated based on model performance on test tasks such as classification accuracy and quality of QA pairs.

**Interpretation**: Higher accuracy indicates better model performance, while lower edit distances and higher mAP values represent improved alignment with ground truth.

**Baseline Results**: N/A

**Validation**: Extensive validation through human review of QA pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
