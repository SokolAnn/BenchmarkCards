# AMuRD (Annotated Arabic-English Receipt Dataset for Key Information Extraction and Classification)

## 📊 Benchmark Details

**Name**: AMuRD (Annotated Arabic-English Receipt Dataset for Key Information Extraction and Classification)

**Overview**: AMuRD is a novel multilingual human-annotated dataset specifically designed for information extraction from receipts, comprising 47,720 samples with detailed annotations for key item attributes.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Retail

**Languages**:
- Arabic
- English

**Similar Benchmarks**:
- WildReceipt
- SROIE

**Resources**:
- [GitHub Repository](https://github.com/Update-For-Integrated-Business-AI/AMuRD)
- [Resource](https://arxiv.org/abs/2307.11278)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for key information extraction and classification tasks from scanned receipts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Extraction
- Item Classification

**Limitations**: The dataset does not always represent full receipts, which could limit the models’ ability to accurately classify and extract information.

## 💾 Data

**Source**: Collected from the DISCO application with receipts from various retail and commercial establishments.

**Size**: 47,720 samples

**Format**: Text

**Annotation**: Human-annotated with item names, attributes like price and brand, and classification into product categories.

## 🔬 Methodology

**Methods**:
- Fine-tuning language models (LLaMA V1 and V2)
- Evaluation using precision, recall, F1 score, and accuracy

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics calculated based on model performance on training, validation, and test datasets.

**Interpretation**: Higher F1 scores and accuracy indicate better performance in information extraction and classification tasks.

**Validation**: Data validation performed by a head annotator to ensure annotation accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes diverse receipts across multiple product categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International (CC-BY-NC-ND 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
