# BuDDIE (Business Document Dataset for Multi-task Information Extraction)

## 📊 Benchmark Details

**Name**: BuDDIE (Business Document Dataset for Multi-task Information Extraction)

**Overview**: BuDDIE is the first multi-task dataset of 1,665 real-world business documents that contains rich and dense annotations for Document Classification (DC), Key Entity Extraction (KEE), and Visual Question Answering (VQA).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RVL-CDIP
- FUNSD
- SROIE

**Resources**:
- [GitHub Repository](https://github.com/jpmchase/BuDDIE)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate research in visually rich document understanding by providing a multi-task dataset that addresses three distinct tasks: Document Classification, Key Entity Extraction, and Visual Question Answering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Document Classification
- Key Entity Extraction
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available business entity documents from US state government websites.

**Size**: 1,665 documents

**Format**: N/A

**Annotation**: Annotated by a team of annotators using specific guidelines for each task.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score
- Precision
- Recall
- Accuracy
- Average Normalized Levenshtein Similarity (ANLS)

**Calculation**: Metrics are calculated according to standard practices in document classification, entity extraction, and question answering.

**Interpretation**: Higher F1 scores indicate better model performance across tasks. For DC, macro F1 is used due to imbalanced classes; KEE uses weighted averages; VQA metrics include accuracy for boolean questions and ANLS for span questions.

**Baseline Results**: The best baseline for each task includes BERT, RoBERTa, LayoutLM, LayoutLMv3, GPT4, and DocLLM, achieving F1 scores of 99.15 for DC, 89.97 for KEE, and 89.58 for VQA respectively.

**Validation**: The dataset was validated through a two-round annotation process involving initial assignments and subsequent checks for agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Harmful output', 'Toxic output']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: BuDDIE is publicly available for non-commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
