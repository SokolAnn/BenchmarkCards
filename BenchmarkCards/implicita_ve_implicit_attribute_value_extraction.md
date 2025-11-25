# ImplicitA VE (Implicit Attribute Value Extraction)

## 📊 Benchmark Details

**Name**: ImplicitA VE (Implicit Attribute Value Extraction)

**Overview**: ImplicitA VE is the first publicly available multimodal dataset for implicit attribute value extraction, sourced from the MA VE dataset, consisting of 68k training and 1.6k testing data across five domains.

**Data Type**: text and image

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HenryPengZou/ImplicitAVE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for multimodal large language models (MLLMs) on implicit attribute value extraction.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Attribute Value Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from the MA VE dataset and expanded to include implicit A VE.

**Size**: 68,604 training instances and 1,610 evaluation instances

**Format**: N/A

**Annotation**: Validated through two rounds of human inspection.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro-F1

**Calculation**: Micro-F1 score calculated between the ground truth answer and the model-generated answer for each attribute.

**Interpretation**: Higher micro-F1 scores indicate better performance in implicit attribute value extraction tasks.

**Validation**: Test set annotations validated through human inspection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets are sourced from publicly available data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
