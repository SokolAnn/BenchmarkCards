# PDF-MVQA (PDF-based Visual Question Answering)

## 📊 Benchmark Details

**Name**: PDF-MVQA (PDF-based Visual Question Answering)

**Overview**: PDF-MVQA is a new multi-page, multimodal document entity retrieval dataset designed to facilitate visual question answering in text-dense documents. It addresses challenges in understanding hierarchically structured semantic relationships across multiple pages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- DocCVQA
- RDVQA
- VisualMRC

**Resources**:
- [Resource](https://arxiv.org/abs/2404.12720)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the effectiveness of vision-and-language models in handling multi-page document understanding and information retrieval.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Multimodal Document Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Collected from PubMed Central, encompassing research articles, review articles, and systematic reviews.

**Size**: 3,146 documents, 30,239 pages

**Format**: CSV

**Annotation**: Automatically generated questions and answers based on the contents of the documents, using ChatGPT for question generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Matching (EM)
- Partial Matching (PM)
- Multi-Label Recall (MR)

**Calculation**: Metrics are calculated based on the proportion of correctly identified document entities against ground truth in the context of given questions across multiple pages.

**Interpretation**: Higher scores indicate better performance in retrieving relevant document entities as support for answering questions. EM is strict about exact matches, while PM allows for partial correctness.

**Baseline Results**: Various models including RoI-based and Patch-based frameworks, achieving different performance levels across metrics.

**Validation**: Experimentally validated through quantitative and qualitative analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading or incorrect answers affecting decision-making processes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Appropriate measures taken to anonymize patient-related data where applicable.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
