# MOLE (Metadata Extraction and Validation in Scientific Papers Using LLMs)

## 📊 Benchmark Details

**Name**: MOLE (Metadata Extraction and Validation in Scientific Papers Using LLMs)

**Overview**: MOLE is a framework using Large Language Models (LLMs) to automatically extract and validate metadata attributes from scientific papers covering datasets of multiple languages, including Arabic, English, Russian, French, and Japanese.

**Data Type**: structured metadata

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- English
- Russian
- French
- Japanese

**Similar Benchmarks**:
- Masader

**Resources**:
- [GitHub Repository](https://github.com/IVUL-KAUST/MOLE)
- [Resource](https://huggingface.co/datasets/IVUL-KAUST/MOLE)

## 🎯 Purpose and Intended Users

**Goal**: To automate the extraction and validation of metadata from scientific papers, enhancing research discovery and reproducibility.

**Target Audience**:
-  Researchers
- Data Scientists
- Natural Language Processing Practitioners

**Tasks**:
- Metadata Extraction
- Validation

**Limitations**: N/A

## 💾 Data

**Source**: 126 annotated scientific papers covering datasets in multiple languages.

**Size**: 1,000 tokens

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human annotation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on matching extracted metadata with ground truth in the annotated papers.

**Interpretation**: High precision indicates fewer hallucinated values, while high recall shows accurate prediction of existing metadata.

**Baseline Results**: N/A

**Validation**: The annotations were verified by two authors to ensure consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
